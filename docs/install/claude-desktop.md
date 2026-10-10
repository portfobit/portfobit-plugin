# Install in Claude Desktop

Claude Desktop supports the Portfobit plugin in all of its modes. How you install it depends on the mode:

| Mode | Installation |
| --- | --- |
| Code | Ask Claude to install the plugin with a prompt. |
| Chat/Cowork | Install the plugin manually. Chat/Cowork mode cannot install plugins from a prompt. |

## Code mode: install with a prompt

Code mode runs Claude Code, so it uses the same prompt as [Claude Code](claude-code.md).

1. Start a session in Code mode and paste:

```text
Install the Portfobit plugin from https://github.com/portfobit/portfobit-plugin using the Claude Code plugin marketplace, then guide me through Portfobit browser OAuth.
```

2. When Claude asks you to authorize, enter `/mcp`, select `portfobit`, and sign in to Portfobit in the browser. Choose only the scopes needed for the task.
3. Start a new session in Code mode so the plugin and its connector load.
4. Ask: **"Use portfobit to list the account connectors I can connect."**

## Chat/Cowork mode: install manually

1. Open **Customize** from the Claude Desktop sidebar, then choose **Plugins**.
2. Select **Add marketplace** and enter `https://github.com/portfobit/portfobit-plugin`.
3. Select **Portfobit** from the plugin list, then select **Install**.

Installing the plugin does not sign in to the connector. Connect it separately:

4. Open the Portfobit plugin and go to its **Connectors** tab.
5. Connect `portfobit`. Your browser opens the Portfobit authorization page; choose only the scopes needed for the task.
6. After authorization, you return to Claude and the connector shows as connected.
7. Ask: **"Use portfobit to list the account connectors I can connect."**

In either mode, the expected plugin is `portfobit`, with five skills and one Portfobit connector. `activity:write`, `trade:write`, and `transfer:write` are separate scope choices and are not needed for read-only use.

## Safety

Do not enter an API key, exchange secret, OAuth token, or trading OTP into a plugin file or ordinary chat. The protected CEX workflow cannot execute until a private one-time trading-OTP input path has been validated in this host.

If Portfobit MCP was also added as a separate connector, the two connections may show duplicate tools. Remove only the connection you no longer intend to use; plugin removal does not revoke an existing OAuth grant or API key.

## Uninstall

- Code mode: use the uninstall commands in [Claude Code](claude-code.md#uninstall).
- Chat/Cowork mode: uninstall Portfobit and remove its marketplace from **Customize → Plugins**.

Uninstalling does not revoke the OAuth grant. Revoke it in the Portfobit Web app if you no longer need it.
