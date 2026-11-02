# Review guidance and applicability

Use this map to select external guidance for the changed behavior. Read the relevant source or section, not the entire list on every review. The sources were checked on 2026-11-02; verify the version and applicability when relying on a specific requirement. These summaries are navigation aids, not copied standards or evidence of certification.

## Authority and scope

Keycloak's applicable repository policies govern contribution conventions, approvals, testing, and security handling. Protocol specifications and supported product contracts establish relevant behavior. External engineering guidance supplies review questions unless the project explicitly adopts it as a requirement. Explain conflicts rather than silently treating one authority as overriding an unrelated obligation.

For a specification finding, cite the exact version/section and explain the applicable role, profile, configuration, conditions, and normative strength. Distinguish a demonstrated violation from an advisory improvement. A project assessment, badge criterion, or tutorial does not establish that a particular PR is defective or that the project has adopted every recommendation.

## Source map

| Source | Use when reviewing | Scope and limits |
| --- | --- | --- |
| [Google: What to look for in a code review](https://google.github.io/eng-practices/review/reviewer/looking-for.html) | Design, functionality, complexity, tests, naming, documentation, and surrounding context. | General engineering guidance; use Keycloak's conventions for style and contribution requirements. |
| [CNCF: Reviewing Guide template](https://github.com/cncf/project-template/blob/main/REVIEWING.md) | Review process, constructive feedback, tests, documentation, breaking changes, and stability. | A template for projects to customize, not proof that Keycloak adopted its role or approval rules. |
| [Linux Foundation Release Engineering: Code Review](https://docs.releng.linuxfoundation.org/en/latest/best-practices.html#code-review) | Commit clarity, addressed feedback, dependency-license compatibility, tests, documentation, linting, and backward compatibility. | Release Engineering guidance; do not import its ordering, footer, or test conventions into Keycloak automatically. |
| [CNCF: Security self-assessment guidance](https://tag-security.cncf.io/community/assessments/guide/self-assessment/) | New actors, interactions, isolation, security goals/non-goals, and critical components. | Project-level design questions useful for feature threat modeling; not an independent audit or a mandatory assessment for every PR. |
| [OpenSSF: Concise Guide for Developing More Secure Software](https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software.html) | Dependency selection, negative tests, secrets, security tooling, and review before accepting changes. | Broader development/build/distribution guidance; select checks affected by this PR rather than auditing all repository settings. |
| [OWASP: Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html) | Changes to security controls, attack paths, trust boundaries, integrations, and security regressions. | Use the diff-based methodology for PRs; inspect surrounding paths as needed without automatically performing a whole-codebase audit. |
| [OWASP ASVS](https://asvs.owasp.org/) | Specific application security requirements relevant to the affected control. | Cite versioned requirement IDs and applicability. Using ASVS as guidance does not assert an assurance level or compliance certification. |
| [OAuth Security BCP: RFC 9700](https://www.rfc-editor.org/rfc/rfc9700.html) | OAuth security behavior and flows affected by the change. | Verify participant role and conditions; also consult the applicable primary OAuth/OIDC/SAML/WebAuthn specification or profile rather than applying OAuth requirements to every flow. |
| [Apache TVM: Code Reviews](https://tvm.apache.org/docs/contribute/code_review.html) | API design, maintainability, dependency restraint, consistency, and constructive discussion. | Practices from one open-source project; its domain-specific code and review conventions are not Keycloak policy. |
| [IBM: LLM code review using IBM Bob](https://www.ibm.com/think/tutorials/llm-code-review) | AI-assisted inspection of changed code, surrounding context, related patterns, and prioritized findings. | A product tutorial, not a universal IBM engineering standard or a requirement to use Bob. Validate tool-generated findings independently. |
| [Keycloak's CNCF-hosted self-assessment](https://tag-security.cncf.io/community/assessments/projects/keycloak/self-assessment/) | Historical design goals, non-goals, and security context. | Includes older deployment examples such as Keycloak 10.0.1. Verify claims against current, matching-version code/docs; do not treat it as a current security attestation. |

## Applying guidance to a finding

Explain the affected requirement or engineering concern and its concrete consequence, with code/test evidence. Record whether the basis is a protocol requirement, supported product contract, adopted project policy, or external recommendation. Prefer the most direct source; citing several checklists does not strengthen an unsupported claim.

Keep process gaps, code defects, and optional improvements distinct. Do not impose another project's reviewer counts, approval roles, branch strategy, formatting, release policy, or automated merging instructions. A skill's draft review does not satisfy independent human-review requirements. Preserve the main workflow's authorization and disclosure boundaries when a source describes actions such as posting, submitting, or merging.
