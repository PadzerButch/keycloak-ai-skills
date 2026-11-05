# Contributing

## Repository layout

The instructions follow [Agent Skills](https://agentskills.io/specification), and `plugin.json` follows [Agent Plugins 1.0](https://agent-plugins.org/specification). All client integrations use the same `skills/` directory.

| Location | Purpose |
| --- | --- |
| `skills/<name>/` | Skill entrypoint and self-contained resources |
| `shared/` | Canonical evidence, security-handling, and duplicate-search guidance |
| `plugin.json` | Shared package metadata |
| `.agents/plugins/marketplace.json` | Codex marketplace catalog |
| `.claude-plugin/` | Claude and Copilot integration |
| `gemini-extension.json` | Gemini CLI integration |
| `bob-extension.json` and `BOB.md` | Bob Shell integration and routing |
| `tests/` | Structural tests and behavioral scenarios |

For user setup and discovery, see [installation](docs/installation.md).

## Add or change a skill

Follow [add-skill](skills/add-skill/SKILL.md). Keep each skill portable: runtime references must stay inside its own directory. Update the README skill table and `BOB.md` routing when adding a collection skill; no new plugin or manifest entry is needed.

For shared guidance, edit the canonical file in `shared/`. Register any new consumer in `CONSUMERS` in `scripts/sync-shared.py`, then refresh the packaged copies:

```bash
python scripts/sync-shared.py --write
```

Commit sources and generated copies together. CI rejects missing or stale copies. Users do not need to run synchronization when installing or using the skills.

## Validate

With Python 3.10+:

```bash
python -m pip install -r requirements-dev.txt
python scripts/sync-shared.py
python scripts/check-package.py
python -m unittest discover -s tests -v
```

CI runs these checks on Linux and Windows with Python 3.10 and 3.14. Checks cover metadata, resource links, containment, shared-reference synchronization, and standalone relocation. The skill validator also checks naming, bounded YAML without aliases, and unfinished scaffold markers in UTF-8 resources outside `assets/`, up to 1 MiB per file. Structural validation does not prove client activation or good decisions.

Use the [offline scenario guide](docs/skill-validation.md) when changing triage, implementation, or review decisions. Record actual execution and evidence gaps.

## Release

1. Set the same version in `plugin.json`, `.claude-plugin/plugin.json`, `gemini-extension.json`, and `bob-extension.json`. Keep their shared descriptions consistent and update the current-version sentence in `README.md`. Marketplace catalogs have no version field.
2. Run validation, commit the changes, and push them to the default branch.
3. Open **Actions → Release → Run workflow**, select the default branch, and enter the committed version as `X.Y.Z` without a `v` prefix.

The workflow verifies all four manifest versions and the README version, then runs the validation matrix. It archives the exact validated commit as `keycloak-ai-skills-X.Y.Z.tar.gz`, generates a `.tar.gz.sha256` checksum, and uploads both as workflow artifacts and GitHub Release assets. The archive contains the committed repository under `keycloak-ai-skills-X.Y.Z/`, including hidden client integrations. The release tags the same commit as `vX.Y.Z` and includes generated notes.

The workflow uses the built-in `GITHUB_TOKEN`; no additional release secret is required. Repository rules must allow it to create release tags. The workflow must be present on the default branch to appear in the Actions menu.

If publishing fails after tag creation, rerun the original workflow run to preserve the same commit. An existing tag is accepted only when it points to that commit; an existing release causes publication to fail without replacing it. A clean package check does not establish that the plugin has been released or installed in a client.
