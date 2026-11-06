---
name: triage-cve
license: Apache-2.0
description: Triage a specific Keycloak issue for duplicates, related reports, and security impact. Use when asked to distinguish a bug, security weakness, or vulnerability, assess CVE relevance and CVSS severity, and draft an evidence-based report, issue comment, and workflow handoff.
---

# Triage a CVE candidate

Analyze one supplied issue and produce a reviewable triage report, a short, natural comment, and an actionable handoff. Treat classification, duplicate status, CVE assignment, severity, urgency, and embargo as separate decisions.

Apply the judgment expected of a Keycloak security response engineer responsible for validating trust-boundary violations, assessing realistic impact, and protecting confidential evidence. Reason from attacker capabilities, reachable code, and existing controls in the target version. Actively test both the vulnerability claim and explanations that would dismiss it; intended behavior and familiar architecture can still violate security guarantees. Keep uncertainty explicit without inflating severity or treating missing evidence as proof of safety.

## Inputs and tools

Accept an issue URL, a tracker-qualified ID, or pasted issue text. Resolve a bare issue number from the user's repository context; ask for the tracker or repository if ambiguous. Optional inputs include the affected version, deployment configuration, source checkout, reproducer, intended comment audience, and required CVSS version.

Use available tracker connectors, repository search, and web access; no particular client is required. Read [evidence and verification](references/evidence.md) and [security handling](references/security-handling.md) for provenance, safe reproduction, confidentiality, and policy checks.

For questions about general triage practice or gaps in project guidance, read [triage guidance and applicability](references/triage-guidance.md). Apply the current project policy and applicable upstream or downstream process; use general guidance to fill gaps, without importing another organization's routing, deadlines, or disclosure rules. Record material conflicts instead of silently choosing a rule.

## Workflow

### 1. Establish the evidence

When a local checkout and Ripwire are available and useful, follow [optional Ripwire assistance](references/ripwire.md) to locate relevant entry points and trace callers and safeguards. Otherwise use the usual repository tools; Ripwire is not required.

Read the issue body, relevant comments, linked pull requests, fixes, and reproduction evidence. Record issue identity, retrieval date, component, reported versions, and current status.

Establish distribution, release/commit, feature maturity, and configuration. Identify the attacker, required privileges, realm/client boundaries, expected versus actual behavior, and concrete confidentiality, integrity, or availability impact.

Check the available threat model, security self-assessment, and documented guarantees. Identify the boundary or guarantee the report claims to violate. State missing or disputed threat-model assumptions; intended behavior alone does not disprove a security defect. Distinguish a request to change the threat model from evidence that the implementation violates it.

### 2. Search for duplicates and related issues

