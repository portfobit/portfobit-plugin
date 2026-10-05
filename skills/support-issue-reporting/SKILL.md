---
name: support-issue-reporting
description: Prepare a concise, sanitized Portfobit support issue about account, venue, portfolio, activity-history, import, connection, or plugin data; call submit_support_problem only when the user explicitly asks to send it. For diagnosis or draft-only requests, do not submit.
---

# Support issue reporting

Use this workflow when the user explicitly asks to report a Portfobit problem, or asks for a report draft. Diagnosis alone never authorizes submission. A clear request to send the described issue already grants permission for that minimal report; do not ask for redundant approval. A request for a draft gets a draft only.

## Gather minimum relevant evidence

Use only already authorized read tools and only facts needed for the issue. For account balance or position coverage, include the actual venue, `account_id`, asset/contract, `asset_location` or missing field path, relevant sync time, and request ID if known. For a portfolio value, include `portfolio_id` (or `global`), filters, `base_currency`, `data_as_of` / `price_as_of`, warnings, and known affected account IDs. For activity or import, include `account_id`, type, symbol, UTC interval, missing/incorrect field, and known `ahi_*` status or error code. For connection or plugin issues, include the host/plugin version and a sanitized reproducible error. Check filters, pagination, freshness, and exclusions before stating a record is missing.

Separate Portfobit observations from the user's expected result or exchange-screen report. Mark user-supplied identifiers and claims as unverified if the MCP grant lacks the needed read scope; do not bypass authorization, start sync/import, or gather full holdings to fill a template. A likely cause remains a hypothesis until supported. If the question itself needs investigation, use `account-diagnostics`, `portfolio-overview`, or `cex-activity-history` as appropriate before writing the report.

## Compose and send

`submit_support_problem` accepts a required `problem` string of 10 to 5000 characters and optional `full_name`, `email`, and `phone_number`. Put venue, IDs, dates, and error codes inside a short Markdown `problem`; do not invent structured fields or attachments. A useful shape is:

```markdown
**Problem:** [one-sentence symptom]
- Scope: venue=...; account_id=...; asset_location=...; UTC interval=...
- Observed: [returned field or sanitized error; request_id if known]
- Expected (user reported): [user's expectation, marked as reported]
- Reproduce: [minimal safe steps]
```

Omit irrelevant lines. Never include exchange credentials, OAuth or API tokens, trading OTP, raw provider payloads, full positions/order history, log dumps, or unnecessary exact balances. Only pass contact details that the user explicitly supplied for this report. A connected MCP submission needs a valid MCP credential but no extra business scope, paid plan, or trading OTP. The separate direct Open API keeps its existing anonymous submission path, which requires an email; this skill does not alter that API or human submissions.

Show the final sanitized Markdown as part of the response. If the user asked to send and the content remains within that request, call `submit_support_problem` once. Report only the actual returned `data.id`, `status`, and `expected_response`; do not invent an SLA or a ticket-status lookup. If the call times out with unknown acceptance, do not resend automatically: preserve the draft and explain the uncertainty. On `problem_rate_limited`, report the limit without changing identity or retrying. On invalid/oversize payload, repair the draft before any user-directed retry. If MCP authentication itself is unavailable, offer the sanitized draft for the official support path; never claim a successful submission. If a receipt already exists in this conversation, show it before creating another report and submit another only on an explicit new request.
