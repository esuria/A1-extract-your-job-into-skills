# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

This repository contains custom Claude Code skills extracted from an Engineering Manager's daily workflow. The skills automate repetitive cognitive tasks like meeting documentation, JIRA ticket creation, code reviews, and commit message writing.

## Repository Structure

```
├── .claude/skills/          # Claude Code skill definitions
│   ├── meeting-to-minutes/  # Convert transcripts to meeting minutes
│   ├── jira-ticket-writer/  # Transform requirements into JIRA tickets
│   ├── pr-review-helper/    # Generate structured code review comments
│   └── writing-commit-messages/  # Write conventional commit messages
├── demo/                    # Sample inputs and generated outputs
├── logs/                    # Assignment documentation and analysis
└── README.md               # Project documentation
```

## Skills

### meeting-to-minutes
Converts raw meeting notes or transcripts into structured meeting minutes with summary, key decisions, action items table, and notes.

**Trigger phrases:** "create minutes", "summarize this meeting", "meeting notes", "extract action items"

### jira-ticket-writer
Transforms business requirements, feature requests, or bug reports into well-structured JIRA tickets with title, type, description, and acceptance criteria.

**Trigger phrases:** "create a JIRA ticket", "write up this requirement", "document this as a story"

### pr-review-helper
Analyzes code changes and generates categorized review comments with severity levels (Critical, Suggestions, Nitpicks, Questions).

**Trigger phrases:** "review this code", "check this PR", "review these changes"

### writing-commit-messages
Writes or improves Git commit messages following Conventional Commits format by analyzing the actual git diff.

**Trigger phrases:** "write a commit message", "improve this commit message", "help with commit format"

## Development Notes

- Skills are defined as markdown files in `.claude/skills/[skill-name]/SKILL.md`
- Each skill has specific input expectations and output formats
- Demo folder contains real examples of skill inputs and outputs
- This is a documentation/skills repository - no build or test commands
