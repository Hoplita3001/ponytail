---
name: skillspector
description: Scan an agent skill, plugin or MCP server for security risks with NVIDIA SkillSpector before installing or enabling it. Use when the user asks whether a skill or plugin is safe, asks to install a skill, plugin or MCP server from GitHub or a URL, or adds a new folder under .claude/skills.
---

# SkillSpector security scan

Run NVIDIA SkillSpector (https://github.com/NVIDIA/SkillSpector, Apache-2.0) on a skill before it is installed.

## 1. Make sure the CLI is installed

```bash
command -v skillspector >/dev/null 2>&1 || uv tool install -q git+https://github.com/NVIDIA/skillspector.git
```

If `uv` is missing, use `pipx install git+https://github.com/NVIDIA/skillspector.git`.

## 2. Scan

Target can be a local folder, a `SKILL.md` file, a `.zip`, or a GitHub URL.

```bash
skillspector scan <target> --no-llm --format json --output /tmp/skillspector-report.json
skillspector scan <target> --no-llm            # human-readable report
skillspector scan <folder-of-skills> --recursive --no-llm
```

Use `--no-llm` unless the user has set `SKILLSPECTOR_PROVIDER` and a matching key (for example `SKILLSPECTOR_PROVIDER=anthropic` with `ANTHROPIC_API_KEY`). Never ask the user to paste a key into chat.

## 3. Report to the user

- Give the score, severity and recommendation from `risk_assessment`.
- A static-only scan (`--no-llm`) flags many patterns that are normal in large, legitimate skills (shell scripts, `subprocess`, env access, `rm` of temp files). For each HIGH or CRITICAL finding, open the file and line it points to and say whether it is a real risk or a false positive.
- Call out real red flags plainly: sending data or credentials to unknown hosts, downloading and executing code, reading browser cookies or SSH keys, hidden instructions that override the user.
- Do not install the skill until the user agrees after seeing the result.
