# Feature and enhancement review

Use this reference for new capabilities and enhancements to existing behavior. Scale the depth to the change: a small configuration enhancement does not require a full architecture assessment. Retain the shared specification, correctness, compatibility, and finding-validation checks from the main workflow.

## Establish scope and acceptance

Read the issue, linked design proposal/discussion, documentation, and relevant maintainer decisions. Identify the intended users, problem, supported scenarios, acceptance criteria, and explicit exclusions. Check required design discussion or approval against current repository policy; absence of a particular document is not automatically a code defect.

Trace material requirements to implementation and tests. A concise requirement/evidence table can expose missing behavior without reproducing the entire specification. Distinguish agreed requirements, proposed requirements, and reviewer assumptions. Validate new behavior against applicable protocol profiles and existing contracts; an issue's requested behavior is not automatically correct.

Explain material ambiguities and the smallest clarification needed. Do not invent acceptance criteria, treat optional integrations as required, or demand future capabilities outside the agreed scope. An unavailable requirement source limits confidence but does not prove incompleteness. Keep technical readiness separate from whether maintainers have accepted the feature or its design.

## Assess design and implementation completeness

Check whether the design uses appropriate existing Keycloak APIs, SPIs, models, and extension points. Evaluate new public contracts, abstraction boundaries, dependency choices, and ownership/lifecycle of state. Explain why added complexity is necessary for the stated requirement, and identify concrete maintenance consequences of duplication or bypassing existing abstractions. Prefer established solutions where they meet the need; do not require speculative generalization.

Trace an intended user scenario end to end. Depending on the feature, check consistency across server behavior, REST representations, authorization, Admin/Account Console, CLI, configuration validation, storage, caches, import/export, and documentation. Only require surfaces the design actually supports. A server-only feature does not inherently require a new UI.

For new or expanded APIs and protocol flows, examine error contracts, defaults, pagination or bounds, idempotency where relevant, and interoperability with supported clients/providers. For UI changes, examine usability, accessibility, localization, and understandable feedback. Identify necessary conceptual and task-based documentation, rather than accepting inline comments as the only user guidance.

## Evaluate security and adoption

Identify new actors, entry points, data flows, permissions, sensitive data, external integrations, and trust boundaries. Check how legitimate access is authorized and how unauthorized or abusive use is constrained. New capabilities can require security design review without claiming an existing vulnerability; load the security reference as directed by the main workflow. Use the CNCF design questions and OWASP review methods from the source map where relevant.

Establish intended feature maturity and availability from the proposal and repository conventions. Where flags or optional configuration exist, check defaults, enabling/disabling, interaction with existing features, and behavior when disabled. Do not prescribe a feature flag for every enhancement. Verify that experimental/preview limitations and security assumptions are communicated accurately.

Review compatibility with supported deployments, persisted data, extensions, and protocol peers. Identify migration and supported rolling-upgrade implications, observability needs, and any documented rollback limitations. Check performance/resource behavior for the new usage pattern using realistic workloads; avoid unsubstantiated performance claims. Required operator actions should be described, not performed during review.

## Verify acceptance and regressions

Choose focused acceptance scenarios that demonstrate the promised capability and meaningful outcomes. Include relevant invalid-input, unauthorized-access, boundary, failure/recovery, and integration scenarios. For optional features, cover relevant enabled/disabled/default behavior and interactions. Follow Keycloak's existing test patterns and keep coverage proportional to the change.

Run new-feature tests on the reviewed head when feasible and verify that unaffected supported behavior still works. Use baseline comparisons where meaningful, but do not require new tests to compile or fail meaningfully against a base lacking the new API/schema. A compilation error on the base does not establish a regression or validate the new behavior. Tests should be capable of detecting an incorrect implementation, not merely mirror its branches or assert that a method was called.

Report implemented requirements, demonstrated gaps, unresolved scope, and verification limits. Apply fix-specific checks separately when a feature also repairs a bug or vulnerability. An unmet established requirement can be an actionable finding; a proposed future improvement or missing optional scenario should not become a merge blocker by assumption.
