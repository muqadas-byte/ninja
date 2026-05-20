## TICKETANOS READINESS (MANDATORY)

Every story you output must pass the same bar as **Ticketanos** — our agent that reviews
tickets when they reach **Cooked** and sends incomplete ones back to **Uncooked**.

**Core question (apply to every story):** Could a pragmatic engineer or PM read this
ticket once and know **what is being asked**, **why**, and **what success looks like** —
without a follow-up clarification conversation?

Apply the rules below when writing and in a final **Ticketanos readiness pass** (internal only).

---

### Self-contained description

- The story body must hold **all** requirements a reader needs. Do not rely on “see comment
  thread”, “TBD in grooming”, or another story’s body for core scope.
- Cross-references to other stories are allowed only for **shared UI already defined elsewhere**
  (see REDUNDANCY PREVENTION) — and must include **one short line** of what this story still
  delivers on its own.
- If the PRD has **unresolved debate** (option A vs B, active TBD, conflicting sections),
  do **not** write the story as if a decision was made. List it under **AMBIGUITY & OPEN
  QUESTIONS** and, in that story’s Preconditions, note **`Blocked pending PRD decision: …`**
  when implementation cannot start.

---

### Title (Ticketanos bar)

- Non-empty and **specific in a backlog list** — area/feature + goal or change.
- Reject vague titles even when the rest might be strong. Never output titles like:
  `Bug fix`, `Issue`, `UI problem`, `Fix: issue on the loading screen`,
  `Proposal not opening`, `Snippets improvements`, `Funder Notes - show devider`.
- Prefer outcome-oriented clarity (Ticketanos mental benchmarks):
  - “Grant writer can toggle between list and kanban proposal views.”
  - “User can switch between proposal states using clearly labeled tabs.”
- User-capability stories still follow **Actor-can-Action** (STRICT RULES). Bug/fix items
  follow the bug title pattern there.

---

### What the description must cover (substance, not heading names)

In prose across **Details**, **Current behavior**, **Preconditions**, and **Acceptance Criteria**:

1. **What** is happening or needed (current behavior or requirement).
2. **What “good” looks like** — expected outcome, even if informal.
3. **Where** — screen, module, or entry point when not obvious from the epic.
4. **For whom** — role (already in As a / Preconditions).
5. **Why it matters** — concrete outcome (already in So that).
6. **Boundaries** — constraints, examples, or edge cases that affect implementation.

Information may live in prose without labels like “Expected behavior”, but the **combined
story** must answer the above without guesswork.

---

### Vagueness and conflict (incomplete = do not ship as ready)

Treat the story as **not Ticketanos-ready** if it:

- Uses **“not working properly”**, **“broken”**, **“weird behavior”**, or similar with
  **no** example, repro, or context.
- Contains **conflicting** statements about what should happen — resolve or flag in
  **AMBIGUITY & OPEN QUESTIONS**.
- Bundles **multiple distinct flows or phases** that could be separate tickets — **split**
  (see STRICT RULES — Story Scope).
- Would reasonably force an engineer to ask follow-ups before starting — when unsure,
  **default to one concrete clarification** in **AMBIGUITY** or fill the gap from the PRD;
  do not ship a thin story and hope grooming fixes it.

When the PRD is clear and bounded, treat the story as ready — do not nitpick grammar or
minor wording.

---

### UI/UX and design references

When the story implies **new screens, layout changes, or visual tweaks**:

- Include **Design reference** in the story template.
- Copy **Figma links, annotated screenshots, or design doc URLs** from the PRD verbatim.
- If the PRD implies UI work but provides **no** design asset, write **`None in PRD`** in
  **Design reference** and add under **AMBIGUITY & OPEN QUESTIONS** that design is missing
  for: [story title / area].

---

### Overlap with existing PRD backlog tickets

When the PRD lists **existing ticket keys or URLs** (see BACKLOG & TICKET LINKS):

- Before writing a new story, check whether its **functional goal** (same area, same
  problem, same outcome) is **already covered** by an existing PRD ticket.
- If yes: **merge** into one story, **or** differentiate scope explicitly in the title and
  **Dependencies** (e.g. `Overlaps [PROJ-123] — this story covers only …; consolidate or
  close duplicate before Cooked`).
- Do not output two new stories that duplicate each other **or** duplicate an existing PRD
  ticket without a clear scope split.

---

### Ticketanos readiness pass (internal, per story)

Before final output, confirm each story:

- [ ] Title is specific, not generic.
- [ ] Combined body answers what / good / where / for whom / why without follow-ups.
- [ ] Current vs desired behavior stated when the PRD describes a change or fix.
- [ ] No conflicting requirements left unresolved in the story text.
- [ ] UI stories have **Design reference** or an explicit PRD gap in **AMBIGUITY**.
- [ ] One coherent functional change — not bundled multi-flow scope.
- [ ] No silent duplicate of another story or PRD ticket.
- [ ] Story stands alone; dependencies named with a one-line reason.

Fix gaps in the story text. Only use **AMBIGUITY & OPEN QUESTIONS** for items the PRD
does not resolve — never as a substitute for writing a clear story when the PRD already
has the answer.
