# Install in OpenClaw

## Recommended: Install the Portfobit plugin

Paste this into OpenClaw:

```text
Install the Portfobit plugin in OpenClaw from https://github.com/portfobit/portfobit-plugin, following https://docs.portfobit.com/guides/mcp/openclaw. Use its compatible skills and Remote MCP connection, guide me through browser authorization and permissions, then verify the connection with a read-only account query. Preserve existing MCP settings and never request credentials in chat. Then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account.
```

Use an OpenClaw release with compatible plugin-bundle and HTTP MCP support. Install this repository through its compatible bundle installer. Inspect the detected format and confirm the five shared Skills and one remote MCP server are enabled; not every native OpenClaw plugin feature maps from a bundle. This repository retains its Agent Plugins, Cursor and Claude metadata.

If a same-name MCP server was already configured manually, inspect the conflict before removing or replacing it.

## Sign in and check

Sign in to Portfobit in your browser. On the OAuth authorization page, choose the access you need and approve the connection. Ask **“Use portfobit to list the account connectors I can connect.”** and then query your connected accounts. Installation does not by itself grant access.

Never put API keys, exchange credentials, OAuth tokens or trading OTPs in chat or plugin files.

## Disconnect

Disable or remove Portfobit using the host's plugin management controls. Revoke its grant in **Portfobit → Authorized Agents** when access is no longer needed. Removing a plugin alone does not revoke authorization.

[Portfobit host guide](https://docs.portfobit.com/guides/mcp/openclaw)
