# Offline skill-routing evaluation

**Date:** 2026-10-03

**Package:** local `0.1.0` skill text

**Codex CLI:** `0.154.0`

**Claude Code:** `2.1.132` (package and Marketplace install); `2.1.286` (model routing, 2026-10-09)

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

**Claude result (2026-10-09):** Claude Code `2.1.286`, signed in, default model `claude-opus-5-5`. Each case ran as a separate print-mode session from an empty working directory with `--plugin-dir` pointing at the isolated `portfobit-eval` copy, `--strict-mcp-config` with no MCP configuration, `--setting-sources local`, tools limited to `Skill`, `Read`, `Glob`, and `Grep`, and `--no-session-persistence`. The initialization event listed no MCP servers and exactly the five `portfobit-eval:*` skills. Routing was judged from the `Skill` tool calls in each stream-json trace, not from answer text.

All ten English cases above and the same seven Chinese synthetic requests matched: **17/17**. Each positive case loaded only its expected skill; the quote, NAV, and withdrawal cases loaded no skill. No account, import, order, transfer, or support tool existed or was called. The submission cases reported that nothing was sent and returned a sanitized draft. The order case asked for the missing parameters without requesting an OTP. The withdrawal case explained that the action is unsupported. The only other tool calls were empty `Glob` lookups in the empty working directory.

Like the Codex run, this checks skill discovery and selection in an offline fixture. It does not check MCP tool selection, server authorization, OAuth, data semantics, or real writes, which remain in the [host acceptance checklist](host-validation.md).
