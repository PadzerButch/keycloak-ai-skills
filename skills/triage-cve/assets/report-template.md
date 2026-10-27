# Triage report: {{issue title}}

- Issue: {{canonical link or supplied identifier}}
- Assessed: {{date; source retrieval dates where relevant}}
- Disposition and confidence: {{classification; confidence and reason}}
- CVE status: {{verified ID and record state, candidate, no recommendation, or unknown}}
- Duplicate status: {{canonical duplicate, possible duplicate, related only, or none found within stated coverage}}
- Scope: {{distribution, component, version/commit, feature maturity, deployment, audience}}

## Finding and rationale

{{Explain expected versus observed behavior, root cause, attacker prerequisites, security boundary, and impact. Distinguish reported claims, verified evidence, and inference. Explain the classification and CVE recommendation, counterevidence, and any supported CWE mapping.}}

## Evidence and verification

| Evidence | Observation | Source / revision | Status |
| --- | --- | --- | --- |
| {{claim or test}} | {{what it supports or contradicts}} | {{link or path and commit}} | {{reported, inspected, reproduced, or unverified}} |

{{Record affected-version evidence without extrapolating unsupported ranges. State tests actually run, configuration, results, and missing verification.}}

## Duplicates and related issues

Search coverage: {{sources, queries, open/closed coverage, date, access gaps}}.

| Candidate | Relationship | Evidence for or against a match |
| --- | --- | --- |
| {{issue, PR, advisory, or CVE link}} | {{confirmed duplicate, possible duplicate, related, or distinct}} | {{root cause, versions, prerequisites, impact, fix}} |

{{If no credible matches, remove the example row and state that none were found in the searched sources.}}

## Severity assessment

- Scenario: {{attacker starting point, target, prerequisites, and resulting impact}}
- Method: {{CVSS version and metric groups, or reason not assessed}}
- Vector: {{complete justified vector, or pending metrics}}
- Score and severity: {{verified calculation, attributed published score, or pending}}
- Calculation source: {{tool/version or calculator link; exact vector used}}

| Metric | Value | Rationale and evidence / assumption |
| --- | --- | --- |
| {{each required metric}} | {{selected value}} | {{specific supporting fact or uncertainty}} |

{{Distinguish provisional assessment from vendor scores. Explain differing scenarios and deployment risk separately. Remove the metric table if no assessment is supportable.}}

## Next action and limitations

{{Recommend the concrete next step, key unanswered question, and applicable security handling. For a security submission draft, state AI assistance and actual reproduction and human-review status.}}

## Proposed comment — draft

{{Two to four short, natural sentences: conclusion, key reason, relevant link when useful, and next step. Match the audience and avoid exposing private details.}}
