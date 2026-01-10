# Commit Message Skill Demo

## Input: Git Diff Analysis

The skill analyzed the following changes in `demo/src/user_validator.py`:

- Added `re` import for regex validation
- `validate_email`: replaced naive `@` check with proper RFC-compliant regex pattern, added null/type checks
- `validate_password`: increased minimum from 6 to 8 chars, added uppercase/lowercase/digit requirements, added null/type checks
- `validate_username`: added max length (20), added alphanumeric+underscore pattern validation, added null/type checks
- `register_user`: now collects ALL validation errors instead of returning on first failure, improved error messages
- Updated test cases in `__main__`

## Analysis

| Step | Result |
|------|--------|
| Commit Type | `fix` - security bug fixes (weak validation was allowing invalid/insecure input) |
| Scope | `validation` - all changes are in the validation module |
| Breaking Change | No |

## Generated Commit Message

```
fix(validation): strengthen user input validation rules

Replace weak validation logic with secure, comprehensive checks
to prevent invalid registrations and improve security posture.

- Add regex pattern for email validation (RFC-compliant format)
- Require 8+ chars with uppercase, lowercase, and digit for passwords
- Add username length bounds (3-20) and alphanumeric pattern
- Add null/type checking to prevent runtime errors
- Collect all validation errors instead of failing on first
- Improve error messages with specific requirements
```

## Why This Format?

1. **Type `fix`**: The original validation was insecure (email only checked for `@`, password only required 6 chars). This is a security fix.

2. **Scope `validation`**: All changes are contained within the validation module.

3. **Imperative mood**: "strengthen", "replace", "add" - not past tense.

4. **Description under 50 chars**: "strengthen user input validation rules" = 40 chars

5. **Body explains WHY**: Focuses on the security improvement rationale, not just listing what changed.

6. **Bullet points for WHAT**: Lists the specific changes for easy scanning.
