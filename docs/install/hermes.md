# Install in Hermes

## Recommended: Install the Portfobit plugin

Paste this into Hermes:

```text
Install and enable the Portfobit plugin in Hermes from https://github.com/portfobit/portfobit-plugin, following https://docs.portfobit.com/guides/mcp/hermes. Use its shared skills and Remote MCP connection, guide me through browser authorization and permissions, then verify the connection with a read-only account query. Preserve existing MCP settings and never request credentials in chat. Then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account.
```

Install and enable the Portfobit plugin, then sign in to Portfobit in your browser. On the OAuth authorization page, choose the access you need and approve the connection.

Install and explicitly enable the package using the host confirmation flow, or:

```bash
hermes plugins install portfobit/portfobit-plugin --no-enable
hermes plugins list
hermes plugins enable portfobit
```

Start the next session so its five shared skills and one remote MCP connection load. Use Hermes' MCP connection controls to complete browser OAuth.

If you already configured Portfobit manually, keep a single connection to avoid duplicate tools.

## Sign in and check

Ask **“Use portfobit to list the account connectors I can connect.”** and then query your connected accounts. Installation does not by itself grant access.

Never put API keys, exchange credentials, OAuth tokens or trading OTPs in chat or plugin files.

## Disconnect

Disable or remove Portfobit using the host's plugin management controls. Revoke its grant in **Portfobit → Authorized Agents** when access is no longer needed. Removing a plugin alone does not revoke authorization.

[Portfobit host guide](https://docs.portfobit.com/guides/mcp/hermes)
