## STORY TEMPLATE

Use exactly this structure for every story. Do not rename, skip, or reorder fields. Keep language plain and direct — no jargon for its own sake.

---

TITLE: ### [Title following Actor-can-Action pattern]


Details:

**As a** [specific role, not just "user"]
**I want to** [specific action]
**So that** [concrete business or user outcome — not "I can use the feature"]
Keep the user story short; put extra nuance in Preconditions and Acceptance Criteria.

**Preconditions**
The exact state the system and user must be in for this story to apply.
- Use short bullets. Do not repeat the same line in every story — use **Epic assumptions** when the same context applies to the whole epic.

**Acceptance Criteria**

Write criteria in **third person** (describe the product and the user as “the user”, “the page”, “the list” — **never** “I”, “I’m”, “me”). Use **simple words** and **short lines** so the list is easy to scan.

**Format (pick one style and use it consistently within the story):**

- **Option A — Given / When / Then** (third person only), e.g.  
  `Given the user is on the dashboard, when they click Save, then the draft persists and a success message appears.`
- **Option B — Outcome bullets** (also third person), e.g.  
  `The proposals table shows columns: Name, Funder, Assignees, Due Date, Priority, Stage.`

**Density rules**

- **Do not** paste the same setup (“the user is on the dashboard”) on every line. State context once in Preconditions or the first criterion, then use shorter follow-on lines.
- Combine related checks **when they are one rule** (e.g. one line listing visible columns instead of seven lines, one per column header), unless the PRD requires separate test cases.
- Aim for **roughly 4–10** criteria per story when the PRD allows grouping; add more only when the PRD demands distinct behaviours.
- Every outcome must stay **specific and observable**:
  - Weak: “An error is shown.”
  - Strong: “An inline message appears under the field: ‘Enter a valid email’ and the form does not submit.”
- Preserve **exact strings** the PRD mandates (button labels, error text, limits). Do not drop important rules — tighten **wording and repetition**, not substance.

Use checkboxes:

- [ ] …
- [ ] …

**Edge Cases & Error States**
Short lines only: `trigger → response` (exact message or behaviour when the PRD specifies it). Do not duplicate the same generic failure text on every story — use epic-level or “standard handling” once where appropriate (see REDUNDANCY PREVENTION).

**Dependencies @PMs to look and resolve it**
- [Title of story that must ship first] — [one short reason]
  OR: None

---
