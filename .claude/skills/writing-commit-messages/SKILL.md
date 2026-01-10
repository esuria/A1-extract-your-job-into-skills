---
name: writing-commit-messages
description: Helps write and improve Git commit messages following Conventional Commits format and industry best practices. Use when the user asks to: (1) Write a commit message, (2) Review or improve a commit message draft, (3) Help with commit message format, or (4) Follow commit conventions. Analyzes git diff to ensure messages accurately reflect all changes.
---

# Writing Commit Messages

## Overview

This skill helps you write clear, consistent commit messages following the Conventional Commits specification. It can:

- Write commit messages from scratch by analyzing git changes
- Improve draft messages by comparing them against actual code changes
- Ensure messages follow industry-standard format and best practices
- Identify missed changes in your commit description

## Two Workflows

### Workflow 1: Write from Scratch

When the user asks you to write a commit message, copy this checklist and track your progress:

```
Writing Commit Message Progress:
- [ ] Step 1: Analyze git changes
- [ ] Step 2: Determine commit type
- [ ] Step 3: Identify scope (if applicable)
- [ ] Step 4: Write description
- [ ] Step 5: Add body (if needed)
- [ ] Step 6: Add footer (if applicable)
```

**Steps:**

1. **Analyze the changes**
   - Run `git status` to see modified files
   - Run `git diff` (or `git diff --staged` for staged changes) to see actual code changes

2. **Determine the commit type**
   - `feat` - New functionality added
   - `fix` - Bug fix
   - `refactor` - Code restructuring without behavior change
   - `docs` - Documentation changes only
   - `test` - Test additions or modifications
   - `chore` - Maintenance tasks (deps, config, etc.)
   - `perf` - Performance improvements
   - `style` - Formatting changes (whitespace, semicolons)
   - `ci` - CI/CD pipeline changes

3. **Identify the scope** (optional but recommended)
   - What part of the codebase? Examples: `auth`, `api`, `ui`, `database`

4. **Write the description**
   - Use imperative mood: "add feature" not "added feature"
   - Aim for 50 characters, maximum 72 characters
   - Prioritize clarity over brevity
   - Be specific and clear

5. **Add body if needed** (for complex changes)
   - Explain WHY, not WHAT (code shows what)
   - Wrap at 72 characters per line

6. **Add footer if applicable**
   - Reference issues: `Fixes #123`
   - Note breaking changes: `BREAKING CHANGE: description`

### Workflow 2: Improve Draft

When the user provides a draft commit message, copy this checklist and track your progress:

```
Improving Draft Progress:
- [ ] Step 1: Get draft message from user
- [ ] Step 2: Analyze actual git changes
- [ ] Step 3: Compare draft vs reality and identify gaps
- [ ] Step 4: Check Conventional Commits format
- [ ] Step 5: Check best practices
- [ ] Step 6: Provide detailed feedback
- [ ] Step 7: Write improved message
```

**Steps:**

1. **Get the draft message** from the user

2. **Analyze actual changes**
   - Run `git status` to see modified files
   - Run `git diff` (or `git diff --staged`) to see code changes

3. **Compare draft vs reality**
   - List all changes found in git diff
   - List what the draft message mentions
   - **Identify gaps**: What changes are missing from the draft?

4. **Check format**
   - Does it follow Conventional Commits format?
   - Is the type correct for the changes?
   - Is there a scope? Should there be one?

5. **Check best practices**
   - Imperative mood?
   - Aim for 50 characters, maximum 72 characters
   - Prioritize clarity over brevity
   - Clear and specific?

6. **Provide feedback**
   - Point out what was missed
   - Suggest format improvements
   - Offer a revised version

7. **Write improved message**
   - Include all changes from git diff
   - Follow Conventional Commits format
   - Apply best practices

## Format and Best Practices

### Conventional Commits Structure

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Example:**
```
feat(auth): add password reset functionality

Implemented email-based password reset flow with
secure token generation and expiration handling.

- Add PasswordResetController
- Create email templates
- Add rate limiting to prevent abuse

Closes #234
```

### Commit Types

| Type | Use For | Example |
|------|---------|---------|
| `feat` | New features | `feat(api): add user search endpoint` |
| `fix` | Bug fixes | `fix(auth): resolve token refresh issue` |
| `docs` | Documentation only | `docs: update API usage examples` |
| `refactor` | Code restructuring | `refactor(parser): simplify validation logic` |
| `test` | Tests only | `test(api): add integration tests for users` |
| `chore` | Maintenance | `chore: update dependencies` |
| `perf` | Performance | `perf(db): optimize query with indexing` |
| `style` | Formatting | `style: fix indentation in utils` |
| `ci` | CI/CD changes | `ci: add automated deployment` |

### Best Practices

1. **Use imperative mood**
   - ✅ "add feature" / "fix bug" / "update docs"
   - ❌ "added feature" / "fixed bug" / "updating docs"

2. **Description length**
   - Aim for 50 characters
   - Maximum 72 characters
   - Be specific but concise

