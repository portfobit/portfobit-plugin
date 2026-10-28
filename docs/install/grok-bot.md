# Install in Grok Bot

## Recommended: Install the Portfobit plugin

Paste this into Grok Bot:

```text
Set up Portfobit in Grok Bot using https://docs.portfobit.com/guides/mcp/grok-bot. Prefer the plugin from https://github.com/portfobit/portfobit-plugin; otherwise use Remote MCP. Guide me through signing in to https://portfobit.com and browser OAuth with the permissions I choose, then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account. Explain the credential-entry options before asking for exchange keys.
```

This repository includes Cursor-compatible plugin metadata. Let Grok Bot inspect it and use its supported GitHub plugin workflow. If plugin import is unavailable in your version or workspace, use custom Remote HTTPS MCP at `https://mcp.portfobit.com/v1/mcp` instead; do not invent a Grok Bot marketplace command.

## Continue setup

1. Sign in to [Portfobit](https://portfobit.com), then start the plugin or MCP connection in Grok Bot.
2. Complete browser OAuth and let the user choose access on the authorization page. This flow does not require a Portfobit Developer API Key.
3. Follow [Connect Your First Account](https://docs.portfobit.com/guides/connect-your-first-account). Explain MCP credential visibility and website entry, help create the exchange API key, then complete the account connection and check its first sync.

[Full Grok Bot setup guide](https://docs.portfobit.com/guides/mcp/grok-bot)
