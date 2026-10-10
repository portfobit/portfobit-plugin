# Install in Claude Code

Use this guide for Claude Code. If you use Claude Desktop, see [Claude Desktop](claude-desktop.md), which covers both Code mode and Chat/Cowork mode.

## Install with a prompt

Paste this into Claude Code, or into a session in Claude Desktop Code mode:

```text
Install the Portfobit plugin from https://github.com/portfobit/portfobit-plugin using the Claude Code plugin marketplace, then guide me through Portfobit browser OAuth.
```

The expected plugin identity is `portfobit@portfobit`, with five skills and one Portfobit HTTP MCP connection.

## Sign in

When asked, enter `/mcp`, select `portfobit`, and sign in to Portfobit in the browser. Choose only the scopes needed for the task. `activity:write`, `trade:write`, and `transfer:write` are separate choices and are not needed for read-only use.

Start a new session so the plugin and its connector load, then ask: **"Use portfobit to list the account connectors I can connect."**

For manual Remote MCP setup without the plugin, see the [Portfobit docs](https://docs.portfobit.com/guides/mcp/claude-code).

## Safety

Do not enter an API key, exchange secret, OAuth token, or trading OTP into a plugin file or ordinary chat. The protected CEX workflow cannot execute until a private one-time trading-OTP input path has been validated in this host.

If Portfobit MCP was also added manually, the two connections may show duplicate tools. Remove only the connection you no longer intend to use; plugin installation does not revoke an existing OAuth grant or API key.

## Uninstall

```sh
claude plugin uninstall portfobit@portfobit
claude plugin marketplace remove portfobit
```

Uninstalling does not revoke the OAuth grant. Revoke it in the Portfobit Web app if you no longer need it.

## Local development install

To test an unpublished checkout, run from the cloned `portfobit-plugin` directory:

```sh
claude plugin validate .
claude plugin marketplace add ./
claude plugin install portfobit@portfobit
claude plugin list
```

A local package install alone does not prove that the public MCP service, OAuth, or account access works. Remove it with the uninstall commands above.
