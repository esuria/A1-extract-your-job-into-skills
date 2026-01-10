---
name: meeting-to-minutes
description: Convert meeting notes, transcripts, or audio transcriptions into structured meeting minutes with narrative summary and action items. Use when the user pastes meeting notes, shares transcripts, needs to document outcomes, or says "summarize this meeting", "create minutes", or "extract action items".
---

# Meeting to Minutes

Convert raw meeting notes or transcripts into structured meeting minutes with a narrative summary and actionable items.

## Input

The user will provide one of:
- Raw meeting notes (bullet points, fragments)
- Meeting transcript (conversation format)
- Audio transcription output
- Unstructured discussion summary

## Output Format

Generate meeting minutes in this exact format:

```markdown
# Meeting Minutes: [Meeting Title/Topic]

**Date:** [Date if mentioned, otherwise "Not specified"]
**Attendees:** [Names if mentioned, otherwise "Not specified"]

## Summary

[2-4 paragraph narrative summary of what was discussed, key points raised, and overall context. Write in past tense, professional tone.]

## Key Decisions

- [Decision 1]
- [Decision 2]
- [Add more as needed, or "No formal decisions recorded" if none]

## Action Items

| Action | Owner | Due Date |
|--------|-------|----------|
| [Task description] | [Name or "TBD"] | [Date or "TBD"] |
| [Task description] | [Name or "TBD"] | [Date or "TBD"] |

## Notes

[Any additional context, parking lot items, or follow-up topics that don't fit above]
```

## Processing Rules

1. **Extract meeting metadata** from context clues (names, dates, topics mentioned)
2. **Write narrative summary** that captures the "why" and context, not just "what"
3. **Identify decisions** - look for phrases like "we agreed", "decided to", "will go with"
4. **Extract action items** - look for assignments, commitments, next steps
5. **Assign owners** - if names are mentioned with tasks, capture them
6. **Infer due dates** - if timelines mentioned ("by Friday", "next sprint")
7. **Keep professional tone** - suitable for sharing with stakeholders

## Quality Checks

Before outputting, verify:
- Summary is 2-4 paragraphs, not just bullet points
- All mentioned action items are captured
- Owner names match exactly as mentioned in notes
- No invented information - use "TBD" or "Not specified" when unknown
