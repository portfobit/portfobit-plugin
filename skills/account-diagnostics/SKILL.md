---
name: account-diagnostics
description: Investigate a Portfobit account connection, permission check, current snapshot sync, or missing portfolio source. Use for why current account or portfolio data has not updated; do not use for CEX activity-history collection or import, and never start a sync from diagnosis alone.
---

# Account and current-snapshot diagnostics

Investigate with read-only MCP tools and actual returned facts. Never request or echo an exchange API key, secret, OAuth token, or one-time code. Check `get_current_user_context` for grant and plan context when useful, but respect each tool's actual error.

## Investigate

1. Resolve the exact account and venue with `list_accounts` / `get_account` under `account:read`. Check account status, last sync timestamps, permission-check coverage, requested permissions, and any reported warning or error. `partially_verified`, `unverified`, and `check_failed` are different states. One upstream failure or a stale timestamp alone does not prove an invalid credential.
2. If the user has a known `sync_id`, call `get_sync` and distinguish queued, running, complete, and failed outcomes. There is no current tool to list every sync task for an account; do not invent one or infer a task result without its ID.
3. For a missing portfolio source, inspect `get_portfolio` bindings, `get_portfolio_summary` filters, included/excluded counts, plan limits, account status, and warnings. Portfolio tag lookup and temporary account-tag filtering have different meanings. Use `list_account_connectors` for supported venues and `list_service_egress_ips` when an exchange IP whitelist may matter.
4. Explain what is observed, what remains unknown, and the concrete Web or exchange step the user can take. Recognize scope denial, plan restriction, read permission rejection, whitelist errors, connector coverage, rate limits, and upstream unavailability without guessing an exact root cause.

## Sync and plan facts

Current account snapshots come from account-level SyncRuns. The default scheduled task creation interval is 24 hours per account on Free and 8 hours on active Plus, subject to eligibility and operational delays. These are trigger intervals, not completion deadlines or freshness guarantees. The current portfolio is aggregated on request from available account snapshots, definitions, prices, and FX; it has no separate current-portfolio SyncRun clock. A `plan_limited` account may still have sync behavior, while access to its data can be restricted by plan rules.

`start_account_sync` and `start_accounts_sync` are separate explicit write tools requiring `account:write`; this diagnostic skill does not call them. The server currently limits manually started SyncRuns to 20 per user per UTC day. If the user explicitly requests a sync, handle that as a separate operation under the actual MCP contract, never as a side effect of diagnosis.

For CEX orders, trades, ledger, or transactions, use `cex-activity-history`. Its collection cadence and eligibility are independent of account SyncRuns. If the user only asks "how often does it sync?", first determine whether they mean the current account snapshot or CEX activity history.
