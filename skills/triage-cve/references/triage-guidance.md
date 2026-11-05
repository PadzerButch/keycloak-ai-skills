# Triage guidance and applicability

Use this reference when general triage practice is requested or project guidance leaves a decision unresolved. These sources inform the assessment; they do not replace the affected project's policy or applicable vendor process. Record source dates and distinguish recommendations from project requirements. Consult only the sources relevant to the decision.

| Source | Useful guidance for this skill | Applicability |
| --- | --- | --- |
| [OpenSSF maintainer guide](https://oss-vulnerability-guide.openssf.org/maintainer-guide.html) | Distinguish vulnerabilities from bugs and hardening, document the rationale, maintain reporter communication, identify coordination ownership, and discuss disclosure expectations. | General open-source response guidance. Its example response times and disclosure practices are not automatically Keycloak requirements. |
| [CNCF incident-response template](https://tag-security.cncf.io/community/resources/project-resources/templates/incident-response/) | Assess component, privileges, interaction, impact, and exploit availability; reproduce the report or request clarification; identify the reporter's next update. | Useful triage and communication prompts. Use the project's actual CVE-request route, scoring requirement, and disclosure process. |
| [CNCF guidance on AI-assisted vulnerability discovery and triage](https://www.cncf.io/blog/2026/04/16/the-ai-driven-shift-in-vulnerability-discovery-what-maintainers-and-bug-finders-need-to-know/) | Check the report against a threat model and triage criteria, then validate exploitation against the actual application. A demonstration against copied or simplified code may not establish a product vulnerability. | Guidance for evidence quality. State gaps or threat-model disagreements explicitly; an incomplete report is not proof that the product is safe. |
| [Linux Foundation security guidance](https://www.linuxfoundation.org/security) | Follow the affected project's reporting process and prepare to receive reports; the foundation recommends the OpenSSF maintainer guide. | Foundation affiliation does not substitute for a project's reporting channel. |
| [FIRST PSIRT Services Framework 1.1, service area 3](https://www.first.org/standards/frameworks/psirts/psirt_services_framework_v1-1#service-area-3-vulnerability-triage-and-analysis) | Define qualification criteria, reproduce safely, protect evidence, and investigate affected products and variants. | A general framework; identify relevant supported products without assuming an untested version range. |
| [IBM vulnerability management](https://www.ibm.com/trust/security-vulnerability-management) | A risk-based lifecycle covering discovery, triage, remediation, and disclosure, coordinated between PSIRT and product teams and informed by FIRST. | An enterprise example. IBM's intake and operational process apply to IBM products; they do not establish Keycloak's workflow. |

## Applying the guidance

Explain which documented guarantee or security boundary is violated, using attacker capabilities and deployment assumptions. Separate intentional design, a request for stronger defenses, and an exploitable defect; if the threat model is disputed, explain the disagreement rather than treating design intent as conclusive.

Keep technical severity separate from handling urgency. Record public disclosure, exploit availability, evidence of active exploitation, exposure, and mitigations with sources. A proof of concept is not evidence of exploitation in the wild, and a missing exploit report is not proof that exploitation is absent.

Make the next step actionable: identify the responsible role, missing evidence, communication status, and any established next update. Mark proposed dates and assignments as proposals. Draft communications for the intended audience; neither these guides nor a triage request authorize contacting reporters or publishing findings.
