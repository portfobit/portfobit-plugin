# Contributor guidance

Read `README.md` before changing this repository. Keep the published plugin package self-contained: its code, tests, build, and release process must not read sibling repositories through local paths.

Write this public repository's README, skills, installation guides, examples, release notes, and contributor documentation in English.

- Use Portfobit's published MCP and API contracts for tool names, scopes, response fields, and errors. Verify the live connection before claiming that an agent is supported.
- Interactive users connect through Remote MCP OAuth. Never include real API keys, OAuth tokens, exchange credentials, one-time codes, or account data in source, examples, logs, or release archives.
- Keep live data, valuation, risk rules, authorization, trading, and audit enforcement on the Portfobit server. Do not add withdrawal, external-transfer, cross-exchange-transfer, or P2P actions.
- Preserve server-provided freshness, warnings, currency, decimal-string values, and risk conclusions. Do not call valuation changes realized profit and loss.
- Test Codex and Claude Code independently for installation, OAuth, scope denial, refresh, revocation, and protected-action safety before announcing support.
- Check `git status` before edits and preserve unrelated changes. Commit only when requested.
