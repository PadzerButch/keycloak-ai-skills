---
name: review-pr
license: Apache-2.0
description: Review a Keycloak pull request for a bug fix, enhancement, new feature, security hardening, or vulnerability fix with or without a CVE. Verify requirements, specification applicability, completeness, regressions, and finding validity; produce an evidence-based report and draft review. Use for reviewing proposed changes, not standalone issue triage or implementing changes.
---

# Review a Keycloak pull request

Determine whether a proposed change meets its applicable requirements, preserves supported behavior, and introduces actionable defects. Return a review tied to an exact revision, with evidence and explicit limits.

Apply the judgment expected of a Keycloak maintainer responsible for correctness, security, architectural fit, compatibility, and long-term maintainability. Assess whether fixes restore the violated invariant across affected paths and whether features build on suitable existing abstractions. Judge design patterns by the responsibilities and guarantees they clarify. Investigate unusual designs before recommending replacement; justify architectural changes with concrete consequences and distinguish necessary corrections from optional improvements. A workaround alone does not establish a complete fix.

## Inputs and boundaries

Accept a PR URL or repository-qualified number, or a supplied diff with base/head revisions and issue/design context. Resolve a bare number from the user's repository context. Optional inputs include the mode (`bug`, `feature`, `hardening`, or `vulnerability`), design proposal and acceptance criteria, advisory or private report, distribution/version, deployment configuration, reproducer, and intended audience. Treat “enhancement” and “new feature” as feature review, “weakness” as hardening, and “CVE fix” as vulnerability review, without assuming that the labels establish exploitability.

Use available repository/tracker tools, local code, and authoritative documentation; no particular client is required. Read [evidence and verification](references/evidence.md) for provenance, safe verification, and handling access gaps. Ask for missing information only when it materially prevents a reliable review.

Review drafts do not authorize implementing fixes, posting comments/reviews or security reports, changing metadata, creating issues, committing, pushing, or merging. Honor explicit authorization already given for the action and destination.

## Workflow

### 1. Establish the change and expected behavior

Read applicable repository instructions, `CONTRIBUTING.md`, `SECURITY.md`, and relevant build/test guidance. Inspect the linked issue, design proposal or report, PR discussion, changed files, and CI results. Existing review comments are claims to verify; avoid repeating findings already resolved at the reviewed head.

Record the repository, PR, target branch, base and head SHAs, merge base, and assessment date. Review the merge-base-to-head diff and trace affected callers, implementations, validation, and tests beyond the changed lines. For supplied patches, state unavailable revision/context information. Recheck the head before finalizing when possible; if it changed, review the delta or clearly limit conclusions to the recorded revision.

When Ripwire is available and useful, follow [optional Ripwire assistance](references/ripwire.md) to investigate affected callers, change impact, and candidate tests at the reviewed revision. Otherwise use the usual repository tools; Ripwire is not required.

For fixes, explain the original trigger, actual versus expected behavior, and root cause. Establish whether the report describes a defect, expected behavior, unsupported usage, misconfiguration, or an enhancement. For features and enhancements, establish the user problem, intended capability, acceptance criteria, design rationale, and agreed exclusions; distinguish explicit requirements from inferred expectations without inventing scope. Check whether the proposed behavior is itself valid. Intentional changes can still break supported contracts; misconfiguration does not automatically excuse a violation of documented guarantees or safe defaults.

### 2. Verify specification applicability

Identify the authoritative requirements for the affected behavior: protocol specifications and selected profiles/extensions, matching-version Keycloak documentation, API/SPI contracts, and repository policy. Use primary sources, check relevant errata and updates, and cite exact versions and sections when alleging noncompliance.

Verify that each requirement applies to Keycloak's participant role, flow, feature maturity, configuration, and version. Distinguish `MUST`/`MUST NOT`, `SHOULD`/`SHOULD NOT`, and `MAY`; evaluate conditional requirements and justified exceptions. Do not turn examples, recommendations, or common practice into unconditional requirements. If multiple behaviors are permitted, explain why the chosen behavior is acceptable or harmful.

Explain conflicts between documentation, implementation, and specifications rather than silently selecting one as intent. An unavailable source or uncertain applicability is a limitation, not a confirmed violation. Specification compliance alone does not establish security: also evaluate the intended trust boundaries and supported deployment assumptions.

Read the [review guidance source map](references/review-guidance.md) when selecting external criteria or resolving their authority and applicability. Consult only relevant primary sources, including protocol specifications and security requirements when affected. Keycloak's policies govern project-specific choices; external checklists, badge criteria, and product tutorials are advisory unless adopted. This is not a full compliance certification or an unrelated audit.

### 3. Select the review depth

All modes include the shared checks below. Honor a requested mode as a starting point; it does not establish the security classification or suppress relevant findings. Otherwise select checks from the evidence and state the rationale and any uncertainty. Apply more than one mode when the change warrants it.

| Mode | Evidence and additional objective |
| --- | --- |
| `bug` | Assess whether the root cause is fixed across affected paths and supported behavior is preserved. No security impact has yet been established. |
| `feature` | Assess whether an enhancement or new capability meets established requirements, fits the architecture, and is complete and usable within its agreed scope. |
| `hardening` | Assess a defined security property or reduced exposure even when an exploitable attack path is unestablished. Do not require a demonstrated exploit to recognize useful hardening. |
| `vulnerability` | Assess an alleged or established attack path, security boundary, and impact, then verify the fix and relevant bypasses. A CVE is optional; the review may conclude that the security claim is unsupported or uncertain. |

