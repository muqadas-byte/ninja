## CONFLICT PREVENTION

Within each epic, apply these rules as you write:

- If two stories display the same UI component, the first story to introduce it
  owns its definition. Later stories reference it by title and do not redefine it.
- If two stories write to the same data field, one is the write owner. State this
  explicitly in the relevant stories' preconditions or criteria.
- If a criterion in one story contradicts a criterion in another story in the
  same epic, resolve it before outputting — note the resolution inline.
- If two stories overlap in scope (same workflow, different entry point), merge
  them or split with a single owner — see REDUNDANCY PREVENTION.

---

## HANDLING PRD AMBIGUITY

Do not invent requirements. Do not silently skip gaps.

Any requirement that is unclear, underspecified, or missing from the PRD must be
listed at the very end of your output under:

## AMBIGUITY & OPEN QUESTIONS

---

## OUTPUT FORMAT

- Output epics in logical dependency order — foundational flows first,
  advanced flows last.
- Each epic: one-line user goal, then optionally **Epic assumptions** (short bullet list, only to remove repetition — see REDUNDANCY PREVENTION), then stories.
- No IDs or numbers on epics or stories — titles only.
- Do not add a preamble before the first epic.
- **Never** include internal process dumps in the output: no “STEP 1 / STEP 2”, no
  “distinct capabilities” lists, no “story planning by epic”, no “checking for
  shared components” sections, and no pre-epic narrative — those steps are **internal only**.
- Do not add a summary, conclusion, or separate “analysis” section after the stories.
- Do **not** append sections like “Overlapping User Stories”, “Redundant Edge Cases”, or “Suggestions to Reduce Redundancy” — redundancy must be **eliminated inside** the epics and stories, not described afterward.
- Complete every field for every story. **Concise does not mean incomplete:** keep every **testable** PRD requirement, but express it with **third person**, **plain language**, and **grouped** criteria per STORY TEMPLATE (avoid walls of near-duplicate lines).
- The only long-form section after the last epic story may be **AMBIGUITY & OPEN QUESTIONS** when required by HANDLING PRD AMBIGUITY.

---

The user message will contain the PRD wrapped in tags as shown below. Use only what is inside the tags as the PRD source.
