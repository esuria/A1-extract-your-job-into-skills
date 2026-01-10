# Engineering Manager Skills for Claude Code

A collection of 4 focused, reusable Claude Code skills that automate repetitive cognitive tasks from an Engineering Manager's daily workflow.

## Overview

These skills were extracted from real Engineering Manager. Each skill targets a specific, high-frequency task that consumes mental energy and time.

| Skill | Replaces | Time Saved | Frequency |
|-------|----------|------------|-----------|
| `meeting-to-minutes` | Manual meeting documentation | 15-30 min/meeting | Daily |
| `jira-ticket-writer` | Translating requirements to tickets | 10-20 min/ticket | Daily |
| `pr-review-helper` | Structuring code review feedback | 10-15 min/review | Daily |
| `writing-commit-messages` | Writing/reviewing commit messages | 5-10 min/commit | Daily |

**Total Estimated Weekly Time Saved:** ~14 hours

---

## Skills

### 1. Meeting to Minutes (`meeting-to-minutes`)

**What it replaces:** Manually synthesizing meeting notes into structured documentation with decisions and action items.

**Input:** Raw meeting notes, transcripts, or unstructured discussion summaries

**Output:**
- Narrative summary (2-4 paragraphs)
- Key decisions list
- Action items table with owner and due date
- Additional notes section

**Quality improvements:**
- Consistent format across all meeting documentation
- Never miss capturing an action item
- Professional tone suitable for stakeholder sharing
- Captures "why" context, not just "what"

**Measurable outcome:** Meeting documented within 2 minutes instead of 20+ minutes

---

### 2. JIRA Ticket Writer (`jira-ticket-writer`)

**What it replaces:** Manually translating business requirements, bug reports, or feature requests into well-structured JIRA tickets.

**Input:** Business requirement, feature request, bug report, or informal description

**Output:**
- Clear, actionable title (verb + what + context)
- Ticket type (Story/Bug/Task/Spike)
- Description with background and requirements
- Testable acceptance criteria (checkbox format)

**Quality improvements:**
- Consistent ticket structure across the team
- Forces clear acceptance criteria (testable)
- Captures business context ("why") not just implementation
- Reduces back-and-forth clarification with developers

**Measurable outcome:** Ticket created in 2 minutes instead of 15+ minutes; fewer clarification questions from developers

---

### 3. PR Review Helper (`pr-review-helper`)

**What it replaces:** Time spent structuring code review feedback and ensuring comprehensive coverage of review concerns.

**Input:** Code diff, PR changes, or code snippets

**Output:**
- Overview with verdict (Approve/Request Changes/Needs Discussion)
- Critical issues (must fix) with specific file/line references
- Suggestions (recommended improvements) with code examples
- Nitpicks (optional style items)
- Questions needing clarification
- Positive feedback section

**Quality improvements:**
- Systematic review coverage (security, performance, logic, edge cases)
- Clear severity categorization prevents blocking on minor issues
- Constructive feedback with actionable suggestions
- Consistent review quality regardless of reviewer energy level

**Measurable outcome:** Reviews completed in 5 minutes instead of 15+ minutes; more comprehensive feedback with fewer follow-up rounds

---

### 4. Writing Commit Messages (`writing-commit-messages`)

**What it replaces:** Manually crafting commit messages or reviewing draft messages against actual code changes.

**Input:** Git changes (staged/unstaged) or draft commit message to review

**Output:**
- Properly formatted Conventional Commits message
- Type, scope, and description
- Body explaining "why" (for complex changes)
- Footer with issue references and breaking changes

**Quality improvements:**
- Consistent Conventional Commits format across the team
- Messages accurately reflect all changes in the diff
- Catches missed changes when reviewing draft messages
- Enforces best practices (imperative mood, proper length, etc.)

**Measurable outcome:** Commit messages written in 1 minute instead of 5-10 minutes; consistent format across all commits

---

## Installation

These skills are already configured in the `.claude/skills/` directory:

```
.claude/
└── skills/
    ├── meeting-to-minutes/
    │   └── SKILL.md
    ├── jira-ticket-writer/
    │   └── SKILL.md
    ├── pr-review-helper/
    │   └── SKILL.md
    └── writing-commit-messages/
        └── SKILL.md
```

