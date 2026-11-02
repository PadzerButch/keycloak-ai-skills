# Security triage handoff

Use this reference when preparing tracker recommendations, security-team coordination, or a CVE-request draft. It describes a proposed handoff; it does not authorize tracker changes, external messages, CVE requests, or publication.

## Establish the applicable process

Use the current [Keycloak security policy](https://www.keycloak.org/security), applicable repository `SECURITY.md`, and any handling requirements supplied by an authorized maintainer. Record the policy revision or retrieval date. Keep confidential evidence out of shared skill files and public artifacts.

Read the issue's current type, labels, assignments, and relevant discussion. Verify available repository labels and organization issue types before proposing exact values. Issue types and labels are different metadata; do not treat them as interchangeable or request creating missing values. Record conflicts with current metadata or policy for the responsible security team to resolve.

If metadata or handling requirements are inaccessible, continue the technical assessment. State the duplicate-search and workflow-verification gaps, describe the handoff provisionally, and identify what an authorized maintainer must verify. Do not infer unavailable labels, assignments, or decisions from another tracker.

## Map the assessment to a proposed handoff

| Assessment | Proposed next step |
| --- | --- |
| Confirmed duplicate | Identify the canonical issue, explain the matching root cause, and propose the justified duplicate disposition and closure. Respect the reporter's access when drafting a reply. |
| Inconclusive or possible duplicate | Retain the need for triage. Request the smallest missing reproduction, version, impact, or duplicate evidence; do not reject or close solely because verification is incomplete. |
| Supported vulnerability / CVE candidate | Propose the vulnerability classification and justified project severity, assess disclosure restrictions, and record whether team agreement exists. Hand off to the responsible security team or CNA after applicable prerequisites are satisfied. Candidate status is not an assigned CVE. |
| Weakness/hardening or ordinary bug | Propose the matching classification and explain the security assessment. Evaluate publication under the applicable policy; route any proposed public transfer through the responsible security team. |
| Question, expected behavior, or configuration issue | Explain the conclusion and propose the applicable support disposition. Do not equate a question with a rejected vulnerability or dismiss a violation of documented guarantees. |
| Dependency advisory not applicable in the assessed configuration | Record the absent or unreachable prerequisite and inspected build/configuration. Propose maintainer verification of the advisory match and shipped artifacts before any closure; do not generalize to uninspected deployments. |

Propose removing a triage marker only when the required evidence and decisions are complete. Keep assessment changes distinct from bot-managed CVE-request/assignment state and from fix or release readiness.

## Disclosure, ownership, and downstream work

Evaluate personal-data exposure, risk to existing installations, and applicable embargo criteria. Verify the required CVSS version before applying any score-based rule; use the [scoring guidance](scoring.md). A low score alone does not authorize disclosure. Preserve established restrictions while the handling decision is unresolved. For accidental public disclosure, follow the published escalation route without repeating confidential details.

Route proposed public transfers through the responsible security team with appropriate sanitization and reporter acknowledgment. Check the intended audience and permitted reproducer content before drafting a public issue. General disclosure examples do not override the applicable project policy.

Identify the proposed fixing team and evidence for affected supported release streams. Mark unverified streams, release targets, and ownership pending. Fix preparation, review, testing, backports, and release coordination are downstream work; triage does not establish that they have happened.

## Draft the operational result

Include the proposed metadata changes, rationale and prerequisites, next responsible role, unresolved evidence, and established or explicitly proposed communication dates. Keep internal rationale separate from reporter-response drafts and respect each recipient's access. For a requested CVE submission, verify the required content and destination; do not invent a subject, command, or recipient.

Bot-triggering comments can send external messages or request CVEs. Include them only when an operational draft is requested and explain their effects outside the copyable comment. Posting still requires authorization for the action and destination. Honor authorization already given within its stated scope.
