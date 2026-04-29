## STRICT RULES

### Story Scope
- One story = one thing a user can DO. Not a system behaviour. Not a feature area.
  One action with one outcome.
- If a story requires "and" in the title to describe what it does, split it.
- No story should touch UI AND API AND validation all at once unless they are
  genuinely inseparable from the user's perspective.

### Title Format
- Pattern: [Actor] can [specific action] [optional: context/constraint]
- The title alone must tell an engineer exactly what functionality to build.

UNACCEPTABLE — never write titles like these:
- "User management" — feature area, not a user action
- "Handle errors on the login page" — system behaviour, not user capability
- "Support proposal attachments" — vague, no actor, no action
- "Implement section locking" — engineering task disguised as a story
- Any title starting with: Implement, Build, Create, Add, Handle, Support, Manage

ACCEPTABLE — titles at this level of specificity:
- "Grant applicant can save a proposal draft mid-completion and resume it later
  without losing any entered section data"
- "Org admin can deactivate a team member account without deleting their
  contribution history on active proposals"
- "Grant writer can reorder proposal sections via drag-and-drop within a
  template without affecting other proposals using the same template"
- "System sends the grant applicant an email reminder 72 hours before a
  submission deadline they have saved to their dashboard"
- "Reviewer can approve or reject a proposal section and leave a mandatory
  comment that the writer sees before resubmitting"
- "Grant writer can attach supporting documents to a specific proposal section
  with a file size limit of 10MB per attachment"

---

### INSTRUCTIONS
- Please ensure to avoid adding unnecessary details, which are obvious.
- Do not make the ticket dumb which mentions the obvious parts (for example, authenticated user — we know that functionality is authenticated. ONLY add for the ones for example where authentication is not needed, which kind of makes sense to know (just an example))
