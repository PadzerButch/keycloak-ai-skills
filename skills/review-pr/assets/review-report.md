# PR review: {{title}}

- Change: {{PR link or supplied patch identity}}
- Reviewed: {{date; repository, target branch, base SHA, merge-base SHA, head SHA; unavailable fields}}
- Scope and mode: {{bug / feature / hardening / vulnerability; selection rationale and uncertainty; distribution, version, configuration}}
- Audience and disclosure: {{intended audience; public/private/unknown; report handling}}

## Findings

{{List actionable findings in severity order. If none are established, say so within the assessed scope. Keep private technical findings out of public output.}}

### {{severity}} — {{short finding title}}

- Location: {{file and smallest useful line range at the reviewed revision; permalink when available}}
- Relationship to PR: {{introduced/exposed defect, incomplete fix, or unmet established feature requirement; connection to changed code}}
- Trigger and behavior: {{inputs/prerequisites; expected versus actual behavior}}
- Impact: {{concrete consequence and severity rationale}}
- Evidence and confidence: {{test result or complete code-path argument; counterevidence, assumptions, and uncertainty}}
- Correction and coverage: {{minimal correction direction and meaningful regression test}}

{{Repeat only for distinct findings. Keep unrelated pre-existing issues separate.}}

## Change intent, requirements, and specification checks

{{Explain the intended behavior, validated requirements, and whether the change meets them. For fixes, include the reported failure and root cause. For features/enhancements, identify the user problem, acceptance criteria, design rationale, and agreed exclusions. Distinguish observations, deductions, and author claims.}}

| Feature requirement / source — when applicable | Implementation and acceptance evidence | Status / gap |
| --- | --- | --- |
| {{established requirement and issue/design reference}} | {{code and meaningful test result, or unverified}} | {{met, unmet, or unresolved; reason}} |

{{Use the requirement table for material feature criteria when helpful; omit for changes that do not need it. Keep inferred scope and missing design/product acceptance under open questions.}}

| Source / version / section | Applicability and required behavior | Observed behavior / evidence | Assessment |
| --- | --- | --- | --- |
| {{primary source or contract}} | {{role, flow, configuration, conditions, normative strength}} | {{code/test reference}} | {{compliant, violation, permitted choice, or unresolved; reason}} |

{{Include relevant checks only; explain source conflicts or missing evidence. Remove the table when no specification claim is relevant.}}

## Security assessment — when applicable

- Design and controls: {{for new/expanded functionality: guarantees, changed actors/trust boundaries, control evidence, assumptions, and unresolved questions}}

{{Use the following remediation fields only for relevant hardening or vulnerability claims. Omit inapplicable fields.}}

- Security claim: {{established vulnerability / conditional weakness / defense-in-depth / unsupported / unknown; evidence}}
- Intended guarantee: {{attacker, prerequisites, assets, boundary, and impact}}
- Advisory applicability: {{verified record/advisory and status, mismatch, partial match, unknown, or no supplied advisory}}
- Fix effectiveness: {{supported within assessed scope / partial / ineffective / insufficient evidence; root cause versus compensating control}}
- Bypasses and residual exposure: {{verified outcomes, untested variants, assumptions, counterevidence}}
- Rollout and backports: {{versions/configurations verified; remaining exposure and required operator action}}

## Validation

| Check / command | Revision and configuration | Actual result | Limitations |
| --- | --- | --- | --- |
| {{test, reproduction, CI job, or inspection}} | {{base/head SHA and relevant setup}} | {{passed, failed, inspected, skipped, or not run}} | {{what it establishes and what it does not}} |

{{Distinguish tests executed locally, observed CI results, code inspection, and proposed coverage. For fixes, include before/after and legitimate-use results where relevant. For features, include acceptance and preservation-of-existing-behavior results without requiring new APIs/tests to exist on the base.}}

## Gaps and other observations

{{Separate open questions, missing tests/validation, contribution-policy gaps, unrelated pre-existing problems, and optional improvements. For each material gap, state the smallest verification or action needed. Omit empty categories and speculative findings.}}

## Recommendation

{{ready / changes required / insufficient evidence, with reasons tied to findings and material gaps. State reviewed scope, whether the change meets its requirements (and the original problem appears fully fixed when applicable), and any head changes since inspection. Separate technical readiness from unresolved product/design acceptance. Do not claim complete security.}}

## Proposed review — draft only

{{A concise, natural comment with the conclusion, strongest evidence or actionable concern, and next step. Match the audience. Exclude private identifiers/links and unpublished attack details from public drafts; when disclosure is uncertain, use minimal public-safe wording.}}
