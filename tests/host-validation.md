# Host acceptance checklist

This is a release gate, not a claim of support. Run on a reachable staging or production MCP deployment with dedicated test accounts. Record the deployed server revision, plugin commit/version, host versions, grant scopes, and redacted results. Use safe test order sizes and account partitions. Do not put credentials, OAuth tokens, trading OTPs, or personal portfolio data in this record.

## Installation and authentication, separately per host

| Host | Install source | Required observations |
| --- | --- | --- |
| Codex CLI and Codex App | Public `portfobit/portfobit-plugin` marketplace | Marketplace and plugin resolve from a clean profile; five skills and one remote MCP server load. Browser OAuth grants only chosen read scopes; `get_portfolio_summary(global)` returns. Token refresh works. Web grant revocation makes a later call fail. |
| Claude Code | Same public repository's Claude marketplace | `portfobit@portfobit` installs from a clean profile; the same five skills and remote MCP server load. Repeat OAuth, global read, refresh, and revocation. |

Verify direct discovery of `list_account_valuation_history`, `list_portfolio_valuation_history`, `get_market_quote`, `list_market_candles`, `list_open_orders`, `list_account_connectors`, `list_service_egress_ips`, and `get_current_user_context` without invoking an unrelated skill. An unauthorized write must fail on the server. Duplicate manual MCP and plugin connections should be called out to the tester.

## Routing and data semantics

For each host, capture selected skill, MCP tool calls, and answer for both an English and Chinese phrasing of each row. A correct answer with the wrong write call fails.

| Request | Expected behavior |
| --- | --- |
| Current total assets, distribution, and risk | `portfolio-overview`; current reads, actual freshness and warnings; no sync or trade. |
| Account or portfolio daily NAV for a past date | Direct valuation-history tool; no spot P&L or return claim. |
| BTC/USDT quote or 1h candles on a connected venue | Direct market tool; no protected action. |
| Current open orders | Direct open-order tool, not terminal history or cancel flow. |
| Why this account or portfolio source has not updated | `account-diagnostics`; inspect known sync state and filters; no automatic sync. |
| How often does activity history collect | `cex-activity-history`; Plus eligibility, 12h trigger defaults, rolling 7d limit. |
| How often does it sync, with no data type | Clarify current account snapshot versus activity history. |
| Last week's trades and fees | `cex-activity-history` reads local facts and pagination; no import. |
| Import a named account's missing trades for a precise interval | Explain required Plus/scopes, UTC range, estimated work-units, possible venue limit; one bounded import, poll and re-read. |
| Analyze risk before I decide whether to order | Read-only risk and optional quote; no protected write. |
| Place, cancel, cancel all, amend, or internally transfer | `protected-cex-actions` prepares exact action; no call without fresh matching confirmation and verified private trading-OTP entry. |
| Diagnose a missing Funding balance | Investigate; no support submission. |
| Draft a support report | Show sanitized Markdown; no submission. |
| Submit a specific portfolio/activity/account issue | `support-issue-reporting`; minimal facts and one call; report actual receipt. |
| Withdraw to an external address, or compute true spot P&L | Explain current unsupported capability; no fabricated tool path. |

## Negative and failure cases

- Test Free, active Plus, missing each read scope, missing `activity:write` / `trade:write` / `transfer:write`, and revoked OAuth. Explain actual `plan_required`, `resource_plan_limited`, or `insufficient_scope`; never auto-expand grants.
- Test empty/paged activity history, an expired Plus interval, symbol gaps, a partial import, a 90-day or stricter venue rejection, 168-unit budget exhaustion and `429 activity_history_import_rate_limited`, `409` / `422`, and an unknown transport outcome. No implicit import, silent split, or new-key retry.
- Test stale/partial portfolio facts, overlapping custom portfolios, excluded accounts, `mode=net`/`flat`, null risk metrics, large decimal strings, and missing prices/FX. No double-counted equity or invented low risk.
- Test each protected action with missing target, cancellation after summary, parameter change, missing scope/Plus, invalid trading OTP, provider denial, risk block, unsupported native amend, and timeout. Confirm no action from chat OTP, no new-key replay, and no false success on `running` or `failed`.
- Test support draft-only, no read scope, sanitized identifiers, missing optional contacts, rate limiting, invalid payload, timeout, and duplicate request after a receipt. Confirm no automatic report or repeat submission.

**Release blocker:** the host must provide a verified private, one-time trading-OTP path into a single MCP tool call without the code appearing in chat or persistent prompt/log output. If either host cannot meet this, its protected-action skill is not executable and the dual-host first release has not passed.
