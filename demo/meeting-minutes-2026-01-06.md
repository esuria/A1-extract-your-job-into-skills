# Meeting Minutes: TS Migration - Product Feedback

**Date:** January 6, 2026
**Attendees:** Emad Suria, Shahid Ali, Ravi Jani, Shoaib Mehmood, Syed M Yasir, Ahsan Zulfiqar

## Summary

The team conducted a detailed review of data mapping and migration requirements for the TimeSolv to Next Gen migration project. The discussion focused on identifying feature gaps between the two systems, determining appropriate data transformations, and establishing rules for handling edge cases during migration.

Key areas covered included time tracking features (lockout, billing increments, timer units), user permissions and roles, address field merging and truncation handling, phone number formatting, and invoice recipient configuration. The team identified several features that Next Gen does not currently support, such as start/end time tracking and the lockout feature, which will limit which customers can be migrated in the first cohort. A significant discovery was made regarding the additional invoice recipient feature where comma-separated emails inherited from clients are being treated as a single email address rather than multiple recipients.

The team agreed on several migration approaches including converting billing increment values from hours to minutes, implementing pre-migration validation to identify data loss instances before proceeding, and following TimeSolv's hierarchy rules for determining invoice email recipients. Several items require follow-up with Pablo regarding phone number formatting requirements.

## Key Decisions

- Next Gen does not have a lockout feature; time can be entered for all dates (accepted limitation)
- Billing increment values will be converted from hours (TimeSolv) to minutes (Next Gen)
- Start time/end time tracking is not supported in Next Gen; first cohort will only include customers not using this feature
- Permissions mapping will not be included in the first cohort; customers will be migrated with full permissions
- Address line 2 and 3 will be merged; pre-migration validation will identify data loss instances with option to proceed or fix
- Invoice recipient hierarchy: optional invoice contact takes precedence over main contact if email is provided

## Action Items

| Action | Owner | Due Date |
|--------|-------|----------|
| Investigate comma-separated email bug in additional invoice recipients (inherited from client showing as single email) | Ravi Jani | TBD |
| Confirm phone number formatting requirements with Pablo | Yasir / Team | TBD |
| Re-evaluate permissions migration requirement for first cohort | Shoaib Mehmood | TBD |
| Confirm address line merge implementation is complete | Syed M Yasir | Done |
| Add pre-migration validation for data loss instances (address truncation, phone formats) | Team | TBD |

## Notes

- Next Gen uses combined permissions for time and expense (view, add/edit, delete) rather than separate permissions
- Phone number validation exists on Next Gen UI but not at database level; direct migration scripts bypass UI validation
- Internal billing notes field in Next Gen is only used for pre-bill reports and does not appear on invoices
- First cohort customer selection criteria: customers not using start/end time tracking, and potentially those not using complex permissions
