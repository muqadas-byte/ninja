"""
Stories Ninja — Streamlit app: PRD → user stories via Claude API.
Edit files in ./prompts/ to change agent instructions.
"""

from __future__ import annotations

import os
import traceback

import streamlit as st
from anthropic import Anthropic

from prompt_loader import load_system_prompt
from utils.docx_export import markdown_to_docx_bytes
from utils.prd_loaders import extract_from_bytes

DEFAULT_MODEL = "claude-sonnet-4-20250514"


def _normalize_api_key(raw: str | None) -> str:
    """Strip edges and remove accidental newlines/spaces (common when pasting)."""
    if not raw:
        return ""
    return "".join(raw.strip().split())


def _api_key_from_env_or_secrets() -> str | None:
    if os.environ.get("ANTHROPIC_API_KEY"):
        n = _normalize_api_key(os.environ["ANTHROPIC_API_KEY"])
        return n or None
    try:
        n = _normalize_api_key(st.secrets.get("ANTHROPIC_API_KEY", ""))
        return n or None
    except Exception:
        return None


def _effective_api_key(manual: str) -> str | None:
    """Typed key wins so you can override env/secrets without restarting."""
    m = _normalize_api_key(manual)
    if m:
        return m
    return _api_key_from_env_or_secrets()


def _is_likely_anthropic_key(key: str) -> bool:
    return key.startswith("sk-ant-")


def _render_auth_error_help() -> None:
    st.error("**Authentication failed (401):** Anthropic rejected this API key (`invalid x-api-key`).")
    st.markdown(
        """
**Checklist**

1. **Use a Secret key** from [console.anthropic.com](https://console.anthropic.com/) → **API keys** — it should start with `sk-ant-` (not an OpenAI `sk-proj-…` key, not a “Project” ID).
2. **Paste only the key** — no word `Bearer`, no quotes, no spaces or line breaks in the middle.
3. **Override a bad env value** — if `ANTHROPIC_API_KEY` is set in your system or `.env`, it may be stale. Paste the correct key in the **Anthropic API key** field above (that overrides env/secrets for this app).
4. **Create a new key** if the old one was rotated, revoked, or never had billing/API access enabled for your workspace.
        """
    )


def _looks_like_auth_failure(exc: BaseException) -> bool:
    if getattr(exc, "status_code", None) == 401:
        return True
    s = str(exc).lower()
    if "401" in s or "authentication_error" in s or "invalid x-api-key" in s:
        return True
    return type(exc).__name__ == "AuthenticationError"


def _resolve_prd_text(uploaded_name: str | None, uploaded_bytes: bytes | None, pasted: str) -> tuple[str, str]:
    """Returns (prd_text, source_description)."""
    if uploaded_bytes and uploaded_name:
        try:
            text = extract_from_bytes(uploaded_name, uploaded_bytes).strip()
            if not text:
                raise ValueError("No text could be extracted from the file.")
            return text, f"file: {uploaded_name}"
        except Exception as e:
            raise ValueError(f"Could not read file: {e}") from e
    pasted = (pasted or "").strip()
    if pasted:
        return pasted, "pasted text"
    raise ValueError("Provide a PRD by uploading a file (.docx, .pdf, .odt) or pasting text.")


def main() -> None:
    st.set_page_config(page_title="Stories Ninja", page_icon="📋", layout="wide")
    st.title("Stories Ninja")
    st.caption("Turn a PRD into epics and user stories using Claude. Edit `prompts/*.md` to change behaviour.")

    st.subheader("Claude API")
    key_col, model_col = st.columns([3, 2])
    with key_col:
        manual_key = st.text_input(
            "Anthropic API key",
            type="password",
            placeholder="sk-ant-api03-…",
            help="From console.anthropic.com. Leave empty to use ANTHROPIC_API_KEY or `.streamlit/secrets.toml`.",
            key="anthropic_api_key_field",
        )
    with model_col:
        model = st.text_input(
            "Model",
            value=os.environ.get("CLAUDE_MODEL", DEFAULT_MODEL),
            help="Override with env CLAUDE_MODEL",
            key="claude_model_field",
        )

    api_key = _effective_api_key(manual_key)
    fallback = _api_key_from_env_or_secrets()
    if api_key and fallback and not _normalize_api_key(manual_key):
        st.success("Using API key from environment variables or Streamlit secrets (paste a key above to override).")
    elif not api_key:
        st.warning(
            "Add your API key in the field above, or set `ANTHROPIC_API_KEY` / add `ANTHROPIC_API_KEY` to `.streamlit/secrets.toml`."
        )

    st.divider()

    col_a, col_b = st.columns(2)
    with col_a:
        uploaded = st.file_uploader(
            "PRD file (optional)",
            type=["docx", "pdf", "odt"],
            help="Word (.docx), PDF, or OpenDocument (.odt). If set, this overrides pasted text.",
        )
    with col_b:
        pasted = st.text_area("Or paste PRD text", height=220, placeholder="Paste your PRD here…")

    gen = st.button("Generate user stories", type="primary")

    if gen:
        if not api_key:
            st.error("Add an Anthropic API key in **Claude API** above, or set ANTHROPIC_API_KEY / secrets.")
            return
        name = uploaded.name if uploaded else None
        raw = uploaded.getvalue() if uploaded else None
        try:
            prd_text, source = _resolve_prd_text(name, raw, pasted)
        except ValueError as e:
            st.error(str(e))
            return

        try:
            system = load_system_prompt()
        except Exception as e:
            st.error(f"Could not load prompts: {e}")
            return

        user_msg = f"""<PRD>
{prd_text}
</PRD>

(Source: {source})"""

        if api_key and not _is_likely_anthropic_key(api_key):
            st.warning(
                "This key does not look like an Anthropic **secret** key (expected prefix `sk-ant-`). "
                "If the API returns 401, paste the key from **Anthropic Console → API keys**."
            )

        client = Anthropic(api_key=api_key)
        with st.spinner("Calling Claude…"):
            try:
                msg = client.messages.create(
                    model=model.strip() or DEFAULT_MODEL,
                    max_tokens=16384,
                    system=system,
                    messages=[{"role": "user", "content": user_msg}],
                )
            except Exception as e:
                if _looks_like_auth_failure(e):
                    _render_auth_error_help()
                    with st.expander("Technical details"):
                        st.code(traceback.format_exc())
                else:
                    st.error(f"API error: {e}")
                    with st.expander("Details"):
                        st.code(traceback.format_exc())
                return

        text_parts: list[str] = []
        for block in msg.content:
            if hasattr(block, "text"):
                text_parts.append(block.text)
        output = "".join(text_parts).strip()
        if not output:
            st.warning("Empty response from the model.")
            return

        st.subheader("Output")
        st.markdown(output)
        docx_bytes: bytes | None = None
        try:
            docx_bytes = markdown_to_docx_bytes(output)
        except Exception as e:
            st.warning(f"Could not build Word file: {e}")

        c1, c2 = st.columns(2)
        with c1:
            st.download_button(
                "Download .md",
                data=output,
                file_name="user-stories.md",
                mime="text/markdown",
                key="download_md",
            )
        with c2:
            if docx_bytes:
                st.download_button(
                    "Download .docx",
                    data=docx_bytes,
                    file_name="user-stories.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key="download_docx",
                )


if __name__ == "__main__":
    main()
