# Install in Cursor

Use this guide for the Cursor editor and the Cursor CLI (`agent`). Cursor finds the plugin through this repository's `.cursor-plugin/marketplace.json`.

## Recommended: Install the Portfobit plugin

Paste this into the Cursor Agent chat:

```text
Install the Portfobit plugin from https://github.com/portfobit/portfobit-plugin using the Cursor plugin marketplace, then guide me through Portfobit browser OAuth. Then help me connect my first exchange account using https://docs.portfobit.com/guides/connect-your-first-account.
```

Or install from GitHub: open **Customize** in the Cursor sidebar, choose **From GitHub Repository**, enter `https://github.com/portfobit/portfobit-plugin`, then install Portfobit.

The plugin adds five skills and one Portfobit HTTP MCP connection.

## Sign in

- In the Cursor editor, open the MCP settings and connect `portfobit`.
- In the Cursor CLI, start `agent`, run `/mcp`, and select Portfobit. The plugin's MCP server appears there as `plugin-portfobit-portfobit`; it is not available to `agent mcp login`, which only reads `mcp.json`.

Sign in to Portfobit in the browser and choose only the scopes needed for the task. `activity:write`, `trade:write`, and `transfer:write` are separate choices and are not needed for read-only use.

Then ask: **"Use portfobit to list the account connectors I can connect."**

For manual Remote MCP setup without the plugin, see the [Portfobit docs](https://docs.portfobit.com/guides/mcp/cursor).

## Safety

Do not enter an API key, exchange secret, OAuth token, or trading OTP into a plugin file or ordinary chat. The protected CEX workflow cannot execute until a private one-time trading-OTP input path has been validated in this host.

If Portfobit MCP was also added manually in `mcp.json`, the two connections may show duplicate tools. Remove only the connection you no longer intend to use; plugin installation does not revoke an existing OAuth grant or API key.

## Uninstall

Open **Customize** in the Cursor sidebar, find Portfobit among your plugins, and uninstall it.

Uninstalling does not revoke the OAuth grant. Revoke it in the Portfobit Web app if you no longer need it.
