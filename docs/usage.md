# Using the skills

Choose a skill from the [README](../README.md#available-skills), provide the issue, PR, or report, and add the relevant version or checkout. URLs, repository-qualified issue numbers, and pasted evidence are supported where applicable. The skills use available repository/tracker tools and report access or validation gaps.

## Invocation

You can request a skill by name in ordinary language. For explicit invocation:

| Client | Example |
| --- | --- |
| Codex | `$review-pr` |
| Claude Code | `/keycloak-ai-skills:review-pr` |
| Other supported clients | `Use review-pr to review <pr-url>.` |

Replace `review-pr` with the desired skill name. Start a new session after installing or updating the collection.

## Investigate a bug

```text
Use triage-bug to analyze <issue-url>, check duplicates, and draft a report, short comment, and next actions.
```

Include the affected version, deployment details, and reproducer when available. The skill checks expected versus observed behavior, duplicates and existing fixes, and priority using Keycloak's verification flow. Security concerns are routed for appropriate handling.

## Assess a security report

```text
Use triage-cve to assess <report>, check related issues, and draft an internal handoff and a public-safe reply.
```

Specify the intended audience and whether the report is private. Keep confidential evidence in authorized private sources. The assessment distinguishes security impact, CVE status, severity, urgency, and disclosure handling. For the security-tracker workflow, current authorized handling policy access may be needed for tracker recommendations.

## Implement a fix

```text
Use fix-issue to fix <issue-url> in <checkout> on <branch>, including regression coverage.
```

Provide a target checkout or revision. The skill traces the root cause, reuses suitable Keycloak abstractions, implements the fix, and validates supported behavior. It discusses unresolved contract or compatibility choices with you. A CVE or prior triage is not required.

## Review a pull request

```text
Use review-pr in feature mode to review <pr-url> against <design-or-issue-url>.
```

Provide a PR URL or a diff with base/head revisions and issue or design context. Optional modes are `bug`, `feature`, `hardening`, and `vulnerability`; otherwise the skill selects relevant checks. Feature mode covers enhancements and new capabilities. Reviews assess requirements, architecture, completeness, tests, compatibility, and relevant security controls. Vulnerability review does not require a CVE or a separate triage assessment.

## Create a skill

```text
Use add-skill to create a skill for reviewing Keycloak configuration.
```

Describe the task, expected result, and target client or location when known. Collection skills go in `skills/`; standalone skills use the target client's discovery directory. The authoring workflow keeps instructions portable and adds supporting resources when useful.

## Drafts and changes

Triage and review return assessments and comment drafts. A fix request includes local implementation and validation. Posting comments, triggering bots, changing tracker state, publishing, or modifying live systems requires authorization for the action and destination. Existing authorization is honored.

For the detailed decision criteria, follow the skill links in the README. The [triage guidance](../skills/triage-bug/references/triage-guidance.md) and [review guidance](../skills/review-pr/references/review-guidance.md) explain which project requirements and external recommendations apply.
