# Keycloak AI Skills

Reusable AI skills for Keycloak skill authoring, bug and security triage, and pull request review. The current package version is `0.3.0`.

| Skill | Purpose |
| --- | --- |
| [add-skill](skills/add-skill/SKILL.md) | Turn a task description into a reusable skill. |
| [triage-bug](skills/triage-bug/SKILL.md) | Triage a public bug report, check duplicates and fixes, follow Keycloak's priority flow, and draft a report, comment, and next actions. |
| [triage-cve](skills/triage-cve/SKILL.md) | Analyze an issue, check duplicates, classify security impact, assess CVSS, urgency, and embargo handling, and draft a report, comment, and workflow handoff. |
| [review-pr](skills/review-pr/SKILL.md) | Review fixes, enhancements, and new features for requirements, specification applicability, completeness, regressions, and valid findings; draft a review. |

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

Bob Shell uses an extension context file to find the shared skills. Bob IDE has separate [skill discovery](https://bob.ibm.com/docs/ide/features/skills); the Shell command does not install an IDE plugin. Other Agent Skills clients can use the same skill folders through their own installer.

## Use

Start a new session after installation and ask:

```text
Use add-skill to create a skill for reviewing Keycloak configuration.
```

In Claude Code, use `/keycloak-ai-skills:add-skill`. In Codex, use `$add-skill`. For discovery paths and activation details, see [client support](skills/add-skill/references/client-support.md). Verified versions and limitations are recorded in [compatibility checks](docs/compatibility.md).

New collection skills go in `skills/`. Standalone skills go in the target tool's discovery directory; `add-skill` identifies that tool before choosing a path.

To triage a public bug, provide its URL, repository-qualified number, or text:

```text
Use triage-bug to analyze <issue-url>, check duplicates, and draft a report, short comment, and next actions.
```

The skill follows Keycloak's verification and priority diagrams, keeps impact and confidence separate from priority, and checks current metadata and bot effects. It supports GitHub connectors, `gh` CLI, and pasted evidence with explicit access limits. Its [guidance map](skills/triage-bug/references/triage-guidance.md) ranks Keycloak, OpenSSF, CNCF, Linux Foundation, IBM, Red Hat, and other applicable sources. Reports include security routing when relevant; a full CVE assessment remains a separate task.

In Codex, invoke `$triage-bug`; in Claude Code, use `/keycloak-ai-skills:triage-bug`. It drafts by default; posting comments, triggering bots, and changing tracker state require authorization for those actions.

To assess security impact or CVE relevance, provide an issue URL, tracker-qualified ID, or text:

```text
Use triage-cve to analyze <issue-url>, check for duplicates, and draft a report and short comment.
```

Triage also records urgency, disclosure/embargo reasoning, and the next responsible role or team. For the security-tracker workflow, it drafts tracker changes and a handoff using the current handling policy and authorized sources. It keeps CVSS, project severity, CVE status, and disclosure decisions distinct; proposed actions require authorization before execution.

To review a proposed fix, enhancement, or new feature, provide a PR URL or a diff with base/head revisions and issue/design context:

```text
Use review-pr to review <pr-url> and draft an evidence-based review.
```

Optionally request `bug`, `feature`, `hardening`, or `vulnerability` mode; `feature` covers enhancements and new capabilities. Otherwise the skill selects relevant checks from the evidence and states any uncertainty. All modes include specification applicability, finding validation, tests, compatibility, and baseline security checks. Feature review adds acceptance, design, completeness, and adoption checks; additional security guidance is loaded for relevant controls and trust boundaries as well as fixes. A vulnerability fix does not need a CVE. `triage-cve` remains optional for separate issue triage and severity assessment.

For example:

```text
Use review-pr in feature mode to review <pr-url> against <design-or-issue-url>.
```

The skill's [review guidance](skills/review-pr/references/review-guidance.md) maps CNCF, Linux Foundation, OpenSSF, OWASP, Google, Apache TVM, and IBM sources to applicable checks. It distinguishes Keycloak requirements from external recommendations and historical context.

In Codex, invoke `$review-pr`; in Claude Code, use `/keycloak-ai-skills:review-pr`. These skills draft findings without posting them. New collection skills become available after the updated plugin is released and installed; start a new session after updating. Structural validation does not verify client discovery or invocation.

## Maintain

Keep shared metadata in `plugin.json` and instructions in `skills/`. The Codex catalog is `.agents/plugins/marketplace.json`; Claude and Copilot share `.claude-plugin/marketplace.json`. Claude, Gemini, and Bob Shell have small compatibility manifests. `BOB.md` routes Bob Shell to the shared skills without duplicating their instructions.

When releasing, keep the version identical in `plugin.json`, `.claude-plugin/plugin.json`, `gemini-extension.json`, and `bob-extension.json`, and update the version stated in this README. Keep shared descriptions consistent across these manifests. The marketplace catalogs reference the package and have no version field. Checks reject mismatched metadata and catalogs. There is no metadata generator.

With Python 3.10+:

```bash
python -m pip install -r requirements-dev.txt
python scripts/check-package.py
python -m unittest discover -s tests -v
```

CI runs these checks on Linux and Windows with Python 3.10 and 3.14. The validator checks containment, relative symlinks, bounded YAML without aliases, and CommonMark links outside code examples. Scaffold markers use `@@ADD_SKILL_...@@` and are checked in UTF-8 resources outside `assets/`, with a 1 MiB limit per checked file. Structural checks do not prove client activation.

## Publish

Prepare and commit the version changes described above, then push them to the default branch. To publish a release, open **Actions → Release → Run workflow**, select the default branch, and enter the committed version without a `v` prefix (for example, `0.3.0`). The workflow supports stable `X.Y.Z` versions.

The manual workflow verifies all four manifest versions and the README version, runs package validation and tests on Linux and Windows with Python 3.10 and 3.14, then tags the exact validated commit as `vX.Y.Z` and publishes a GitHub Release with generated release notes. GitHub provides the source archives. It uses the built-in `GITHUB_TOKEN`; no additional release secret is required. Repository rules must allow that token to create the release tag.

If publishing fails after tag creation, rerun the original workflow run so it uses the same commit. An existing tag is accepted only when it points to that commit; an existing release causes publication to fail without replacing it. The workflow must first be present on the default branch to appear in the manual Actions menu.

For the initial repository push:

```bash
git status --short
git add -A
git diff --cached --stat
git commit -m "Publish Keycloak AI skills collection"
git push -u origin main
```

## License

[Apache License 2.0](LICENSE.txt).
