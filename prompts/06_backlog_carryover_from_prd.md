## BACKLOG & TICKET LINKS FROM THE PRD

**Skip this entire section** if the user message explicitly says to **omit** **Backlog carry-over** / **Epic backlog** sections.

Otherwise, PRDs often list **existing backlog work**, **carry-over scope**, or **ticket links** (Jira, Azure DevOps, Linear, GitHub Issues, etc.). That information must **not** be dropped when you write stories.

### What to capture

- Ticket **keys** (e.g. `PROJ-123`, `AB#456`) exactly as written.
- **Full URLs** exactly as written (copy/paste from the PRD — do not shorten or “fix” hosts).
- Short **labels** or **titles** next to links in tables or lists — keep them faithful to the PRD (you may trim obvious duplication, but do not invent scope).

### Where to put it

1. **Per story — required section**  
   Every story ends with **Backlog carry-over (from PRD)** (see STORY TEMPLATE).  
   - List only items the PRD **clearly ties** to that story’s scope (same feature, same screen, same epic slice).  
   - If nothing in the PRD applies: write **`None`** (do not omit the heading).

2. **Per epic — optional block**  
   After **Epic assumptions** (or the epic one-liner if there are no assumptions), add **Epic backlog / tickets (from PRD)** when the PRD mentions items that apply to the **whole epic** or **multiple stories** without a single owner.  
   - Bullets: link or key + one short line from the PRD.  
   - If there are no epic-wide items: omit this block **or** use a single line **`None`**.

### Mapping rules

- Prefer **one primary story** per ticket when possible. If the PRD ties the same ticket to two stories, list it under the **best-fit** story and under the other use: `Same as PRD ticket: [key or URL] — see **Backlog carry-over** under: [exact story title]`.
- Do **not** invent tickets, IDs, or URLs. If the PRD is silent, use **`None`** under that story’s backlog section.
- If the PRD only says “see backlog spreadsheet” without links, quote that phrase and add under **AMBIGUITY & OPEN QUESTIONS** that the backlog artifact was not inlined.

### Interaction with redundancy rules

- Do not paste the **same** long ticket paragraph under five stories — use epic-level block + one primary story, or cross-references as above.

### Overlap with existing tickets (Ticketanos)

- When a PRD ticket’s goal **matches** a new story you are writing (same area, problem, and
  outcome), do **not** duplicate scope — merge stories or state in **Dependencies** how this
  story differs from `[key or URL]` (see TICKETANOS READINESS).

---
