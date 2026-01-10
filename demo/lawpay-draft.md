# Draft: LawPay Improvements

**Title:** LawPay - Improve Error messaging and event processing logic and logs

**Description:** Some of the following improvements were identified in LawPay integration:

- Improve error messaging to be user-friendly.
- Improve Logic for Event Processing that fails to fetch the correct tenant at first in non-prod environment due to all accounts using the same sandbox merchantAccountID
- Fix the incorrect tenant being reported in OutSystems logs as a result of the problem in the above point.
