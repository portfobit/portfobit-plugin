#!/usr/bin/env python3
"""Check the distributable package without reading sibling repositories."""

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "portfolio-overview",
    "cex-activity-history",
    "account-diagnostics",
    "protected-cex-actions",
    "support-issue-reporting",
}
MCP_URL = "https://mcp.portfobit.com/v1/mcp"


def load(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    portable = load("plugin.json")
    portable_mcp = load("mcp.json")
    claude = load(".claude-plugin/plugin.json")
    claude_mcp = load(".mcp.json")
    codex_market = load(".agents/plugins/marketplace.json")
    claude_market = load(".claude-plugin/marketplace.json")
    contract = load("tests/contract-tools.json")
    routing_cases = json.loads((ROOT / "tests/offline-routing-cases.json").read_text(encoding="utf-8"))

    check(portable["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "portable schema")
    check(portable_mcp["$schema"] == "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json", "MCP schema")
    check(set(portable_mcp) == {"$schema", "mcpServers"}, "unexpected portable MCP fields")
    check(portable["name"] == claude["name"] == "portfobit", "plugin names differ")
    check(portable["version"] == claude["version"] == claude_market["plugins"][0]["version"], "versions differ")
    check(re.fullmatch(r"\d+\.\d+\.\d+", portable["version"]) is not None, "version is not semver")
    check(portable["description"] == claude["description"], "host descriptions differ")
    check(len(portable["extensions"]["com.openai"]["interface"]["shortDescription"]) <= 30, "listing subtitle too long")
    check(portable_mcp["mcpServers"] == {"portfobit": {"type": "streamable-http", "url": MCP_URL}}, "portable MCP mismatch")
    check(claude_mcp["mcpServers"] == {"portfobit": {"type": "http", "url": MCP_URL}}, "Claude MCP mismatch")
    check(codex_market["plugins"][0]["name"] == claude_market["plugins"][0]["name"] == "portfobit", "marketplace names differ")
    check(codex_market["plugins"][0]["source"] == {"source": "local", "path": "./"}, "Codex source must be repo root")
    check(claude_market["plugins"][0]["source"] == "./", "Claude source must be repo root")

    skill_dirs = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    check(skill_dirs == SKILLS, f"unexpected skill set: {skill_dirs ^ SKILLS}")
    tool_names = set(contract["tools"])
    check(len(tool_names) == len(contract["tools"]) == 42, "contract snapshot needs 42 unique tools")
    check(len(routing_cases) >= 10 and len({case["id"] for case in routing_cases}) == len(routing_cases), "routing cases need unique IDs")
    check(all(case["expected_skill"] in SKILLS | {None} for case in routing_cases), "routing case references unknown skill")
    for directory in sorted(SKILLS):
        path = ROOT / "skills" / directory / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\nname: ([a-z-]+)\ndescription: ([^\n]+)\n---\n", text)
        check(match is not None and match.group(1) == directory, f"skill frontmatter: {directory}")
        check(len(match.group(2)) >= 40, f"skill description too short: {directory}")
        referenced = set(re.findall(r"`([a-z]+(?:_[a-z]+)+)`", text))
        unknown = {name for name in referenced if name.startswith(("get_", "list_", "start_", "place_", "cancel_", "amend_", "submit_")) and name not in tool_names}
        check(not unknown, f"unknown MCP tools in {directory}: {sorted(unknown)}")

    package_files = [p for p in ROOT.rglob("*") if p.is_file() and p != Path(__file__) and ".git" not in p.parts and p.suffix in {".md", ".json", ".py"}]
    for path in package_files:
        text = path.read_text(encoding="utf-8")
        check("/Volumes/utmp/git/pfb" not in text, f"workspace path in {path}")
        check("../product-spec" not in text and "../portfobit-server" not in text, f"sibling dependency in {path}")
        check(not re.search(r"(?i)(?:sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})", text), f"possible credential in {path}")

    print("Package structure, adapter parity, contract references, and source hygiene passed.")


if __name__ == "__main__":
    main()
