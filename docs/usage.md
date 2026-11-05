# Using the skills

Choose a skill from the [README](../README.md#available-skills) and provide the issue, PR, or report. Add the relevant version or checkout when known. You can supply a URL, a repository-qualified issue number, or pasted evidence.

## Invocation

Use the [Codex and Claude Code prompts](../README.md#run-a-skill), replacing `review-pr` with the desired skill name. The examples below use plain-language requests that you can also enter directly in supported clients.

## Investigate a bug

```text
Use triage-bug to analyze <issue-url>, check duplicates, and draft a report, short comment, and next actions.
```

Include the affected version, deployment details, and reproducer when available. The skill checks expected versus observed behavior, duplicates and existing fixes, and priority using Keycloak's verification flow. Security concerns are routed for appropriate handling.

## Assess a security report

```text
Use triage-cve to assess <report>, check related issues, and draft an internal handoff and a public-safe reply.
```

Specify the intended audience and whether the report is private. Keep confidential evidence in authorized private sources. The assessment distinguishes security impact, CVE status, severity, urgency, and disclosure handling. Tracker recommendations use verified metadata and the applicable security policy.

## Implement a fix

```text
Use fix-issue to fix <issue-url> in <checkout> on <branch>, including regression coverage.
```

Provide a target checkout or revision. The skill traces the root cause, reuses suitable Keycloak abstractions, implements the fix, and validates supported behavior. It discusses unresolved contract or compatibility choices with you. A CVE or prior triage is not required.

## Review a pull request

```text
Use review-pr in feature mode to review <pr-url> against <design-or-issue-url>.
```

Provide a PR URL or a diff with base/head revisions and issue or design context. The skill selects relevant checks automatically. To guide its focus, request `bug`, `feature` (including enhancements), `hardening`, or `vulnerability` mode. A CVE or prior triage assessment is not required.

## Create a skill

```text
Use add-skill to create a skill for reviewing Keycloak configuration.
```

Describe the task, expected result, and target client or location when known. Collection skills go in `skills/`; standalone skills use the target client's discovery directory. The authoring workflow keeps instructions portable and adds supporting resources when useful.

## Drafts and changes

Triage and review return assessments and comment drafts. A fix request includes local implementation and validation. Posting comments, triggering bots, changing tracker state, publishing, or modifying live systems requires your authorization.

For the detailed decision criteria, follow the skill links in the README. The [triage guidance](../skills/triage-bug/references/triage-guidance.md) and [review guidance](../skills/review-pr/references/review-guidance.md) explain which project requirements and external recommendations apply.
