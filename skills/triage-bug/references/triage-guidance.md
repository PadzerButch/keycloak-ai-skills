# Guidance and relevance

Use this source map for general practice questions or decisions not settled by project guidance. These are relevance tiers, not issue priorities. The sources are a mix of project rules, badge criteria, community advice, and vendor support policies; do not describe them as one formal standard or certify compliance from a triage report.

| Relevance | Source | Useful application and limit |
| --- | --- | --- |
| Essential | [Keycloak workflow](keycloak-workflow.md), including linked project documentation and security policy | Governs Keycloak disposition, priority, reporting, ownership, and intended tracker behavior. Check the applicable version and current policy. |
| High | [OpenSSF Best Practices criteria](https://www.bestpractices.dev/en/criteria/0), reporting and quality sections | Searchable reports and responses, acknowledgment, traceability, and testing. Badge requirements apply to that assessment program; do not import a response deadline into Keycloak bug handling. |
| High | [CNCF contributor FAQ](https://contribute.cncf.io/contributors/faq/) | Read project instructions, provide specific environment/error information, search existing reports, and collaborate respectfully. Its cross-project examples do not override Keycloak contribution rules. |
| High | [Ubuntu bug triage](https://ubuntu.com/project/docs/contributors/bug-triage/) | Assess report sufficiency, reproduce, check duplicates, route to the correct component, and cross-reference upstream/downstream reports. Do not copy Launchpad states or Ubuntu closure policies. |
| Supporting | [Linux Foundation open-source tooling guide](https://www.linuxfoundation.org/resources/open-source-guides/tools-managing-open-source-programs) | Use collaboration and tracking tools appropriate to the community. Program-management guidance is less specific than a project's triage flow. |
| Conditional: security | [Linux Foundation security reporting](https://www.linuxfoundation.org/security) | Use the affected project's vulnerability reporting route. LF affiliation does not make LF's infrastructure security address the Keycloak reporting channel. |
| Conditional: impact and communication | [IBM support guidance](https://www.ibm.com/support/pages/system/files/inline-files/IBM%20Support%20Executive%20Briefing%20Document%20%28April%29_0_0.pdf), [IBM case severity](https://www.ibm.com/support/pages/node/7271994) | Capture one problem, precise versions/reproduction, diagnostics, business impact, and agreed next steps. IBM support severity, contractual response times, and escalation channels apply to IBM cases. |
| Conditional: downstream support | [Red Hat support severity](https://access.redhat.com/support/policy/severity) | Describe operational interruption and changes in impact for an applicable Red Hat support case. Keep downstream support urgency separate from the upstream project's priority and release decisions. |
| Conditional: interoperability | [IETF RFCs](https://www.rfc-editor.org/), [OpenID specifications](https://openid.net/developers/specs/), [OASIS SAML specifications](https://docs.oasis-open.org/security/saml/v2.0/) | Verify a protocol claim against the applicable version, section, role, and enabled feature. A requirement for another role or optional profile does not establish a Keycloak defect. |

Consult only what changes the decision. Record source dates and distinguish documented requirements from recommendations or your interpretation. Do not require every organization to be cited in every issue report.

## Practices that improve the assessment

Keep technical impact, scheduling priority, and evidence confidence separate. A high-impact allegation may be uncertain; a confirmed defect may have low operational impact. Workarounds and affected populations influence urgency but need evidence. Document the facts that would change the recommendation.

Use a minimal reproducer against the actual relevant application/configuration, protect diagnostic data, and record version provenance. For intermittent behavior, define the test conditions and limits rather than inferring validity from a single run. Do not extrapolate an affected version range from one tested build.

Preserve the issue's history and distinguish symptoms from root causes. Link canonical reports and fixes, but keep regressions after fixes and distinct causes separate. Explain any closure so future reporters can tell whether their case is covered.

Ask focused questions and give a next actor and observable next step. Keep public comments specific and readable. Neither courteous wording nor a source citation compensates for invented reproduction, agreement, deadlines, or assignments.
