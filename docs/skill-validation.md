# Triage and review scenario guide

Use the six [offline scenarios](../tests/scenarios/skill-cases.md) when changing triage or review decisions. Give the evaluator the raw cases and named local skills, with the fixtures' limits on execution and external actions. Ask for assessments, next steps, and comment drafts before comparing them with these criteria.

| Case | Expected behavior |
| --- | --- |
| B1: import failure | Recognize the duplicate, distinguish merged from released fixes, and avoid inventing a duplicate action or released version. |
| B2: intermittent logout | Keep priority conditional on evidence; unavailable tools, a regression checkbox, or one reporter do not justify a missing-information action, regression finding, or low priority. Avoid replaying initial priority automation. |
| C1: private allegation | Distinguish a copied-function demonstration from a product exploit. Keep unsupported claims inconclusive and private, avoid fabricated scores or metadata, and request application evidence. |
| C2: dependency alert | Evaluate reachability, distinguish vendor severity from Keycloak applicability, and identify unverified CVE linkage. |
| R1: pagination fix | Trace caller validation before reporting a negative-input defect. Attribute supplied CI evidence and state local execution limits. |
| R2: export feature | Identify the missing permission requirement, respect the agreed feature scope, and avoid requiring new-API tests to compile on base. Keep sensitive findings private and draft a public-safe review. |

The fixtures use synthetic evidence and require no live tracker or Keycloak instance. Keep generated outputs in a temporary workspace. Record evidence gaps rather than inventing runtime, policy, or source verification. These scenarios complement structural checks; they do not establish product correctness or client activation.

See [client compatibility](compatibility.md) for packaging and discovery details.