To use in any project:
1. Copy the `.claude/skills/` directory to your project root
2. Claude Code will automatically discover and use these skills

---

## Usage Examples

### Meeting to Minutes
```
User: Here are my notes from today's standup:
- john: auth bug still blocked
- sarah: API done, starting frontend
- discussed pushing deadline
- need to talk to devops about staging

[Claude Code invokes meeting-to-minutes skill and outputs formatted minutes]
```

### JIRA Ticket Writer
```
User: Write a ticket for this - customers want to export reports as PDF, not just CSV.
Enterprise clients need this by end of quarter.

[Claude Code invokes jira-ticket-writer skill and outputs structured ticket]
```

### PR Review Helper
```
User: Review this code change:
[pastes diff]

[Claude Code invokes pr-review-helper skill and outputs categorized review]
```

### Writing Commit Messages
```
User: Write a commit message for my staged changes

[Claude Code invokes writing-commit-messages skill, analyzes git diff, outputs formatted message]
```

```
User: Review this commit message: "fix: login bug"

[Claude Code analyzes git diff, compares to draft, suggests improvements]
```

---

## Metrics & Measurement

### Time Savings Calculation

| Skill | Tasks/Week | Old Time | New Time | Weekly Savings |
|-------|------------|----------|----------|----------------|
| meeting-to-minutes | 5 meetings | 20 min | 2 min | 90 min (1.5 hrs) |
| jira-ticket-writer | 25 tickets | 15 min | 2 min | 325 min (5.4 hrs) |
| pr-review-helper | 30 reviews | 15 min | 5 min | 300 min (5 hrs) |
| writing-commit-messages | 30 commits | 5 min | 1 min | 120 min (2 hrs) |

**Total: ~14 hours/week saved**

### Quality Metrics

- **Consistency:** 100% of outputs follow standard format
- **Completeness:** Skills check for required sections before output
- **Accuracy:** Built-in verification rules catch common omissions

---

## Who Can Reuse These Skills

These skills are designed for anyone who:
- Leads or manages technical teams
- Attends multiple meetings requiring documentation
- Writes technical tickets or requirements
- Reviews code or technical proposals
- Needs to synthesize discussions into actionable outcomes

Applicable roles:
- Engineering Managers
- Tech Leads
- Scrum Masters
- Product Managers (with technical focus)
- Senior Engineers with coordination responsibilities

---

## File Structure

```
A1-extract-your-job-into-skills/
├── README.md                    # This file
├── artifacts/
│   ├── 01-job-description.md    # Original role description
│   ├── 02-work-analysis.md      # Analysis of automation opportunities
│   ├── 03-skill-demos.md        # Skill demonstrations
│   └── 04-assignment-summary.md # Assignment summary
└── .claude/
    └── skills/
        ├── meeting-to-minutes/
        │   └── SKILL.md             # Skill 1
        ├── jira-ticket-writer/
        │   └── SKILL.md             # Skill 2
        ├── pr-review-helper/
        │   └── SKILL.md             # Skill 3
        └── writing-commit-messages/
            └── SKILL.md             # Skill 4
```

---

## Assignment Checklist

- [x] **3-5 skills** (4 skills implemented)
- [x] **Skills are small** (each skill focused on single task)
- [x] **Each skill has one clear outcome** (minutes, ticket, review, commit message)
- [x] **Each skill is measurable** (time saved, quality metrics defined)
- [x] **Skills you actually use** (derived from real daily tasks)
- [x] **Skills save time or reduce mental load** (14 hours/week)
- [x] **Skills could be reused by someone like you** (any EM/Tech Lead)
- [x] **README.md describing skills** (this file)
- [ ] **60-90 second demo recording** (use Loom to record skill usage)

---

## Demo Script (60-90 seconds)

1. **Intro (10s):** "I'm an Engineering Manager. I built 4 skills to automate my repetitive cognitive work."

2. **Meeting Minutes Demo (20s):** Paste messy meeting notes → show formatted output with actions

3. **JIRA Ticket Demo (20s):** Describe a requirement informally → show structured ticket

4. **PR Review Demo (20s):** Paste code snippet → show categorized review with verdict

5. **Commit Messages Demo (15s):** Run skill on staged changes → show Conventional Commits formatted message

6. **Wrap-up (10s):** "These skills save me 14 hours per week and ensure consistent quality."
