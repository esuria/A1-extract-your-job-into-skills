---
name: pr-review-helper
description: Analyze code changes, diffs, or PRs and generate structured review comments categorized by severity. Use when the user pastes code diff, asks to "review this code" or "check this PR", wants feedback on changes before merging, or says "what do you think of this change", "review these changes", or "any issues here".
---

# PR Review Helper

Analyze code changes (diffs, PRs) and generate structured review comments categorized by severity, helping provide thorough, consistent code reviews.

## Input

The user will provide one of:
- Git diff output
- Code snippets (before/after)
- PR description with code changes
- Link context with pasted code

## Output Format

Generate a code review in this exact format:

```markdown
# Code Review

## Overview
[1-2 sentence summary of what the changes do and overall assessment]

**Verdict:** [Approve | Request Changes | Needs Discussion]

---

## Critical Issues
[Must be fixed before merge - bugs, security issues, data loss risks]

> None found.

OR

### 1. [Issue Title]
**File:** `filename.ext` | **Line:** X-Y
```
[relevant code snippet]
```
**Issue:** [What's wrong and why it matters]
**Suggestion:** [How to fix it]

---

## Suggestions
[Recommended improvements - better patterns, performance, maintainability]

> None.

OR

### 1. [Suggestion Title]
**File:** `filename.ext` | **Line:** X-Y
**Current:**
```
[current code]
```
**Suggested:**
```
[improved code]
```
**Why:** [Benefit of this change]

---

## Nitpicks
[Minor style/preference items - optional to address]

- [Nitpick 1]
- [Nitpick 2]

---

## Questions
[Clarifications needed to complete review]

- [Question 1]
- [Question 2]

---

## What's Good
[Positive feedback - good patterns, clever solutions, improvements noticed]

- [Positive observation 1]
- [Positive observation 2]
```

## Processing Rules

1. **Categorize by severity**:
   - **Critical**: Bugs, security vulnerabilities, data corruption risks, breaking changes
   - **Suggestions**: Performance improvements, better patterns, maintainability
   - **Nitpicks**: Naming, formatting, style preferences (if no linter)
   - **Questions**: Unclear intent, missing context, design clarifications

2. **Review focus areas** (check each):
   - Logic correctness - does the code do what it claims?
   - Edge cases - null checks, empty arrays, boundary conditions
   - Security - injection risks, auth checks, data exposure
   - Performance - N+1 queries, unnecessary loops, memory leaks
   - Error handling - are failures handled gracefully?
   - Naming clarity - do names reflect purpose?
   - Code duplication - is there unnecessary repetition?

3. **Provide actionable feedback**:
   - Bad: "This could be better"
   - Good: "Consider using `Array.map()` instead of forEach with push - it's more idiomatic and returns the new array directly"

4. **Include positive feedback**: Always find something good to acknowledge

5. **Verdict logic**:
   - **Approve**: No critical issues, suggestions are optional
   - **Request Changes**: Has critical issues that must be fixed
   - **Needs Discussion**: Architectural concerns or unclear requirements need sync

## Quality Checks

Before outputting, verify:
- All critical issues explain WHY it's a problem
- Suggestions include concrete code examples where helpful
- Feedback is respectful and constructive
- "What's Good" section has at least one item
- Verdict matches the severity of issues found