Follow [duplicate and fix search](references/duplicate-search.md). Include [Keycloak advisories](https://github.com/keycloak/keycloak/security/advisories) and relevant [CVE records](https://www.cve.org/), alongside public or authorized private issues and fixes.

Verify any existing CVE against its authoritative record or assigning vendor advisory, including reserved, published, or rejected status. A reserved record may not provide enough information to establish a match.

### 3. Classify and explain

Choose a primary disposition using the available evidence:

| Disposition | Evidence needed |
| --- | --- |
| Bug without established security impact | Incorrect behavior with no supported attacker-driven security consequence in the assessed scenario. Explain the scope of that conclusion. |
| Security weakness / hardening opportunity | A security-relevant design or implementation condition, but no established exploitable vulnerability in the assessed context. State what additional conditions could change the assessment. |
| Security vulnerability / CVE candidate | A supported attack path violates an intended security boundary or causes unauthorized confidentiality, integrity, or availability impact. Explain prerequisites, affected behavior, and impact. |
| Inconclusive | Missing or contradictory evidence prevents a reliable choice. Name the smallest verification that would resolve it. |
| Expected behavior / configuration issue | Evidence supports intended behavior or a deployment-specific cause. Still evaluate whether documented guarantees or safe defaults are violated. |
| Dependency advisory not applicable in the assessed configuration | Evidence shows that the advisory's required functionality is absent or unreachable in the inspected build/configuration. State coverage and runtime limits without extrapolating to other deployments. |

These are triage dispositions, not disjoint technical taxonomies: a vulnerability can also be a bug caused by a weakness. Map a CWE only when the root cause supports it; use the [CWE definitions](https://cwe.mitre.org/about/index.html) and link the selected entry.

A CVE is an assigned identifier, not a severity category. Separately state “verified existing CVE,” “candidate for CNA review,” “no CVE recommendation on current evidence,” or “unknown,” with the rationale. Do not invent or assign an ID, promise eligibility, or use a score threshold as the assignment rule. Consult the current [CVE CNA rules](https://www.cve.org/ResourcesSupport/AllResources/CNARules/) for assignment questions; leave unresolved assignment decisions to the responsible CNA.

For a vulnerability or candidate, explain why the behavior is a security defect, who can exploit it, what additional access or damage it permits, affected-version evidence, and why a related advisory does or does not already cover it. Do not infer a complete affected version range from a single tested release. Record confidence and the strongest evidence against the conclusion.

A complete code-based attack path can support a candidate assessment when runtime verification is unavailable. Keep that conclusion distinct from reproduced observations and the validation required before submitting a report.

### 4. Assess severity

For a supported vulnerability or CVE candidate, establish the user's requested CVSS version and the applicable project's scoring requirement. When neither specifies a version, use CVSS v4.0. If the requested assessment and project workflow require different versions, identify their purposes and assess each as needed; leave a dependent decision pending if its required score is unavailable. Read the [scoring guidance](references/scoring.md) before selecting metrics. Provide a complete justified vector and a verified score and severity label when calculation is available; otherwise mark the numeric score and label pending calculation. Distinguish your provisional assessment from published vendor scores and explain differences.

If key facts are missing, give explicitly conditional scenarios or leave the assessment pending with the missing metrics identified. Do not fabricate a numeric score. For other dispositions, mark CVSS as not assessed and explain why; absence of evidence is not a score of zero.

### 5. Determine urgency and handoff

Record public-disclosure status, exploit availability, evidence of active exploitation, deployment exposure, and available mitigations. Distinguish unknown from absent, and a proof of concept from exploitation in the wild. Explain any urgency or escalation recommendation separately from CVSS. Recommend embargo handling using the applicable policy; severity alone does not establish permission to disclose.

Identify the next responsible role or team, the smallest outstanding verification, and any established communication or disclosure dates with their sources. Mark suggested owners and dates as proposals; do not invent assignments, agreements, or deadlines. If evidence is inconclusive, recommend retaining the need for triage and requesting the missing information.

When preparing tracker recommendations, security-team coordination, or a CVE-request draft, read [security triage handoff](references/security-workflow.md). Verify metadata and required decisions before proposing operational transitions. Continue technical analysis when handling requirements are unavailable, with the handoff marked provisional. Keep classification, CVE state, and downstream fix/release readiness distinct.

### 6. Deliver the report and comment

Use the [report template](assets/report-template.md) as a content checklist, omitting irrelevant sections and combining short conclusions into prose. Lead with disposition, confidence, and next action. Cover classification rationale, duplicate-search coverage, CVE status, CVSS or why it is pending/not assessed, applicable urgency/disclosure decisions, and limitations. A straightforward non-security disposition needs only a brief explanation of inapplicable security fields. Return the assessment in the response unless a file is requested; preserve existing files when saving.

End with a proposed comment of roughly two to four short sentences: the finding in plain language, its key reason, any useful canonical link, and the next step or focused question. Make it specific, respectful, and understandable without the full report. Avoid stock praise, inflated certainty, and claims of testing or maintainer agreement that did not happen.

Apply the audience and submission rules in security handling. Include a separate reporter reply only when the applicable workflow calls for it.

For confidential reports, limit public replies to review status and a public-safe next step unless more disclosure is authorized. Keep testing history, validation gaps, and technical rationale in the internal assessment; do not copy them into a public reply merely because they omit exploit details.

This workflow produces drafts. Posting comments (including bot triggers), changing tracker metadata, closing or transferring issues, contacting reporters, submitting security reports, and requesting CVE assignment require explicit user authorization for the action and destination. Honor authorization already given without asking again. A triage request alone does not authorize those actions. Fix implementation, merging, and release execution are separate tasks.

## Completion

Complete when the assessment and proposed comment above are delivered, with an actionable handoff and proposed tracker changes when applicable. Identify unverified metadata and unresolved evidence. Triage completion does not establish a confirmed vulnerability, fix, CVE assignment, or completed workflow action.
