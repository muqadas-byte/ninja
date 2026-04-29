## REDUNDANCY PREVENTION (MANDATORY)

The backlog must not contain overlapping stories, copy-pasted acceptance criteria, or the same preconditions repeated in every ticket. Apply the rules below before you write the final output.

### 1. One distinct capability per story (no “two stories, one feature”)

- If two story titles describe **different entry points into the same workflow** (e.g. “invite collaborators” vs “open collaborator management from assignees column”), **merge into one story** whose title covers the user goal, **or** split so only **one** story owns “open panel, search org members, invite/remove” and the other story is deleted.
- Do not ship separate stories whose acceptance criteria largely duplicate **opening the same panel**, **same search field**, or **same list of collaborators**.

### 2. Epic-level assumptions instead of repeated preconditions

- At the **start of each epic** (after the one-line epic goal), include a short block **Epic assumptions** only when it removes repetition:
  - Example: workspace context, role, “user can reach the dashboard”, “list view vs kanban called out only where it matters”.
- In individual stories, **do not** repeat the same precondition in 10+ stories (“User is on the home dashboard”, “User has at least one proposal”) unless a story **requires an exception**. Use “Unless stated otherwise, epic assumptions apply.”

### 3. Single ownership for shared layout and copy

- **Primary CTAs**, **navigation chrome**, **sidebar**, **tab bar**: define in **one** story (the story that **owns** that screen region). Other stories **reference** that story by title, e.g. “Primary CTAs behave as defined in *[exact story title]*” — **do not** re-list the same buttons and layout.
- **Empty states** that show the same CTAs must not re-specify full button copy and layout if already owned elsewhere; reference the owning story and only add **delta** criteria (e.g. when empty state appears vs when it does not).

### 4. Cross-cutting session/tab behavior (say once)

- Patterns like “when I switch tabs, search/sort/filter/view mode applies to the new tab” or “selection clears when changing tabs” must appear **once** as an **Epic assumption** or in **one** explicitly named story (e.g. scope of dashboard state). **Do not** paste the same Given/When/Then into search, sort, filter, and view-toggle stories.

### 5. Bulk actions and selection

- **Checkbox selection**, **bulk action bar enabled/disabled**, **selection clears after successful bulk operation**: define in **one** story (or epic assumptions). Later bulk stories (archive, trash, restore, delete) reference it and only add **criteria unique to that operation** (confirmations, destinations, irreversible delete).

### 6. Repeated “generic” edge cases

- Do **not** end every story with the same generic lines (“API fails → show ‘Unable to … Please try again’”). For the epic, either:
  - add **one** epic-level line: “Standard API failure: inline or toast error with retry where applicable,” **or**
  - put detailed failure copy in the **first** story that introduces the surface, and elsewhere “Failures: standard handling for this surface (see *[story title]*)”.
- Reserve per-story edge cases for **behaviour that differs** (confirmation modals, irreversible actions, partial success).

### 7. Duplicated column / field display rules

- If multiple stories mention the same column (e.g. Assignees avatars, +N overflow, tooltips), **one** story owns column behaviour. Others say “Assignees column behaves as in *[story title]*” unless the criterion is **new**.

### 8. Self-check before output

- Re-read the full epic: if any acceptance criterion appears **twice** with minor wording changes, **delete or merge**.
- If two stories could be implemented as one PR without loss of clarity, **merge them**.

---
