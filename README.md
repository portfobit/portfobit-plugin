# Portfobit Plugin

An Agent Plugins 1.0 package for Portfobit's existing Remote MCP server, with Codex and Claude Code adapters and five shared skills. Portfobit remains the source for account data, portfolio values, risk results, permissions, and protected actions.

## What the MCP connection exposes

The current server contract includes current account and portfolio balances, positions, allocation, and risk; live open orders; terminal order history, trades, ledger entries, and exchange deposits/withdrawals; and daily account/portfolio NAV history. `list_account_valuation_history` and `list_portfolio_valuation_history` answer standalone historical valuation questions directly. `get_market_quote` and `list_market_candles` query a connected exchange directly. NAV changes are not spot profit and loss or investment returns, and raw exchange quotes/candles are not Portfobit's internal portfolio valuation prices.

Users can also query available connectors (`list_account_connectors`), service egress IPs (`list_service_egress_ips`), and the current plan and granted scopes (`get_current_user_context`). The MCP catalog includes explicitly requested account connection, tag, and sync tools, plus portfolio create/update/bind tools; this package does not provide guided skills for those writes. Account deletion is handled in the Web app. The plugin cannot withdraw assets, transfer to an external address, move funds across exchanges, or use P2P.

The five skills add task guidance, not another data source or permission layer:

| Skill | Guided task |
| --- | --- |
| `portfolio-overview` | Current portfolio/account assets, source freshness, and server risk. |
| `cex-activity-history` | Stored CEX activity and gap explanation; a bounded import only on explicit request. |
| `account-diagnostics` | Account connection, permissions, current snapshot sync, and missing portfolio source diagnosis. |
| `protected-cex-actions` | Guidance for five protected CEX actions, including exact parameters, explicit confirmation, and trading-OTP requirements. |
| `support-issue-reporting` | A concise, sanitized issue; submit only when explicitly requested. |

Interactive MCP access uses browser OAuth. Grant only the scopes needed for the task; `activity:write`, `trade:write`, and `transfer:write` are separate choices and are not presumed. A skill cannot bypass server-side authorization or plan limits. No token, API key, exchange credential, or trading OTP belongs in this package or a chat transcript.

## Package layout

- `plugin.json` and `mcp.json`: portable identity, discovery, and Streamable HTTP connection.
- `skills/`: one shared set of English workflow instructions.
- `.agents/plugins/marketplace.json`: Codex marketplace entry.
- `.claude-plugin/` and `.mcp.json`: Claude Code marketplace, manifest, and MCP adapter.
- `docs/install/`: local checkout instructions for [Codex](docs/install/codex.md) and [Claude Code](docs/install/claude-code.md).
- `tests/`: self-contained package checks and host validation scenarios.

The source repository is [`portfobit/portfobit-plugin`](https://github.com/portfobit/portfobit-plugin). Local installation steps are in the guides above. Manual Remote MCP setup remains available in the [Portfobit docs](https://docs.portfobit.com).

See [AGENTS.md](AGENTS.md) for contributor guidance. Licensed under [MIT](LICENSE).
