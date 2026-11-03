# Duplicate and fix search

Search open and closed issues and pull requests. Begin with identifiers and distinctive errors, then vary component, behavior, endpoint, configuration, version, and suspected cause. Follow relevant references to older trackers or other repositories. Inspect credible matches rather than relying on search snippets.

Compare root cause where known, affected code, triggers, prerequisites, versions, impact, and fix. Classify candidates as confirmed duplicate, possible duplicate, related, or distinct, with links and concrete reasons. Shared symptoms or a shared CWE are insufficient; strong evidence can establish the same defect without a proven root cause. A recurrence after a fix may be a separate regression. Recommend a canonical issue only when supported.

Distinguish proposed, merged, backported, and released fixes. Verify the target branch and release evidence before naming a fixed version. A merged PR alone does not establish a released fix.

Record actual sources, queries, dates, open/closed coverage, result caps, and access limitations. Narrow capped searches when useful. Say “no duplicate found in the searched sources,” or that a search was unavailable, rather than claiming no duplicate exists. For private cases, use authorized sources and record private coverage separately; public results cannot establish absence from a private tracker. Keep confidential material out of public search queries.
