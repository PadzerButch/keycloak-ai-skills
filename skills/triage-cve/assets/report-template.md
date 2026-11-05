# Triage report: {{issue title}}

<!-- Content checklist: omit irrelevant fields, combine short sections, and use prose instead of tables for straightforward cases. -->

- Issue: {{canonical link or supplied identifier}}
- Assessed: {{date; source retrieval dates where relevant}}
- Disposition and confidence: {{classification; confidence and reason}}
- CVE status: {{verified ID and record state, candidate, no recommendation, or unknown}}
- Duplicate status: {{canonical duplicate, possible duplicate, related only, or none found within stated coverage}}
- Scope: {{distribution, component, version/commit, feature maturity, deployment, audience}}
- Handling basis: {{applicable project policy and workflow sources, revisions/dates, access gaps, and material conflicts}}

## Finding and rationale

{{Explain expected versus observed behavior, root cause, attacker prerequisites, security boundary, and impact. Identify the relevant threat-model assumption or documented guarantee, including any disagreement or missing source. Distinguish reported claims, verified evidence, and inference. Explain the classification and CVE recommendation, counterevidence, and any supported CWE mapping.}}

## Evidence and verification

| Evidence | Observation | Source / revision | Status |
| --- | --- | --- | --- |
| {{claim or test}} | {{what it supports or contradicts}} | {{link or path and commit}} | {{reported, inspected, reproduced, or unverified}} |

{{Record affected-version evidence without extrapolating unsupported ranges. State tests actually run, configuration, results, and missing verification. Explain whether reproduction exercises the affected application or only a model/unit test, and identify other potentially affected products or supported versions that remain unverified.}}

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
- Project/vendor rating: {{attributed or proposed rating and mapping basis, pending, or not applicable; distinct from the CVSS band}}

| Metric | Value | Rationale and evidence / assumption |
| --- | --- | --- |
| {{each required metric}} | {{selected value}} | {{specific supporting fact or uncertainty}} |

{{Distinguish provisional assessment from vendor scores. Explain differing scenarios and deployment risk separately. Remove the metric table if no assessment is supportable.}}

## Urgency and disclosure handling

- Exposure and exploit evidence: {{public disclosure, exploit availability, active exploitation evidence, deployment exposure, mitigations; distinguish unknown from absent}}
- Urgency: {{recommendation and evidence, separately from CVSS}}
- Embargo: {{current documented status, proposed handling, policy rationale, and unresolved decision; not applicable when appropriate}}
- Communication/disclosure dates: {{established dates and sources; clearly marked proposals or unknown; no assumed deadline}}

## Proposed tracker changes — draft, when applicable

{{Record metadata actually checked and distinguish issue types from labels. Omit this section when no tracker changes are relevant. If metadata is inaccessible, describe the intended transition and the verification needed without inventing names.}}

| Field / action | Current state | Proposed change | Rationale / prerequisite |
| --- | --- | --- | --- |
| {{type, label, assignment, closure, or handoff}} | {{observed state or unknown}} | {{specific verified value/action or pending verification}} | {{evidence and required decision/role}} |

## Next action and limitations

- Next responsible role/team: {{confirmed owner with source, proposed owner, or unknown}}
- Next action and blocking evidence: {{smallest concrete verification, decision, or security-team handoff}}
- Reporter communication: {{known acknowledgment/reply status and next established update date; proposed or unknown when appropriate}}

{{State limitations and actions not performed. For a security submission draft, state AI assistance and actual reproduction and human-review status.}}

## Reporter response — draft, when applicable

{{Acknowledge or explain the assessment and request focused evidence or describe the next step. Keep separate from the internal rationale, respect the recipient's access, and do not imply an unconfirmed fix, CVE, deadline, or team agreement. Omit when no reporter response is needed.}}

## Proposed comment — draft

{{Two to four short, natural sentences: conclusion, key reason, relevant link when useful, and next step. Match the audience and avoid exposing private details.}}
