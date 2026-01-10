---
name: jira-ticket-writer
description: Transform business requirements, feature requests, or bug reports into well-structured JIRA tickets with title, description, and acceptance criteria. Use when the user describes a feature, asks to "create a JIRA ticket", shares requirements, has bug reports, or says "ticket for this", "write up this requirement", or "document this as a story".
---

# JIRA Ticket Writer

Transform business requirements, feature requests, or bug reports into well-structured JIRA tickets with clear title, description, and acceptance criteria.

## Input

The user will provide one of:
- Business requirement description
- Feature request from product/stakeholders
- Bug report or customer issue
- Meeting notes with a specific item to ticket
- Verbal/informal description of work needed

## Output Format

Generate a JIRA ticket in this exact format:

```markdown
## JIRA Ticket

### Title
[Action verb] + [what] + [context/where]

### Type
[Story | Bug | Task | Spike]

### Description

**Background**
[1-2 sentences explaining why this work is needed - the business context]

**Requirements**
[Bullet points describing what needs to be done]

- Requirement 1
- Requirement 2
- Requirement 3

**Technical Notes** (if applicable)
[Any technical context that helps developers - affected areas, suggested approach, dependencies]

### Acceptance Criteria

- [ ] [Specific, testable criterion 1]
- [ ] [Specific, testable criterion 2]
- [ ] [Specific, testable criterion 3]
```

## Processing Rules

1. **Title format**: Start with action verb (Add, Implement, Fix, Update, Create)
   - Good: "Add password reset functionality to user settings"
   - Bad: "Password reset" or "User needs to reset password"

2. **Determine ticket type**:
   - **Story**: New feature or capability for users
   - **Bug**: Something broken that worked before
   - **Task**: Technical work, refactoring, infrastructure
   - **Spike**: Research or investigation needed before implementation

3. **Background section**: Answer "why" - what problem does this solve?

4. **Requirements**: Break down into specific, implementable items

5. **Acceptance Criteria rules**:
   - Must be testable (can verify pass/fail)
   - Use checkbox format for clarity
   - Cover happy path and key edge cases
   - Include non-functional requirements if mentioned (performance, security)

6. **Keep minimal**: Don't add unnecessary fields - focus on Title, Description, Acceptance Criteria

## Quality Checks

Before outputting, verify:
- Title is concise but complete (5-10 words)
- Type matches the nature of work
- Background explains the "why"
- Each acceptance criterion is independently testable
- No ambiguous terms ("should work properly" → specify what "properly" means)
