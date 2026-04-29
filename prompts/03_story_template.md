## STORY TEMPLATE

Use exactly this structure for every story. Do not rename, skip, or reorder fields. Content of the ticket below is given for your reference only. Do not make things redundant in the content in the example.

---

TITLE: ### [Title following Actor-can-Action pattern]


Details:

**As a** [specific role, not just "user"]
**I want to** [specific action]
**So that** [concrete business or user outcome — not "I can use the feature"]
//Include all the details around this for great clarity.

**Preconditions**
The exact state the system and user must be in for this story to apply.
- [e.g., "User is authenticated and holds the 'Grant Writer' role"]
- [e.g., "At least one proposal exists in Draft status in the workspace"]

**Acceptance Criteria**
Write in Given/When/Then. Each criterion = one independently verifiable behaviour.
Cover: happy path, empty states, validation rules, permission boundaries, and
any limits (character counts, file sizes, maximums) the PRD specifies.

Every "Then" must be specific and observable:
- NOT: "Then an error is shown."
- YES: "Then an inline error appears below the Email field reading
       'Please enter a valid email address' and the form does not submit."

- [ ] Given [exact state], When [exact action], Then [specific, measurable outcome]
- [ ] Given [exact state], When [exact action], Then [specific, measurable outcome]
(cover every testable behaviour — do not truncate)

**Edge Cases & Error States**
For each, state the exact trigger and the exact system response:
- [Specific trigger] → [Exact system behaviour or message]
- [Specific trigger] → [Exact system behaviour or message]

**Dependencies @PMs to look and resolve it**
- [Title of story that must ship first] — [one sentence explaining why]
  OR: None

---
