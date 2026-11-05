# Keycloak AI Skills

AI skills to investigate Keycloak issues, assess security reports, implement fixes, and review pull requests. The current package version is `0.4.0`.

## Quick start

Choose your client and run its installation commands. Use a current version with plugin or extension support.

<details>
<summary>Codex</summary>

```bash
codex plugin marketplace add lhanusov/keycloak-ai-skills
codex plugin add keycloak-ai-skills@keycloak-skills
```

</details>

<details>
<summary>Claude Code</summary>

```bash
claude plugin marketplace add lhanusov/keycloak-ai-skills
claude plugin install keycloak-ai-skills@keycloak-skills
```

</details>

<details>
<summary>GitHub Copilot CLI</summary>

```bash
copilot plugin marketplace add lhanusov/keycloak-ai-skills
copilot plugin install keycloak-ai-skills@keycloak-skills
```

</details>

<details>
<summary>Gemini CLI</summary>

```bash
gemini extensions install https://github.com/lhanusov/keycloak-ai-skills
```

</details>

<details>
<summary>IBM Bob Shell</summary>

```bash
bob extensions install https://github.com/lhanusov/keycloak-ai-skills
```

</details>

Start a new session, then ask:

```text
Use review-pr to review <pr-url> and draft a review.
```

For manual downloads, Bob IDE, or discovery problems, see [installation](docs/installation.md).

## Available skills

| Task | Skill | Example prompt |
| --- | --- | --- |
| Investigate a bug | [triage-bug](skills/triage-bug/SKILL.md) | `Use triage-bug to assess <issue-url>.` |
| Assess security impact | [triage-cve](skills/triage-cve/SKILL.md) | `Use triage-cve to assess <report>.` |
| Implement a fix | [fix-issue](skills/fix-issue/SKILL.md) | `Use fix-issue to fix <issue-url> in <checkout>.` |
| Review a change | [review-pr](skills/review-pr/SKILL.md) | `Use review-pr to review <pr-url>.` |
| Create a skill | [add-skill](skills/add-skill/SKILL.md) | `Use add-skill to create a skill for <task>.` |

Provide an issue, PR, or report and any relevant checkout or version. Triage and review produce drafts; `fix-issue` changes local code and runs checks. Publishing and external changes require authorization.

## Further documentation

- [Installation and manual downloads](docs/installation.md)
- [Usage, invocation syntax, and advanced examples](docs/usage.md)
- [Contributing, validation, and releases](CONTRIBUTING.md)

## License

[Apache License 2.0](LICENSE.txt).
