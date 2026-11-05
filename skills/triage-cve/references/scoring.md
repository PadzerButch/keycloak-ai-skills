# CVSS assessment

Use the selected version's official definitions and calculator:

- [CVSS v4.0 specification](https://www.first.org/cvss/v4.0/specification-document), [user guide](https://www.first.org/cvss/v4.0/user-guide), and [calculator](https://www.first.org/cvss/calculator/4.0).
- [CVSS v3.1 specification](https://www.first.org/cvss/v3.1/specification-document) and [calculator](https://www.first.org/cvss/calculator/3.1).

Assess one coherent attack scenario at a time. Name the vulnerable system, attacker starting privileges, required user action, configuration, and resulting impact. Do not combine incompatible assumptions to maximize severity. CVSS expresses technical severity; explain deployment exposure and remediation priority separately.

Record why the selected CVSS version applies. Verify the applicable policy before applying score-based handling rules. Where a requirement specifies only CVSS v3, use v3.1 and state that interpretation unless a more specific requirement is available. Do not apply a v3 threshold to a v4 score or translate scores between versions. If a user also requests a different version, keep the assessments distinct.

Keep the CVSS severity band, Product Security's qualitative rating, and the repository's severity field separate. Propose a mapping only when supported by the applicable policy or an authoritative assessment; otherwise mark the project rating pending. A numerical score does not establish embargo status, CVE eligibility, or permission to publish.

For v4.0, justify each Base metric: AV, AC, AT, PR, UI, VC, VI, VA, SC, SI, and SA. Distinguish impacts to the vulnerable system from subsequent systems. Label a Base-only assessment CVSS-B; identify any additional Threat or Environmental metrics used. Do not assume active exploitation or deployment-specific conditions without evidence.

For v3.1, justify AV, AC, PR, UI, S, C, I, and A. Scope depends on security authority boundaries, not merely a different process or host. Keep v3.1 Scope and v4.0 subsequent-system impacts distinct; do not mechanically translate vectors between versions.

Keycloak scenarios need careful evidence about privileges: an ordinary authenticated user, a realm administrator, and a server administrator have different powers. Assess what the attacker must possess before exploiting the flaw, rather than the privileges they obtain afterward. Explain whether impact stays within one account, client, or realm or reaches other realms or services; do not presume that authentication or administrator involvement rules out a vulnerability.

Calculate using the official calculator or a trustworthy implementation of the selected specification, recording the tool/version or calculator link and the exact vector evaluated. Verify the numeric result and severity band against that vector. Opening a calculator page without obtaining its calculated result is not verification. Do not estimate a score mentally or silently reuse another issue's score.

If calculation is unavailable, report the justified vector and “numeric score pending calculation.” If evidence leaves metrics uncertain, identify them and explain how to resolve them. Use conditional vectors and separately calculated scores only for plausible, clearly described scenarios; do not fill missing impact with maximum values. A published score may be quoted with its source, version, vector when available, and attribution, but must not be presented as your verified calculation.

For each selected metric, include its value, a short rationale, and the supporting evidence or explicit assumption. Keep source-authority disagreements visible. An official advisory's score and a local deployment assessment can differ; explain the reason instead of choosing whichever is higher.
