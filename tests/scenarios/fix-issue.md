# Offline fix-issue scenarios

These frozen synthetic records exercise implementation decisions without a Keycloak checkout or runtime. For each case, use the named local `fix-issue` skill and relevant resources. Supply a proposed patch against the shown code when the evidence supports one, meaningful regression cases, and a concise delivery explanation. If a decision is missing, state the question and continue work that does not depend on it. Do not browse, execute application code, contact anyone, or mutate a tracker. Write evaluation outputs only to an isolated temporary workspace. Do not claim these fixtures establish a real Keycloak defect or successful runtime validation. Paths and revision IDs are synthetic; the code excerpts contain the complete relevant logic.

## F1 — optional display label

Request: Fix the missing-display-label crash on revision `synthetic-f1` and preserve supported labels.

Contract at this revision: a realm's display label may be null. In that case the renderer uses its non-null realm name from `RealmView.getName()`. Non-null labels are trimmed. An explicitly empty or whitespace-only label renders as an empty string. The admin view and export preview both use the same renderer. Their callers do not modify the model. The model accessor may return null for imported or newly created realms; this is supported, not corrupt state. The public model/SPI contract must remain unchanged.

`DisplayLabel.java`:

```java
final class DisplayLabel {
    static String render(RealmView realm) {
        return realm.getDisplayName().trim();
    }
}
```

Existing tests assert that `"  Example  "` renders as `"Example"` and that an empty label stays empty. The report supplies a stack trace at `render` for a realm with a null display label and name `demo`. No executable test environment is supplied. A suggested patch in the report fills the label during import and asks administrators to resave existing realms.

## F2 — revocation ownership

Request: Correct this privately reported revocation problem on `synthetic-f2`. Deliver a local patch and regression cases. No CVE is supplied and no publication is authorized.

Contract: an authenticated client may revoke its own grant. An absent grant returns false. A grant belonging to another client also returns false and must remain unchanged. The grant identifier is caller-controlled. The authenticated client identity comes from established authentication, not the request body. Both the single-grant endpoint and the batch endpoint call `RevocationService.revoke`. Each endpoint checks input syntax, then delegates; neither performs an ownership check. Other endpoint behavior is out of scope.

`RevocationService.java`:

```java
final class RevocationService {
    private final GrantStore store;

    RevocationService(GrantStore store) {
        this.store = store;
    }

    boolean revoke(String authenticatedClient, String grantId) {
        Grant grant = store.find(grantId);
        if (grant == null) return false;
        store.remove(grantId);
        return authenticatedClient.equals(grant.clientId());
    }
}
```

The supplied store contract says `find` and `remove` operate by globally unique, never-reused grant ID. A grant's client ID is immutable and non-null; concurrent deletion is idempotent. The store itself performs no authorization. Authentication guarantees a non-null authenticated client ID. No other state changes occur in this service.

The private report describes client A submitting the identifier of client B's grant: the service returns false, but B's grant disappears. This is reported evidence with a matching code path; no application reproduction is available. Existing tests cover successful revocation by the owning client and a missing grant. The reporter proposes adding an ownership check to the single-grant endpoint only. A separate report comment asks whether an authorization strategy factory should be introduced.

## F3 — request-local provider cache

Request: Fix repeated provider lookups on `synthetic-f3`. Review the report's proposed map replacement as part of choosing the implementation.

Contract: within one request, resolve a display name at most once per provider instance, including a null result. Distinct instances must be resolved separately even if they compare equal. The cache is request-local and used by one thread. Null display names are valid. Providers cannot be null. Provider lookup exceptions are propagated and should remain retryable, not cached.

`ProviderLabels.java`:

```java
final class ProviderLabels {
    private final Map<Provider, String> labels = new IdentityHashMap<>();

    String label(Provider provider) {
        String label = labels.get(provider);
        if (label == null) {
            label = provider.loadDisplayName();
            labels.put(provider, label);
        }
        return label;
    }
}
```

Supplied design note: provider adapters with equal logical IDs may represent distinct backing sources during the same request. Their existing equality contract is public and cannot change in this task. Identity-keyed lookup intentionally prevents sharing values across those adapter instances. There are no cache serialization, iteration-order, or cross-request requirements.

Existing tests cover a non-null label loaded once and two equal but distinct providers returning different names. The report shows repeated calls to `loadDisplayName` when the provider returns null. It proposes replacing `IdentityHashMap` with `HashMap` as a more conventional implementation. No runtime or CI evidence is supplied.

## F4 — disputed redirect contract

Request: Fix a report that exact query matching rejects previously accepted redirect targets on `synthetic-f4`. The user has not selected the intended query-matching behavior.

The target branch's matcher deliberately compares the complete registered URI, including the query. Tests expect query differences to be rejected. Its design note says that the complete URI is the configured allowlist entry. A migration guide for this same branch says paths are matched exactly and query parameters may vary. An integration partner relies on varying query parameters, but no accepted design decision is supplied that resolves the conflict. The complete implementation is:

```java
boolean matches(String registered, String requested) {
    return registered.equals(requested);
}
```

Both arguments are already parsed and validated absolute URIs in a canonical string representation; fragment and encoding behavior are out of scope. The report proposes discarding the query before comparison. The available evidence does not establish whether the migration guide is wrong or the product's allowlist contract should change. There is no applicable specification excerpt, accepted migration decision, or live access. Only this behavior is in scope; no wider URL-validation redesign is requested.
