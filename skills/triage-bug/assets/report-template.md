# Bug triage: {{issue title}}

<!-- Content checklist: omit irrelevant fields, combine short sections, and use prose instead of tables for straightforward cases. -->

{{Lead with the recommended disposition, proposed priority or pending decision, confidence with its reason, and the immediate next step. Adapt the length to the case and omit irrelevant sections.}}

- Issue: {{canonical URL or supplied identity; current state}}
- Assessed: {{date; material source revisions/retrieval dates}}
- Scope: {{upstream/downstream distribution, version/build, component, feature maturity, relevant environment}}

## Finding and impact

{{Explain expected versus observed behavior with sources. Identify the affected capability/population, frequency, workaround, and operational impact. Distinguish reporter claims, observations, and inference; state root-cause uncertainty and relevant migration/configuration alternatives.}}

## Evidence and verification

| Claim or check | Observation | Source / revision | Evidence status |
| --- | --- | --- | --- |
| {{material claim or test}} | {{result and what it supports}} | {{link or path with revision}} | {{reported, inspected, reproduced, unverified}} |

{{Record reproduction steps or commands actually run, versions/configuration/results, and limits. State last working/first failing evidence without extrapolating unsupported version ranges. Identify the smallest missing check.}}

## Duplicates and existing fixes

Search coverage: {{actual sources/queries, open and closed reports/PRs, date, result limits and access gaps}}.

| Candidate | Relationship | Evidence and fix status |
| --- | --- | --- |
| {{canonical issue or PR link}} | {{confirmed duplicate, possible duplicate, related, distinct}} | {{trigger/configuration/version comparison; proposed, merged, backported, released, or unknown fix status}} |

{{Remove empty rows when no credible candidates exist. State no duplicate found within the searched sources, or that a search could not be performed.}}

## Priority and workflow decision

- Flowchart branch: {{documented behavior, population blocked, regression evidence; source links}}
- Proposed action and priority: {{verified action label and resulting priority, conditional outcomes, or pending}}
- Confidence: {{reason and remaining uncertainty; separate from impact and priority}}
- Current routing and proposed owner: {{verified area/team or proposed role; source}}
- Effects and conflicts: {{relevant bot comments, closure, label/milestone changes, aging, and policy/source/deployment uncertainty}}

{{Explain security routing or conditional backport consideration when relevant. Do not include confidential evidence in a public report or name unverified metadata.}}

## Next steps — proposed unless marked performed

| Order / actor | Action and reason | Expected effect | Completion condition |
| --- | --- | --- | --- |
| {{number; reporter, triager, maintainer, developer, security team}} | {{specific evidence request, routing, workflow action, or follow-up}} | {{concrete state or evidence change}} | {{observable result; prerequisite/authorization if needed}} |

{{Keep the table ordered and omit inapplicable steps. Identify when new evidence should trigger reassessment. Record actions actually performed and verified separately from proposals.}}

## Limitations

{{Missing evidence/access, checks not run, conflicting guidance, and decisions still pending. If this is a security-submission draft, state AI assistance and actual reproduction/human-review status.}}

## Public comment — draft

{{Two to four short, natural sentences: specific finding or uncertainty, key reason, useful link when needed, and focused next step. Avoid stock praise or unsupported claims. Keep action labels in the handoff unless a bot-triggering draft is explicitly requested; then append the verified trigger as the final line and explain its effects outside the copyable draft.}}