3. **Scope usage**
   - Use when changes affect specific component: `feat(auth):`
   - Omit for broad changes: `chore: update dependencies`

4. **Body guidelines**
   - Explain WHY, not WHAT (code shows what changed)
   - Wrap lines at 72 characters
   - Use bullet points for multiple changes

5. **Footer usage**
   - Reference issues: `Closes #123`, `Fixes #456`
   - Breaking changes: `BREAKING CHANGE: removed legacy API`
   - Multiple footers allowed

6. **Capitalization**
   - Description starts lowercase: `feat: add feature` not `feat: Add feature`
   - Body and footer use normal capitalization

## Common Mistakes

### 1. Using Past Tense
- ❌ `fix: fixed login bug`
- ✅ `fix: resolve login bug`

### 2. Being Too Vague
- ❌ `fix: bug fix`
- ❌ `feat: add feature`
- ❌ `chore: update stuff`
- ✅ `fix(auth): resolve token expiration in sessions`
- ✅ `feat(api): add user search with filters`

### 3. Wrong Type Selection
- ❌ `feat: fix broken validation` (should be `fix`)
- ❌ `fix: add new dashboard` (should be `feat`)
- ✅ `fix: resolve validation error handling`
- ✅ `feat: add analytics dashboard`

### 4. Description Too Long
- ❌ `feat(auth): implement a new authentication system that supports OAuth, SAML, and traditional login` (89 chars)
- ✅ `feat(auth): add OAuth and SAML authentication support` (53 chars)

### 5. Missing Scope When Needed
- ❌ `fix: resolve button alignment` (which button? where?)
- ✅ `fix(ui): resolve checkout button alignment on mobile`

### 6. Draft Doesn't Match Changes
**Scenario:** User writes `fix: login bug` but git diff shows:
- Fixed login validation
- Added error logging
- Updated login tests

- ❌ Draft only mentions the fix, misses logging and tests
- ✅ `fix(auth): resolve login validation and add error logging`

### 7. Wrong Capitalization
- ❌ `feat: Add new feature`
- ✅ `feat: add new feature`

### 8. Describing HOW Instead of WHY (in body)
- ❌ Body: "Changed variable name from x to userId"
- ✅ Body: "Improve code readability by using descriptive names"

### 9. Missing Breaking Change Notice
When API/behavior changes break existing code:
- ❌ `feat: update user endpoint response`
- ✅ `feat: update user endpoint response`
  ```
  BREAKING CHANGE: User endpoint now returns { data: {...} }
  instead of flat object. Update all API clients.
  ```

### 10. Combining Unrelated Changes
- ❌ `feat: add search and fix login bug and update docs`
- ✅ Split into separate commits:
  - `feat: add user search functionality`
  - `fix: resolve login validation bug`
  - `docs: update authentication guide`

## Examples

### Simple Commits

```
feat: add dark mode toggle
```

```
fix: resolve memory leak in data processor
```

```
docs: add installation instructions to README
```

### With Scope

```
feat(auth): add Google OAuth integration
```

```
fix(api): resolve null pointer in user endpoint
```

```
refactor(database): optimize query performance
```

### With Body

```
feat(checkout): add express checkout for returning users

Implemented one-click purchase flow that pre-fills shipping
and payment information from user profile. Reduces checkout
time by approximately 60% for returning customers.

- Add ExpressCheckout component
- Update payment service integration
- Add analytics tracking for conversion rates
```

```
fix(auth): resolve token refresh race condition

JWT tokens were occasionally expiring during refresh due to
timing issues in the token rotation logic. Updated to use
atomic operations and proper locking.

Fixes #456
```

### With Breaking Changes

```
feat(api): restructure user endpoint response format

BREAKING CHANGE: User endpoint now returns nested object
{ data: { user }, meta: { timestamp } } instead of flat
user object. All API clients must be updated.

Migration guide: https://docs.example.com/migration/v2
```

### Multiple Changes in Body

```
refactor(parser): improve validation logic and error handling

Simplified the validation pipeline and added comprehensive
error messages for better debugging experience.

- Extract validation rules into separate module
- Add detailed error messages with field context
- Improve performance by caching compiled regex
- Update tests to cover edge cases

Related to #789
```

### Different Types Examples

```
test(api): add integration tests for user workflows
```

```
chore: upgrade dependencies to latest versions
```

```
perf(search): add indexing to improve query speed

Reduced search query time from ~2s to ~200ms by adding
database indexes on frequently queried fields.
```

```
ci: add automated deployment to staging environment
```

```
style(components): apply consistent formatting across UI
```

### Real-World Scenario

**User made changes:**
- Added password validation
- Fixed a bug in login form
- Updated tests

**Good commit message:**
```
feat(auth): add password strength validation

Implemented password strength checker that requires minimum
8 characters, uppercase, lowercase, number, and symbol.
Also fixed form submission bug where empty passwords were
accepted.

- Add PasswordValidator utility
- Update LoginForm validation
- Add unit tests for password rules
- Fix empty password submission bug

Closes #123, #124
```
