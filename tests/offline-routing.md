# Offline skill-routing evaluation

**Date:** 2026-10-03

**Package:** local `0.1.0` skill text

**Codex CLI:** `0.154.0`

**Claude Code:** `2.1.132`

This evaluation isolates skill discovery from account access. A temporary package copied the five `skills/*/SKILL.md` files, used a distinct `portfobit-eval` identity, and contained **no** `mcp.json`, `.mcp.json`, OAuth configuration, or account fixture. Codex ran with `--ignore-user-config`, `--sandbox read-only`, and an ephemeral session. The installed production plugin and marketplace were removed before testing. The prompts in [offline-routing-cases.json](offline-routing-cases.json) contain only synthetic requests.

Codex event traces were checked for reads of `skills/<name>/SKILL.md`. The model sometimes queried the generic plugin catalog, but it had no Portfobit MCP server in this fixture. No account, import, order, transfer, or support tool was called.

| Case | Expected skill | Observed skill | Result |
| --- | --- | --- | --- |
| Stale account balance | `account-diagnostics` | `account-diagnostics` | Pass |
| Current assets and risk | `portfolio-overview` | `portfolio-overview` | Pass |
| Missing trades, investigation only | `cex-activity-history` | `cex-activity-history` | Pass |
| Prepare a limit order | `protected-cex-actions` | `protected-cex-actions` | Pass; no action executed |
| Send a support issue | `support-issue-reporting` | `support-issue-reporting` | Pass; no submission tool available |
| Direct exchange quote | None | None | Pass |
| Direct historical NAV | None | None | Pass |
| Risk before deciding to trade | `portfolio-overview` | `portfolio-overview` | Pass; no protected action |
| External withdrawal | None | None | Pass; unsupported action explained |
| Support draft only | `support-issue-reporting` | `support-issue-reporting` | Pass; draft only |

Seven additional Chinese synthetic requests covered the five named workflows plus direct NAV and unsupported external withdrawal. They used the same isolated package and all seven selected the expected skill, or no skill for the two direct/unsupported requests. The Chinese phrasing and expected routing are recorded in the internal Chinese implementation spec. The public package keeps its authored instructions and test documentation in English.

**Codex result:** 17/17 English and Chinese routing expectations matched across the two isolated runs. This checks natural-language selection and the absence of protected tool access in an offline fixture. It does not check whether a connected host chooses the correct MCP tool, server authorization, OAuth, data semantics, or real writes.

**Claude result:** its package and local Marketplace installation validated earlier, and `--plugin-dir` exposed all five skills in the session initialization event. Model routing was left untested at the user's request: `claude auth status` returned `loggedIn: false`; a print-mode invocation returned `Not logged in`. Re-run the same corpus after local Claude Code sign-in. Do not place credentials in this repository or a test prompt.
