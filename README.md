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

For manual downloads, Bob IDE, or a skill that does not appear, see [installation](docs/installation.md).

## Run a skill

Start a new session after installation. Enter the prompt in your AI client's chat, replacing `<pr-url>` with the pull request URL.

**Codex**

```text
$review-pr Review <pr-url> and draft a review.
```

**Claude Code**

```text
/keycloak-ai-skills:review-pr Review <pr-url> and draft a review.
```

For other supported clients, ask `Use review-pr to review <pr-url>.` Replace `review-pr` with any skill below.

## Available skills

| Task | Skill | Example prompt |
| --- | --- | --- |
| Investigate a bug | [triage-bug](skills/triage-bug/SKILL.md) | `Use triage-bug to assess <issue-url>.` |
| Assess security impact | [triage-cve](skills/triage-cve/SKILL.md) | `Use triage-cve to assess <report>.` |
| Implement a fix | [fix-issue](skills/fix-issue/SKILL.md) | `Use fix-issue to fix <issue-url> in <checkout>.` |
| Review a change | [review-pr](skills/review-pr/SKILL.md) | `Use review-pr to review <pr-url>.` |
| Create a skill | [add-skill](skills/add-skill/SKILL.md) | `Use add-skill to create a skill for <task>.` |

Triage and review produce drafts; `fix-issue` edits your checkout and runs checks. Posting, publishing, and changes to live systems require your authorization.

## Further documentation

- [Installation and manual downloads](docs/installation.md)
- [More examples and review modes](docs/usage.md)
- [Contributing, validation, and releases](CONTRIBUTING.md)

## License

[Apache License 2.0](LICENSE.txt).
