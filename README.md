# Portfobit Plugin

Connect Grok Bot, Hermes, OpenClaw, ChatGPT/Codex, Claude, or Cursor to Portfobit with one plugin and five shared skills. Muse connects through a Remote MCP Custom Connector using the prompt below. Portfobit remains the source for account data, portfolio values, risk results, permissions, and protected actions.

## Install

| Where you use it | How to connect |
| --- | --- |
| Grok Bot | Paste the Grok Bot prompt below to install the plugin and complete browser OAuth. [Guide](docs/install/grok-bot.md) |
| Muse | Paste the Muse prompt below to configure a Remote MCP Custom Connector and complete browser OAuth. [Guide](https://docs.portfobit.com/guides/mcp/muse) |
| Hermes | Paste the Hermes prompt below to install and enable the plugin, then complete browser OAuth. [Guide](docs/install/hermes.md) |
| OpenClaw | Paste the OpenClaw prompt below to install the plugin and complete browser OAuth. [Guide](docs/install/openclaw.md) |
| ChatGPT Desktop (Chat or Codex mode) and Codex CLI | Paste the Codex prompt below. Install once to use it in all of them. [Guide](docs/install/codex.md) |
| Claude Code and Claude Desktop Code mode | Paste the Claude Code prompt below. [Guide](docs/install/claude-code.md) |
| Claude Desktop Chat/Cowork mode | Install manually from **Customize → Plugins**: add this repository as a marketplace, install Portfobit, then connect `portfobit` from the plugin's **Connectors** tab. [Guide](docs/install/claude-desktop.md) |
| Cursor editor and Cursor CLI | Paste the Cursor prompt below into the Cursor Agent chat, or add this repository from **Customize → From GitHub Repository**. [Guide](docs/install/cursor.md) |

Grok Bot:

```text
Set up Portfobit in Grok Bot using https://docs.portfobit.com/guides/mcp/grok-bot. Prefer the plugin from https://github.com/portfobit/portfobit-plugin; otherwise use Remote MCP. Guide me through signing in to https://portfobit.com and browser OAuth with the permissions I choose, then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account. Explain the credential-entry options before asking for exchange keys.
```

Muse:

```text
Connect Muse to Portfobit using https://docs.portfobit.com/guides/mcp/muse. Configure a Remote MCP connector with browser OAuth. Guide me through signing in to https://portfobit.com and browser OAuth with the permissions I choose, then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account. Explain the credential-entry options before asking for exchange keys.
```

Hermes:

```text
Install and enable the Portfobit plugin in Hermes from https://github.com/portfobit/portfobit-plugin, following https://docs.portfobit.com/guides/mcp/hermes. Use its shared skills and Remote MCP connection, guide me through browser authorization and permissions, then verify the connection with a read-only account query. Preserve existing MCP settings and never request credentials in chat. Then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account.
```

OpenClaw:

```text
Install the Portfobit plugin in OpenClaw from https://github.com/portfobit/portfobit-plugin, following https://docs.portfobit.com/guides/mcp/openclaw. Use its compatible skills and Remote MCP connection, guide me through browser authorization and permissions, then verify the connection with a read-only account query. Preserve existing MCP settings and never request credentials in chat. Then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account.
```

ChatGPT or Codex:

```text
Install the Portfobit plugin from https://github.com/portfobit/portfobit-plugin using the Codex plugin marketplace, then guide me through Portfobit browser OAuth. Then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account.
```

Claude Code or Claude Desktop Code mode:

```text
Install the Portfobit plugin from https://github.com/portfobit/portfobit-plugin using the Claude Code plugin marketplace, then guide me through Portfobit browser OAuth. Then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account.
```

Cursor:

```text
Install the Portfobit plugin from https://github.com/portfobit/portfobit-plugin using the Cursor plugin marketplace, then guide me through Portfobit browser OAuth. Then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account.
```

Sign in to Portfobit in your browser when asked. On the OAuth authorization page, choose the access you need and approve the connection. Manual Remote MCP setup without the plugin is in the [Portfobit docs](https://docs.portfobit.com/guides/mcp-server-setup).

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

Interactive MCP access uses browser OAuth. Grant only the scopes needed for the task; `activity:write`, `trade:write`, and `transfer:write` are separate choices and are not presumed. A skill cannot bypass server-side authorization or plan limits. No token, API key, exchange credential or trading OTP belongs in this package. Keep OAuth tokens and trading OTPs out of chat. For account creation, explain the [MCP and website credential-entry choices](https://docs.portfobit.com/guides/connect-your-first-account) before collecting exchange keys; website entry provides stronger isolation from the model and host.

## Package layout

- `plugin.json` and `mcp.json`: portable identity, discovery, Streamable HTTP connection, and a Hermes-specific `untrusted` MCP declaration.
- `skills/`: one shared set of English workflow instructions.
- `.agents/plugins/marketplace.json`: Codex marketplace entry.
- `.claude-plugin/` and `.mcp.json`: Claude Code marketplace, manifest, and MCP adapter.
- `.cursor-plugin/`: Cursor marketplace and manifest; Cursor reads `.cursor-plugin/marketplace.json` to find the plugin when installing from a GitHub repository.
- `docs/install/`: installation guides for [Grok Bot](docs/install/grok-bot.md), [Hermes](docs/install/hermes.md), [OpenClaw](docs/install/openclaw.md), [ChatGPT and Codex](docs/install/codex.md), [Claude Code](docs/install/claude-code.md), [Claude Desktop](docs/install/claude-desktop.md), and [Cursor](docs/install/cursor.md), including uninstall and local development steps. The [Muse guide](https://docs.portfobit.com/guides/mcp/muse) covers Remote MCP setup.
- `tests/`: self-contained package checks and host validation scenarios.

The source repository is [`portfobit/portfobit-plugin`](https://github.com/portfobit/portfobit-plugin). Installation steps are in the guides above. Manual Remote MCP setup remains available in the [Portfobit docs](https://docs.portfobit.com).

See [AGENTS.md](AGENTS.md) for contributor guidance. Licensed under [MIT](LICENSE).
