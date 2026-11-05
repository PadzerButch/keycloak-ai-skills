# Security fixes

Use this reference when correcting a security weakness or vulnerability, assessing a supplied CVE's applicability to a fix, or materially changing a security control. Read [security handling](security-handling.md) before using private evidence, choosing an audience, or preparing disclosure material. Consult the applicable security policy; do not expose unpublished findings or bypasses through public searches or outputs.

## Establish the guarantee

Identify the actor, privileges, attacker-controlled inputs, reachable entry points, protected assets, and trust boundary. Explain the security guarantee and the demonstrated or suspected confidentiality, integrity, or availability consequence. Trace caller and downstream protections before declaring an exploitable path. For hardening, state the property being strengthened and its assumptions even when no exploit is established.

Keep the security claim, advisory applicability, and fix effectiveness separate. A vulnerability can exist without a CVE; a CVE label or published severity does not prove that the target code is affected. If a CVE is supplied, verify its [authoritative record](https://www.cve.org/) or assigning vendor advisory against the component, root cause, prerequisites, and revision evidence. Do not infer applicability from similar symptoms or a shared weakness category. Reserved or inaccessible records may leave linkage unverified without blocking an independently established code fix. For dependency issues, establish use and reachability and verify the resolved dependency and shipped artifact when these determine the remedy.

## Remove the cause and check variants

Enforce the guarantee at the layer that owns it across relevant entry points and implementations. Trace ordering relative to side effects, mutation, cleanup, and failure handling. Check that rejected input cannot still change another realm's, client's, or user's state. Consider normalization, alternate encodings, configuration, persisted/cached state, concurrency, and resource bounds only where they could bypass or undermine that guarantee.

An outer filter or added check can be the correct fix when it completely enforces the owned boundary. It is incomplete when another supported route reaches the same defective operation. Explain why the chosen placement closes the cause, not just the reported input. Additional protective checks may support a complete fix, but must not conceal an unresolved root cause.

Use authorized local reproduction with synthetic identities and data. When feasible, demonstrate the violation on the affected application and its prevention after the fix, with a positive control for legitimate use. Verify that rejection comes from the intended control and occurs before forbidden side effects. Tests of copied or simplified functions are supporting evidence, not proof of a Keycloak exploit or remediation.

## Check operational completeness

Assess whether previously issued tokens, online/offline sessions, caches, credentials, or persisted records need invalidation, rotation, or migration to restore the guarantee. Document necessary operator action without treating an operator workaround as the implementation. Check relevant mixed-version behavior; code installation alone may not remove established exposure in existing state.

For requested backports, inspect and validate each target's implementation and test path. A clean cherry-pick does not establish effectiveness. Report only inspected/tested versions and configurations; do not extrapolate affected or fixed ranges, upstream/downstream equivalence, or released artifact status.

Deliver evidence of the corrected property, legitimate-use coverage, relevant bypass coverage, and residual uncertainty to the authorized audience. Keep unrelated findings separate. Do not manufacture exploitability, CVE assignment, severity scores, or a claim of complete security; separate security triage or disclosure work remains optional unless requested.