Read [feature review](references/feature-review.md) for enhancements and new features. Read [security review](references/security-review.md) for hardening or vulnerability changes, new or materially changed security controls/trust boundaries, or a credible security concern found during review. A feature may need security design review before any vulnerability is suspected; a PR labeled “bug” can also require security review. Conversely, a CVE label does not prove that an advisory applies to this patch. Mixed changes can use multiple references without duplicating shared checks.

The separate `triage-cve` skill is optional for issue classification, duplicate analysis, CVE relevance, or severity assessment when requested. Use an existing triage report as evidence, not unquestioned fact. This review is self-contained: do not require that skill, repeat a full triage, or calculate CVSS merely to assess patch correctness.

### 4. Review the implementation and its consequences

Connect each substantive change to the reported problem, agreed requirement, or necessary supporting work. Inspect realistic execution paths and, for fixes, the root cause, including boundary/malformed input, failure handling, cleanup, concurrency, and transaction behavior where affected. Check legitimate behavior as well as rejection paths.

Apply these checks proportionately to the code being changed:

- **Security baseline:** authentication and authorization enforcement; realm, client, and user isolation; validation at trust boundaries; secret/personal-data exposure; attacker-controlled resource consumption. Investigate safeguards in callers and downstream code before alleging a bypass.
- **Compatibility:** REST and protocol behavior, SPI/providers, configuration defaults, supported feature profiles, federation/brokering, and custom extensions. Verify relevant documentation and migration guidance.
- **State and operation:** database/data migration, import/export, distributed caches and invalidation, online/offline sessions, and supported clustering or rolling-upgrade behavior.
- **Performance:** query counts, blocking calls, unbounded work, memory/resource growth, and frequently used authentication paths. Explain a concrete workload and consequence rather than asserting hypothetical slowness.
- **Maintainability and usability:** consistency with existing architecture, unnecessary complexity, duplicated logic, error behavior, and relevant UI accessibility/localization. Separate unrelated refactoring and personal style preferences from actionable defects.

Check contribution requirements from the applicable repository revision, such as issue linkage, sign-offs, commit structure, formatting, documentation, and required disclosures. Report these separately from code defects; private security handling takes precedence over a routine public issue-link requirement.

### 5. Validate tests and findings

Assess whether tests assert meaningful behavior and cover the applicable requirements. For fixes, check that regression tests exercise the reported failure; when feasible, run them against the affected base and reviewed head to show failure before the fix and success afterward. Check that any failure demonstrates the intended defect rather than setup trouble. For features, verify acceptance scenarios on the head and preservation of existing behavior; a new API or schema may not exist on the base, so compilation failure there is not evidence of a defect. Use an isolated checkout for temporary tests; if execution is unavailable, explain the code-based evidence and what remains unverified.

Follow the target repository's current test guidance and nearby examples. Keycloak favors integration/functional tests, with unit tests for suitable isolated logic; do not introduce mocking frameworks. Identify relevant missing negative, boundary, permission, and compatibility coverage without demanding an exhaustive test matrix for every patch. Check test isolation, meaningful assertions, and avoidable timing/flakiness risks.

Run focused checks appropriate to the change; inspect CI results and skipped jobs for the reviewed revision. Record commands, revisions/configuration, results, and reasons for omissions. Do not equate passing CI with correctness or imply that proposed tests were executed.

Before reporting a defect, actively try to disprove it: trace the complete relevant path, look for guards and counterexamples, and verify its prerequisites. Establish the trigger, expected versus actual behavior, impact, and supporting evidence. Distinguish observed facts, code-based deductions, and assumptions; execution is stronger evidence but is not mandatory for a sound, complete code-based finding.

Classify each concern as introduced/exposed by the PR, an incomplete fix, an unmet established feature requirement, or unrelated and pre-existing. Keep the last category separate from merge-blocking findings. Cite the requirement and demonstrate the gap before calling a feature incomplete; unclear scope belongs under open questions. Drop disproven concerns and deduplicate by root cause/remedy. Test gaps and policy gaps are not themselves proof of a runtime defect.

### 6. Deliver the review

Use the [review report](assets/review-report.md) as a content checklist, omitting irrelevant sections and using concise prose for simple changes. Lead with actionable findings ordered by justified severity. Use its finding fields for the trigger, location, impact, evidence, confidence, and correction/coverage direction. Prefer a changed location; explain the connection to the diff when evidence resides elsewhere. Verify source links and line references. Return the review in the response unless a file is requested; preserve existing files when saving.

Separate confirmed defects, unanswered questions, test/validation gaps, repository-policy gaps, and optional improvements. Review severity expresses impact and urgency; it is not a CVSS score. Do not invent findings, a fixed finding quota, or claims of complete security. If none are established, explicitly say so within the reviewed scope.

State whether the change meets its applicable requirements and, for fixes, whether the original problem appears fully fixed. Report what was actually validated, coverage limits, and a recommendation of `ready`, `changes required`, or `insufficient evidence`, with reasons. Separate technical readiness from unresolved product/design acceptance; do not invent maintainer approval. Recommend readiness only when the evidence is adequate; missing execution alone is not an automatic blocker for every change. This is a recommendation, not a submitted approval.

End with a concise proposed review comment matching the intended audience. For sensitive findings or uncertain disclosure status, apply [security handling](references/security-handling.md).

## Completion

Complete when the revision-scoped assessment, findings or explicit absence of established defects, validation limits, justified readiness recommendation, and proposed review above are delivered. Completion does not submit an approval or establish maintainer acceptance.
