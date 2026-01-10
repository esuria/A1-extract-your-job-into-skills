# Skill Demos

Sample inputs and outputs demonstrating each skill in action. Use these for your Loom recording.

---

## Demo 1: Meeting to Minutes

### Sample Input (messy meeting notes)

```
Sprint planning w/ product, dev, qa
- Mike (product): new billing dashboard priority, enterprise clients asking
- needs invoice breakdown view, export options
- Sarah: can do frontend in 2 sprints if backend ready
- Tom: backend API needs DB schema changes, maybe 1 sprint
- QA: Ali says need test data for billing scenarios
- discussed: should we delay mobile app fixes?
- decided yes, dashboard more important for Q1 goals
- Tom will sync with devops on staging DB
- need designs from UX by wednesday
- Ali to create test plan by thursday
```

### Output

# Meeting Minutes: Sprint Planning - Billing Dashboard

**Date:** Not specified
**Attendees:** Mike (Product), Sarah (Dev), Tom (Dev), Ali (QA)

## Summary

The team convened for sprint planning to discuss the prioritization of a new billing dashboard, which has been requested by enterprise clients. The dashboard will include invoice breakdown views and export options. Sarah confirmed the frontend can be completed in two sprints, contingent on backend readiness. Tom estimated one sprint for the backend API work, noting that database schema changes will be required. The team discussed whether to delay mobile app fixes and decided to prioritize the dashboard to meet Q1 goals. QA raised the need for billing-specific test data to properly validate the new functionality.

## Key Decisions

- Mobile app fixes will be delayed to prioritize the billing dashboard
- Billing dashboard is the top priority for Q1

## Action Items

| Action | Owner | Due Date |
|--------|-------|----------|
| Sync with DevOps on staging DB setup | Tom | TBD |
| Deliver billing dashboard designs | UX Team | Wednesday |
| Create test plan for billing dashboard | Ali | Thursday |
| Prepare test data for billing scenarios | Ali | TBD |

## Notes

- Frontend work depends on backend API completion
- Database schema changes required for backend
- Enterprise clients are the primary driver for this feature

---

## Demo 2: JIRA Ticket Writer

### Sample Input (informal requirement)

```
Hey, the support team is getting a lot of tickets about users not being able to find old invoices.
Apparently the invoice list only shows last 3 months and there's no way to search or filter.
Customers with years of history are frustrated. Can we add some kind of search/filter thing?
```

### Output

## JIRA Ticket

### Title
Add search and filter functionality to invoice list

### Type
Story

### Description

**Background**
Support has received multiple tickets from customers unable to locate historical invoices. The current invoice list only displays the last 3 months of data with no search or filtering capabilities. This is particularly problematic for long-term customers who have years of invoice history and need to reference past transactions.

**Requirements**
- Add date range filter allowing users to select custom start and end dates
- Add search functionality to filter invoices by invoice number, amount, or client name
- Extend default display beyond 3 months or provide "Load More" pagination
- Maintain performance with large invoice datasets

**Technical Notes**
- Invoice list is in `/billing/invoices` module
- May need backend API updates to support search parameters
- Consider indexing strategy for search fields if not already indexed
- Current 3-month limit may be a performance safeguard - verify before removing

### Acceptance Criteria

- [ ] Date range picker allows selection of any historical date range
- [ ] Search box filters results as user types (debounced, 300ms)
- [ ] Can search by invoice number, amount (partial match), and client name
- [ ] Results load within 2 seconds for customers with up to 5 years of history
- [ ] Clear filters button resets to default view
- [ ] Empty state message displays when no invoices match the filter criteria

---

## Demo 3: PR Review Helper

### Sample Input (code change)

```javascript
// New endpoint to get user billing history
app.get('/api/users/:id/billing', async (req, res) => {
  const userId = req.params.id;
  const history = await db.query(`
    SELECT * FROM billing_history
    WHERE user_id = ${userId}
    ORDER BY created_at DESC
  `);

  const total = history.reduce((sum, item) => {
    return sum + item.amount;
  }, 0);

  res.json({
    history: history,
    totalSpent: total,
    count: history.length
  });
});
```

### Output

# Code Review

## Overview
This PR adds a new endpoint to retrieve user billing history with aggregated spending data. The implementation has a critical SQL injection vulnerability that must be fixed before merge.

**Verdict:** Request Changes

---

## Critical Issues

### 1. SQL Injection Vulnerability
**File:** `routes/billing.js` | **Line:** 4-7
```javascript
const history = await db.query(`
  SELECT * FROM billing_history
  WHERE user_id = ${userId}
  ...
`);
```
**Issue:** Direct string interpolation of `userId` in the SQL query allows SQL injection attacks. An attacker could pass `1 OR 1=1` as the ID to dump all billing records, or worse.
**Suggestion:** Use parameterized queries:
```javascript
const history = await db.query(
  'SELECT * FROM billing_history WHERE user_id = ? ORDER BY created_at DESC',
  [userId]
);
```

### 2. Missing Authentication Check
**File:** `routes/billing.js` | **Line:** 2
```javascript
app.get('/api/users/:id/billing', async (req, res) => {
```
**Issue:** No authentication or authorization check. Any user could access any other user's billing history by changing the ID parameter.
**Suggestion:** Add auth middleware and verify the requesting user owns this data:
```javascript
app.get('/api/users/:id/billing', authMiddleware, async (req, res) => {
  if (req.user.id !== parseInt(req.params.id) && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  // ... rest of handler
});
```

---

## Suggestions

### 1. Add Input Validation
**File:** `routes/billing.js` | **Line:** 3
**Current:**
```javascript
const userId = req.params.id;
```
**Suggested:**
```javascript
const userId = parseInt(req.params.id, 10);
if (isNaN(userId)) {
  return res.status(400).json({ error: 'Invalid user ID' });
}
```
**Why:** Validates input early and provides clear error message for malformed requests.

### 2. Add Pagination
**File:** `routes/billing.js` | **Line:** 4-7
**Why:** `SELECT *` without LIMIT could return thousands of records for long-term users, causing performance issues and large response payloads. Consider adding `LIMIT` and `OFFSET` with query parameters.

---

## Nitpicks

- Consider using `async/await` error handling with try/catch and proper error responses
- `history` could be renamed to `billingRecords` for clarity

---

## Questions

- Is there a rate limit on this endpoint to prevent abuse?
- Should we exclude cancelled/refunded transactions from `totalSpent`?

---

## What's Good

- Clean, readable async/await pattern
- Useful aggregation (total spent, count) saves frontend from calculating
- Logical sorting by `created_at DESC` shows recent first
- Response structure is well-organized and easy to consume
