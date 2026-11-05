# Keycloak AI Skills

AI skills to investigate Keycloak issues, assess security reports, implement fixes, and review pull requests. The current package version is `0.4.0`.

## Quick start

Choose your client, then run either the install or upgrade commands in your terminal. Use a current version with plugin or extension support.

<details>
<summary>Codex</summary>

Install:

```bash
codex plugin marketplace add lhanusov/keycloak-ai-skills
codex plugin add keycloak-ai-skills@keycloak-skills
```

Upgrade an existing installation:

```bash
codex plugin marketplace upgrade keycloak-skills
```

</details>

<details>
<summary>Claude Code</summary>

Install:

```bash
claude plugin marketplace add lhanusov/keycloak-ai-skills
claude plugin install keycloak-ai-skills@keycloak-skills
```

Upgrade an existing installation:

```bash
claude plugin marketplace update keycloak-skills
claude plugin update keycloak-ai-skills@keycloak-skills
```

</details>

<details>
<summary>GitHub Copilot CLI</summary>

Install:

```bash
copilot plugin marketplace add lhanusov/keycloak-ai-skills
copilot plugin install keycloak-ai-skills@keycloak-skills
```

Upgrade an existing installation:

```bash
copilot plugin marketplace update keycloak-skills
copilot plugin update keycloak-ai-skills
```

</details>

<details>
<summary>Gemini CLI</summary>

Install:

```bash
gemini extensions install https://github.com/lhanusov/keycloak-ai-skills
```

Upgrade an existing installation:

```bash
gemini extensions update keycloak-ai-skills
```

</details>

<details>
<summary>IBM Bob Shell</summary>

Install:

```bash
bob extensions install https://github.com/lhanusov/keycloak-ai-skills
```

Upgrade an existing installation:

```bash
bob extensions update keycloak-ai-skills
```

</details>

For manual downloads, Bob IDE, or a skill that does not appear, see [installation](docs/installation.md).

## Run a skill

Start a new session after installing or upgrading. Enter the prompt in your AI client's chat, replacing `<pr-url>` with the pull request URL.

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
