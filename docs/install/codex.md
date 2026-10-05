# Codex local development install

This is a pre-release checkout workflow. It confirms that Codex can load the package from a local marketplace; it does not establish that the public MCP service or OAuth is available.

From the cloned `portfobit-plugin` directory:

```sh
codex plugin marketplace add .
codex plugin add portfobit@portfobit
codex plugin list --marketplace portfobit
```

The expected plugin identity is `portfobit@portfobit`, with five skills and one Portfobit Streamable HTTP MCP connection. When a reachable Portfobit MCP environment is available, use Codex's MCP OAuth login for the `portfobit` server and choose only the scopes needed for the task. A local package install alone does not prove OAuth or account access.

Do not enter an API key, exchange secret, OAuth token, or trading OTP into a plugin file or ordinary chat. The protected CEX workflow cannot execute until a private one-time trading-OTP input path has been validated in this host.

To remove the local validation install:

```sh
codex plugin remove portfobit@portfobit
codex plugin marketplace remove portfobit
```

If Portfobit MCP was also added manually, the two connections may show duplicate tools. Remove only the connection you no longer intend to use; plugin installation does not revoke an existing OAuth grant or API key.
