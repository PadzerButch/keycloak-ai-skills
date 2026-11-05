# Offline skill scenarios

These synthetic records exercise the written workflows without a live tracker or Keycloak instance. Use the named skill and its relevant local resources to produce an assessment and comment for each case. Do not browse, execute application code, or mutate trackers. Treat the supplied records as a frozen evidence bundle; identify checks that would require live access. `example.invalid` links and revision IDs are synthetic.

## B1 — triage-bug: import failure

Request: Triage https://example.invalid/keycloak/issues/101 and draft a short public comment and next steps.

Issue snapshot: open, `kind/bug`, `status/triage`. Upstream stable feature, version 30.0.1. Import fails when an optional display name is absent. The reporter provides a minimal realm JSON, exact startup command, and log output. They ran the same input and configuration on 29.0.5 successfully. A maintainer comment confirms the failure on 30.0.1. Version-matched documentation says the field is optional. Release currency is not available offline. No team metadata is supplied.

Supplied search log: public issues and PRs, both open and closed, queries `realm import optional displayName` and `import missing displayName`, retrieved 2026-11-03; two results, no cap reached. Issue 88 describes this same input and version; the linked PR 89 was merged to main yesterday, adds the absent-field guard, and has a regression test. No backport or release evidence is supplied. Issue 88 remains open. The comment draft is not authorized for posting.

## B2 — triage-bug: intermittent logout

Request: Triage https://example.invalid/keycloak/issues/102, propose priority, and draft a public comment.

Issue snapshot: open bug, already `priority/normal`; upstream version 30.0.1, two-node cluster. Once every few days, some sessions survive logout until expiry. Reporter supplies redacted node logs, topology, browser version, realm settings, and a repeatable workload, but the precise interleaving is unknown. Reporter checked the regression box; no comparable earlier-version run exists. The agent has no runtime and no search access. The reporter is the only participant; affected population is unknown. No evidence of unauthorized cross-account access is provided. Request is for drafts only.

## C1 — triage-cve: private cross-realm allegation

Request: Assess the supplied private Keycloak report, draft an internal handoff and a public-safe reply.

Private report snapshot: stable upstream feature, version 30.0.1. A realm administrator in realm A claims to list realm B's account identifiers by replacing a realm key. The only demonstration is a Python copy of a filtering function; it does not call Keycloak. Entry-point authentication and caller-side authorization code are not supplied. The report has an internal URL and an unpublished candidate endpoint; neither is approved for public disclosure. Detailed handling requirements, labels, issue types, duplicate-search sources, public search, calculator, and runtime are inaccessible. No CVE record is supplied. A public source bundle contains only the general security policy themes: protect undisclosed vulnerabilities, check feature maturity, validate AI-assisted reports before submission, disclose AI use. No instruction to contact anyone or submit a report is given.

## C2 — triage-cve: dependency alert

Request: Assess a public dependency-CVE issue for Keycloak relevance and draft a comment.

Issue snapshot: dependency version is present in the upstream distribution. The assigning vendor's supplied advisory says the flaw requires the library's optional XML adapter. A supplied call graph and build artifact inventory at revision `synthetic-head-c2` show Keycloak uses the library's JSON reader and excludes the XML adapter; no alternative adapter loading path appears in the inspected code. Runtime verification is unavailable. The advisory supplies a published CVSS v3.1 score of 8.1, but its vector and authoritative CVE record were not included. The issue title's CVE identifier is unverified. Public search is unavailable. The supplied policy snapshot routes known third-party CVEs through public issues. No closure is authorized.

## C3 — triage-cve: supported authorization finding

Request: Assess this unpublished report, draft an internal handoff and a public-safe reply, and assess CVSS v4.0 if supportable. No external actions are authorized.

Revision `triage-positive-1` is synthetic and the feature is supported and stable. The supplied contract limits a realm-A administrator to realm A. The complete supplied routing and implementation accept an authenticated realm-A administrator with `view-users` permission in A and call `listUsers(request.realmId)` with a caller-controlled realm ID. There is no realm-membership or realm-specific permission check anywhere on this path; `listUsers` only selects records matching the passed realm ID. A supplied application request/response transcript reports retrieval of realm-B email addresses. This transcript has not been independently reproduced. No integrity, availability, or subsequent-system effect is supplied. The endpoint's transport and the credential's powers beyond the specified read permission are not stated.

No advisory, CVE record, runtime, searches, calculator, live policy, or tracker metadata is available. The frozen public policy summary requires confidential handling of unpublished findings, verified reproduction and human review before submission, and disclosure of AI assistance. It supplies no deadlines or severity mapping. All paths, revision IDs, and identities are synthetic. Keep any testing and validation history in the internal assessment.

## R1 — review-pr: pagination fix

Request: Review the supplied fix and draft a review; do not implement changes.

Revision snapshot: repository Keycloak, target main, base and merge base `synthetic-base-r1`, head `synthetic-head-r1`; no live PR access. Established contract: page size is an integer in [1,100], oversized positive requests are clamped, negative/zero requests are rejected. Original bug: a large positive request bypasses the cap. Diff in `PageSize.java` line 12: `return requested;` becomes `return Math.min(requested, 100);`. Complete supplied call chain: the only caller `ListResource.list` first throws BadRequest when `requested < 1`, then calls this helper. The helper is package-private and has no other callers. Existing tests cover zero and negative rejection; a new integration test asserts 500 returns 100 results. CI at the supplied head passed those tests. Local execution is unavailable. The author asks if the helper also needs its own negative-input check.

## R2 — review-pr: new export permission

Request: Review this feature using the supplied patch and agreed requirements. Draft a public-safe review and private technical finding if needed.

Revision snapshot: Keycloak, target main, base and merge base `synthetic-base-r2`, head `synthetic-head-r2`. Agreed requirements: add an admin REST export endpoint restricted to `view-users`; a UI is explicitly out of scope. The new class `ExportResource.java` lines 30–34 is the complete handler:

```java
@GET
public List<Account> export() {
    return accounts.findAll(realm);
}
```

Supplied routing context authenticates a realm administrator but performs no permission check. `accounts.findAll` only filters by realm; no downstream guard exists. A normal account-management administrator can authenticate without `view-users`. Neighbouring endpoints call `auth.users().requireView()` before listing accounts. New test uses a full realm administrator and checks only status 200. No runtime or CI results are available. The endpoint is new on this branch; applying its test on base fails to compile. No advisory or CVE is supplied. The PR is public, but newly discovered security details have no established disclosure status.
