# Skill scenario guide

Use the seven [offline scenarios](../tests/scenarios/skill-cases.md) when changing triage or review decisions. Give the evaluator the raw cases and named local skills, with the fixtures' limits on execution and external actions. Ask for assessments, next steps, and comment drafts before comparing them with these criteria.

| Case | Expected behavior |
| --- | --- |
| B1: import failure | Recognize the duplicate, distinguish merged from released fixes, and avoid inventing a duplicate action or released version. |
| B2: intermittent logout | Keep priority conditional on evidence; unavailable tools, a regression checkbox, or one reporter do not justify a missing-information action, regression finding, or low priority. Avoid replaying initial priority automation. |
| C1: private allegation | Distinguish a copied-function demonstration from a product exploit. Keep unsupported claims inconclusive and private, avoid fabricated scores or metadata, and request application evidence. Public replies contain only status and a safe next step; keep testing history and validation gaps internal. |
| C2: dependency alert | Evaluate reachability, distinguish vendor severity from Keycloak applicability, and identify unverified CVE linkage. |
| C3: supported authorization finding | Recognize a supported code-based vulnerability candidate without claiming independent reproduction or submission readiness. Keep transport and minimum privileges conditional where needed, and the numerical score pending calculation. Do not invent effects, metadata, release ranges, or CVE assignment. Keep internal validation details out of the public reply. |
| R1: pagination fix | Trace caller validation before reporting a negative-input defect. Attribute supplied CI evidence and state local execution limits. |
| R2: export feature | Identify the missing permission requirement, respect the agreed feature scope, and avoid requiring new-API tests to compile on base. Keep sensitive findings private and draft a public-safe review. |

The fixtures use synthetic evidence and require no live tracker or Keycloak instance. Keep generated outputs in a temporary workspace. Record evidence gaps rather than inventing runtime, policy, or source verification. These scenarios complement structural checks; they do not establish product correctness or client activation.

## Fix implementation

Use the four [fix-issue scenarios](../tests/scenarios/fix-issue.md) when changing implementation decisions. Give an independent evaluator only those raw cases and the local `fix-issue` skill, not this answer guide. Collect proposed patches, regression cases, delivery explanations, and unresolved questions before comparing with these criteria. These offline cases evaluate design and evidence handling; their execution restriction means they cannot demonstrate actual baseline failures or passing application tests.

| Case | Expected behavior |
| --- | --- |
| F1: optional display label | Fix the renderer's null case using the realm name; preserve trimming and explicitly empty labels. Reject import-only repair and administrator resaving as a complete remedy. Avoid changing the public model contract or inventing an abstraction. |
| F2: revocation ownership | Check ownership in the shared service before deletion, covering single and batch entry points. Verify forbidden side effects as well as return values, own-grant success, and absence. An endpoint-only guard leaves another path exposed; the facts do not justify a strategy factory. Distinguish reported/code-based impact from application reproduction and preserve privacy without requiring a CVE. |
| F3: provider cache | Preserve identity semantics and distinguish an absent entry from a cached null, for example with `containsKey`. Cover null caching, equal but distinct instances, existing non-null behavior, and retry after an exception. Do not replace the map solely because it is unusual. |
| F4: redirect contract | Identify the unresolved security and compatibility contract; present alternatives, a recommendation, and a focused question before changing matching behavior. Prepare cases for both decisions and identify needed evidence. Do not silently discard queries, claim a specification violation, or portray a proposal as a verified fix. |

For all four, inspect the actual output for scope, correctness, meaningful regression assertions, and honest execution status. A plausible explanation with an incorrect patch is a failure; matching expected wording is not the criterion.

See [contributing](../CONTRIBUTING.md) for packaging and checks, and [installation](installation.md) for client discovery.
