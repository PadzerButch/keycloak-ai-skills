---
name: triage-bug
license: Apache-2.0
description: Triage a bug report in the public Keycloak project, check duplicates and existing fixes, assess priority using Keycloak's flow, and draft an evidence-based report, natural issue comment, and next actions. Use for issue triage rather than PR review or a full CVE assessment.
---

# Triage a Keycloak bug

Analyze one supplied issue and deliver a sourced assessment, a short public comment draft, and actionable next steps. Keep disposition, technical impact, priority, and confidence separate.

## Inputs and tools

Accept an issue URL, repository-qualified number, or pasted text. Resolve a bare number from repository context; ask when ambiguous. Optional context includes distribution, affected versions, environment, checkout, reproducer, and audience. Recover relevant details from available sources before asking for more.

Use available GitHub connectors, GitHub CLI (`gh`), web access, and local repository tools; prefer a suitable connector unless the user requests another tool. Read [CLI examples](references/github-cli.md) when using `gh`. Read [evidence and verification](references/evidence.md) for provenance, safe reproduction, and handling access gaps.

Read [Keycloak's public workflow](references/keycloak-workflow.md) and refresh relevant project sources before selecting actions. It contains the verification and priority mappings; read its linked automation notes only when the proposed action depends on them. For general practice or policy gaps, consult [guidance and relevance](references/triage-guidance.md). External recommendations do not replace project rules or introduce vendor SLAs.

## Workflow

### 1. Establish the evidence

Read the body, relevant comments and timeline, linked reports, PRs, and reproduction evidence. Record issue identity, retrieval date, current state, existing decisions, distribution, version/build, component, and feature maturity. Distinguish upstream Keycloak from Red Hat build of Keycloak and other downstream distributions.

Explain expected versus observed behavior, with matching-version documentation or code references. Consult release and migration notes before calling an upgrade difference a regression. For protocol claims, check the applicable specification version, section, and implementation role. Distinguish product defects, documentation defects, configuration problems, intentional changes, and custom-extension incompatibility; a help request can reveal a real defect.

Capture the minimal reproducer, frequency, last working and first failing versions, concrete operational impact, workaround, and only relevant environment details. These may include database/JVM, topology/proxy, Operator, browser/client, identity provider, feature flags, or custom providers/themes. Ask for the smallest missing evidence that changes the decision, not a generic diagnostic bundle.

A regression checkbox, stack trace, or plausible code path does not establish the cause. Do not require a production upgrade or risky downgrade. For intermittent failures, describe a bounded repetition/load check when useful.

### 2. Search duplicates and fixes

Follow [duplicate and fix search](references/duplicate-search.md), comparing the reported behavior and relevant configuration with credible candidates.

### 3. Verify and prioritize

Apply the verification flow in the workflow reference: correct area/team, help request, release currency, sufficient information, valid bug, then priority. Establish current ownership and labels; propose a responsible role if a team is unknown. Report bugs, duplicates, already-fixed issues, help/configuration requests, enhancements, and inconclusive cases distinctly. Lack of local tools is not missing reporter information, and uncertainty is not a reason to declare a report invalid.

Describe the blocked capability, affected population/use case, availability or data impact, frequency, and workaround. Follow the priority diagram and cite the facts supporting its branch. Do not map vendor support severity or invent P0–P3 labels. One reporter does not mean one affected user, and unknown impact is not low impact. Do not invent numeric thresholds for “many” or “some” users. If a branch is unresolved, give a conditional recommendation and the smallest check needed; describe exceptional urgency for maintainer consideration separately.

### 4. Route security concerns when found

At any stage, credible authentication bypass, privilege escalation, cross-realm access, sensitive-data exposure, or attacker-driven availability impact warrants reading [security handling](references/security-handling.md). Prepare the policy-specific handoff; an identity-related symptom alone does not prove a vulnerability.

For dependency CVEs, identify the responsible team and assess reachability. Attribute Keycloak's special “affected”/“vulnerable” terminology when used and explain proposed closure.

Recommend `triage-cve` when a full security assessment is needed and available. Ordinary bugs need no CVSS score or CVE recommendation.

### 5. Draft the handoff and comment

Use the [report template](assets/report-template.md) as a checklist of relevant content, not a mandatory layout. A straightforward case can use a few paragraphs plus a comment draft; expand for material uncertainty. Lead with disposition, justified priority or pending decision, confidence, and next step. Include evidence, duplicate/fix coverage, workflow rationale, and limitations. Return the assessment in the response unless a file is requested; preserve existing files when saving.

Recommend the smallest coherent action set, normally one main triage action plus justified routing. Separate action labels from resulting labels and explain relevant bot side effects, including comments, closures, milestones, and aging. Do not duplicate bot-managed transitions. For already-triaged issues follow the priority-change process in the reference. Consider backports with evidence for affected maintained branches; leave unverified targets pending. Do not promise a fix, assignee, milestone, deadline, or backport approval.

Give the applicable next steps with an actor, action, reason, expected effect, and completion condition; a single next step needs no table. State what evidence should reopen the decision. Consult project test guidance when recommending a regression test; implementation is a separate task.

Write a public comment draft of roughly two to four short sentences: the specific finding or uncertainty, its key reason, a useful link when needed, and a focused next step. Use plain, respectful language without stock praise or blame. Do not claim reproduction, maintainer agreement, or a fix without evidence. Avoid repeating the full report or generic text the bot will post. Keep the proposed action in the handoff by default. When explicitly preparing a bot-triggering comment, put the verified `~<action-name>` on its final line and describe the effects outside the copyable draft.

This workflow drafts by default. Posting comments or bot triggers, changing metadata, closing/reopening/transferring issues, assigning people, and contacting security teams require explicit authorization for the action and destination. Honor authorization already given. Refresh the issue before an authorized change and verify the result afterward; do not duplicate successful mutations or comments. An authorized comment does not implicitly authorize an additional bot-triggered transition.

## Completion

Complete when the assessment, proposed comment, and applicable handoff above are delivered, with proposed, performed, and pending actions distinguished. Triage completion does not establish reproduction, a fix, release, full security assessment, or tracker changes.
