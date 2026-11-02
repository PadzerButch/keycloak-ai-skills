# Security review

Use this reference for hardening and vulnerability reviews, new or materially changed security controls/trust boundaries, or a credible security concern found by the shared workflow. Keep the analysis tied to the changed security property and, for fixes, its root cause. Apply remediation-specific sections only when a change claims to repair an existing weakness or vulnerability.

## Establish the security scope

Record the distribution (upstream Keycloak or downstream build), exact reviewed/tested revision and affected baseline where applicable, feature maturity, relevant configuration, and disclosure status. Read the target repository's `SECURITY.md` and the current [Keycloak security policy](https://www.keycloak.org/security); explain material differences. Apply its handling for experimental features, dependency reports, reproduction evidence, and AI-assisted reporting rather than assuming all security concerns follow the same public workflow.

Define the potential attacker, controlled inputs, required privileges, reachable entry point, assets, and security boundary. For a finding, establish the concrete confidentiality, integrity, or availability consequence. State the intended guarantee, such as “a user authorized in realm A cannot read realm B's resources.” Assess documented guarantees and defaults as well as explicit protocol requirements. Use the [source map](review-guidance.md) to select relevant design and code-review guidance.

For alleged existing weaknesses or vulnerabilities, keep these conclusions separate:

- **Security claim:** established vulnerability, conditional weakness, defense-in-depth improvement, unsupported claim, or unknown. Absence of an exploit demonstration does not prove safety or make useful hardening invalid. A vulnerability may also be a bug caused by a weakness; these labels are not disjoint taxonomies.
- **Advisory applicability:** verified match, mismatch, partial match, or unknown. Check a supplied CVE against its [authoritative record](https://www.cve.org/) or assigning vendor advisory, including reserved/published/rejected status, root cause, component, prerequisites, and version evidence. A reserved record may not provide enough public information to confirm a match. Similar symptoms or a shared CWE are insufficient. A dependency version alert alone does not establish reachability or impact in Keycloak.
- **Fix effectiveness:** supported within assessed scope, partial, ineffective, or insufficient evidence. CVE assignment and a vendor score do not establish patch correctness.

Map a CWE only when the root cause supports the specific entry; use [MITRE's root-cause mapping guidance](https://cwe.mitre.org/documents/cwe_usage/guidance.html). Do not assign a CVE, promise eligibility, or manufacture a severity score. A separate triage or scoring task can be recommended when needed, but is not a prerequisite for reviewing the change.

## Review new or expanded functionality

For features, assess whether the design and implementation enforce the intended security guarantees before any vulnerability is suspected. Trace new actors, sensitive data flows, permissions, external integrations, and trust boundaries. Examine authorization placement, defaults, validation, failure behavior, resource bounds, and relevant enabled/disabled behavior. Explain deployment assumptions and who controls security-sensitive configuration.

Use focused legitimate-use and abuse scenarios to assess those controls. A new feature need not have an exploitable predecessor, a CVE, or an advisory. Record the guarantees assessed, evidence, design assumptions, and unresolved questions; do not force it into a remediation classification. If a defect is discovered, apply the main finding-validation rules and distinguish a newly introduced vulnerability from a pre-existing issue.

## Verify the security effect

Use this section for vulnerability fixes and hardening of existing behavior.

For an alleged vulnerability, inspect the reproducer and, when feasible, demonstrate the security violation on an affected revision and its prevention on the patched revision in an authorized, isolated environment. Establish why the patched attempt fails: the intended control must prevent the violation, rather than a broken setup or unrelated failure hiding it. Retain a positive control showing that legitimate operations still work. If reproduction is unavailable, distinguish the code-path argument from executed evidence and state the smallest missing verification.

For hardening, show which property is strengthened, its before/after behavior, and the assumptions and residual exposure. Do not force an exploit or a CVSS score into a review that has no established vulnerability.

Determine whether the patch removes the root cause, closes only one attack path, or adds a compensating control. Explain what is actually prevented and whether the patch meets its stated claim. Blocking the original reproducer is necessary evidence when it is valid, but does not alone establish completeness.

## Examine controls and relevant bypasses

Trace alternate entry points and implementations enforcing the same guarantee or sharing a defect's root cause. Consider normalization/encoding, malformed or duplicate inputs, configuration differences, errors and fail-open behavior, concurrency, and persisted/cached state only where they affect that guarantee. Examine existing protections before claiming exploitability.

Select Keycloak-specific checks according to the affected flow:

- **Authorization and isolation:** administrative permissions, delegated administration, role/scope checks, cross-realm/client access, and user ownership checks.
- **Tokens and protocols:** signatures and allowed algorithms, issuer/audience, expiry and replay, client/session binding, redirect URI validation, state/nonce/PKCE, logout/revocation, and refresh-token handling. Verify the applicable OAuth/OIDC/SAML participant role and profile instead of applying requirements indiscriminately.
- **Identity lifecycle:** brokering and account linking, federation/LDAP, credential recovery, MFA, and required actions.
- **Input and output boundaries:** injection, XSS, CSRF, SSRF, unsafe parsing, path traversal, and credentials/tokens/personal data in logs, errors, or responses.
- **Availability:** attacker-controlled expensive work, query amplification, unbounded allocation, contention, and resource cleanup, with realistic prerequisites and workload.

Use the specification applicability rules in the main workflow. Distinguish a demonstrated bypass from a plausible but unverified variant. Keep unrelated weaknesses separate from conclusions about this change.

## Check rollout and backports

For each claimed target or fixed branch/configuration in scope, verify the relevant implementation and tests independently. A clean cherry-pick does not prove effectiveness. Check changed dependencies and build/distribution artifacts when they determine whether the new or patched code ships; separate code review from verification of a released artifact.

Assess whether previously issued tokens, active/offline sessions, caches, credentials, or persisted records require invalidation, rotation, migration, or other remediation. Identify any necessary operator action without performing it. Evaluate supported mixed-version/rolling-upgrade behavior and document temporary exposure if established.

Record versions and configurations actually inspected or tested; do not extrapolate complete affected/fixed ranges from a single release. Explain whether upstream conclusions apply to a downstream distribution rather than assuming equivalence.

## Report and disclosure

For features, report security guarantees and control evidence, assumptions, and unresolved design questions. For hardening or vulnerability fixes, include separate conclusions for the security claim, advisory applicability, and fix effectiveness, with counterevidence, residual risks, remediation, and confidence. Omit inapplicable advisory/remediation fields rather than implying that every feature fixes a vulnerability. Missing CVE assignment must not reduce the depth of vulnerability review. Keep CVSS assessment separate; attribute any quoted published score and do not present it as a fresh calculation.

Keep private report content and unpublished bypass details out of public searches and draft comments, even when the original advisory is public. Use authorized private sources or non-sensitive public search terms. A public fix PR does not authorize disclosure of a newly found vulnerability. Do not submit reports or request assignment as part of this skill. If a separate security-submission draft is requested, follow the current project policy, disclose AI assistance, and state reproduction and human-review status accurately.
