# Install in ChatGPT and Codex

Use this guide for ChatGPT Desktop (Chat or Codex mode) and Codex CLI. Install once: the plugin and its connector then appear in both ChatGPT Desktop modes and in Codex CLI.

## Install with a prompt

Paste this into ChatGPT Desktop, in Chat or Codex mode, or into Codex CLI:

```text
Install the Portfobit plugin from https://github.com/portfobit/portfobit-plugin using the Codex plugin marketplace, then guide me through Portfobit browser OAuth.
```

The expected plugin identity is `portfobit@portfobit`, with five skills and one Portfobit Streamable HTTP MCP connection.

## Sign in

When asked, sign in to Portfobit in the browser and choose only the scopes needed for the task. `activity:write`, `trade:write`, and `transfer:write` are separate choices and are not needed for read-only use.

Then ask: **"Use portfobit to list the account connectors I can connect."**

For manual Remote MCP setup without the plugin, see the [Portfobit docs](https://docs.portfobit.com/guides/mcp/codex).

## Safety

Do not enter an API key, exchange secret, OAuth token, or trading OTP into a plugin file or ordinary chat. The protected CEX workflow cannot execute until a private one-time trading-OTP input path has been validated in this host.

If Portfobit MCP was also added manually, the two connections may show duplicate tools. Remove only the connection you no longer intend to use; plugin installation does not revoke an existing OAuth grant or API key.

## Uninstall

```sh
codex plugin remove portfobit@portfobit
codex plugin marketplace remove portfobit
```

Uninstalling does not revoke the OAuth grant. Revoke it in the Portfobit Web app if you no longer need it.

## Local development install

To test an unpublished checkout, run from the cloned `portfobit-plugin` directory:

```sh
codex plugin marketplace add .
codex plugin add portfobit@portfobit
codex plugin list --marketplace portfobit
```

A local package install alone does not prove that the public MCP service, OAuth, or account access works. Remove it with the uninstall commands above.
