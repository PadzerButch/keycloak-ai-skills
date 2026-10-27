# Keycloak AI Skills

Reusable AI skills for working with Keycloak.

| Skill | Purpose |
| --- | --- |
| [add-skill](skills/add-skill/SKILL.md) | Turn a task description into a reusable skill. |
| [triage-cve](skills/triage-cve/SKILL.md) | Analyze an issue, check duplicates, classify security impact, assess CVSS, and draft a report and comment. |

The shared instructions follow [Agent Skills](https://agentskills.io/specification). The root `plugin.json` follows [Agent Plugins 1.0](https://agent-plugins.org/specification). Small client integrations all use the same `skills/` directory.

## Install

Publish this repository before using these GitHub installation commands. Use a current client with plugin or extension support.

Codex:

```bash
codex plugin marketplace add lhanusov/keycloak-ai-skills
codex plugin add keycloak-ai-skills@keycloak-skills
```

Claude Code:

```bash
claude plugin marketplace add lhanusov/keycloak-ai-skills
claude plugin install keycloak-ai-skills@keycloak-skills
```

GitHub Copilot CLI:

```bash
copilot plugin marketplace add lhanusov/keycloak-ai-skills
copilot plugin install keycloak-ai-skills@keycloak-skills
```

Gemini CLI:

```bash
gemini extensions install https://github.com/lhanusov/keycloak-ai-skills
```

IBM Bob Shell:

```bash
bob extensions install https://github.com/lhanusov/keycloak-ai-skills
```

Bob Shell uses an extension context file to find the shared skill. Bob IDE has separate [skill discovery](https://bob.ibm.com/docs/ide/features/skills); the Shell command does not install an IDE plugin. Other Agent Skills clients can use the same skill folder through their own installer.

## Use

Start a new session after installation and ask:

```text
Use add-skill to create a skill for reviewing Keycloak configuration.
```

In Claude Code, use `/keycloak-ai-skills:add-skill`. In Codex, use `$add-skill`. For discovery paths and activation details, see [client support](skills/add-skill/references/client-support.md). Verified versions and limitations are recorded in [compatibility checks](docs/compatibility.md).

New collection skills go in `skills/`. Standalone skills go in the target tool's discovery directory; `add-skill` identifies that tool before choosing a path.

To triage a specific issue, provide its URL, tracker-qualified ID, or text:

```text
Use triage-cve to analyze <issue-url>, check for duplicates, and draft a report and short comment.
```

The skill drafts its findings without posting them. New collection skills become available after the updated plugin is released and installed; start a new session after updating. Structural validation does not verify client discovery or invocation.

## Maintain

Keep shared metadata in `plugin.json` and instructions in `skills/`. The Codex catalog is `.agents/plugins/marketplace.json`; Claude and Copilot share `.claude-plugin/marketplace.json`. Claude, Gemini, and Bob Shell have small compatibility manifests. `BOB.md` routes Bob Shell to the shared skill without duplicating its instructions.

When releasing, update the version in `plugin.json` and the compatibility manifests. Checks reject mismatched metadata and catalogs. There is no metadata generator.

With Python 3.10+:

```bash
python -m pip install -r requirements-dev.txt
python scripts/check-package.py
python -m unittest discover -s tests -v
```

CI runs these checks on Linux and Windows with Python 3.10 and 3.14. The validator checks containment, relative symlinks, bounded YAML without aliases, and CommonMark links outside code examples. Scaffold markers use `@@ADD_SKILL_...@@` and are checked in UTF-8 resources outside `assets/`, with a 1 MiB limit per checked file. Structural checks do not prove client activation.

## Publish

```bash
git status --short
git add -A
git diff --cached --stat
git commit -m "Publish Keycloak AI skills collection"
git push -u origin main
```

## License

[Apache License 2.0](LICENSE.txt).
