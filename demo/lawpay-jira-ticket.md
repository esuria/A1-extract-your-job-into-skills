# JIRA Ticket

## Title
Improve LawPay error messaging, event processing logic, and logging accuracy

## Type
Task

## Description

**Background**
The LawPay integration has several issues affecting developer experience and operational visibility. Error messages are not user-friendly, the event processing logic incorrectly identifies tenants in non-production environments due to shared sandbox merchantAccountIDs, and this causes incorrect tenant information to appear in OutSystems logs.

**Requirements**

- Update error messages throughout the LawPay integration to be clear, actionable, and user-friendly
- Refactor event processing logic to correctly identify the tenant when multiple accounts share the same sandbox merchantAccountID in non-prod environments
- Fix OutSystems logging to report the correct tenant after the event processing logic is corrected

**Technical Notes**
- The root cause of the logging issue is the event processing logic failing to fetch the correct tenant initially
- Non-prod environments use a shared sandbox merchantAccountID across all accounts, which causes tenant lookup to return the wrong result
- Once the event processing logic is fixed, the logging issue should resolve as a downstream effect

## Acceptance Criteria

- [ ] Error messages displayed to users are clear, non-technical, and provide guidance on resolution steps
- [ ] Event processing correctly identifies the tenant on the first attempt in non-prod environments with shared sandbox merchantAccountIDs
- [ ] OutSystems logs show the correct tenant ID/name for all LawPay events
- [ ] Existing functionality in production environments remains unaffected
- [ ] Solution is tested in non-prod environment with multiple accounts sharing the same sandbox merchantAccountID
