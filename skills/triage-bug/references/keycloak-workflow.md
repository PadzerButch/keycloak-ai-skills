# Keycloak public bug workflow

Use this reference when choosing a disposition, priority, or tracker action. Refresh the sources relevant to the decision; these mappings are a researched baseline, not a substitute for current project policy or live metadata.

## Sources and precedence

- Read the current [triage guide](https://github.com/keycloak/keycloak/blob/main/docs/bug-triage.md), [verification diagram](https://github.com/keycloak/keycloak/blob/main/docs/bug-triage-verify.svg), and [priority diagram](https://github.com/keycloak/keycloak/blob/main/docs/bug-triage-prioritize.svg). Inspect the SVG diagrams visually or trace their connections; extracted text alone loses branches.
- Check the [bug form](https://github.com/keycloak/keycloak/blob/main/.github/ISSUE_TEMPLATE/bug.yml), [team mapping](https://github.com/keycloak/keycloak/blob/main/.github/teams.yml), [live labels](https://github.com/keycloak/keycloak/labels), and [bot source](https://github.com/keycloak/keycloak-github-bot) when proposing metadata or automation.
- Use [versioned documentation](https://www.keycloak.org/documentation), [guides](https://www.keycloak.org/guides), [migration guidance](https://www.keycloak.org/docs/latest/upgrading/index.html), and relevant [source documentation](https://github.com/keycloak/keycloak/tree/main/docs) for behavior. Latest documentation may not describe an older release.
- Use the [contribution guide](https://github.com/keycloak/keycloak/blob/main/CONTRIBUTING.md) for enhancements/fix handoffs, [community channels](https://www.keycloak.org/community) for help, and the [security policy](https://www.keycloak.org/security) for security handling.

Record dates/revisions and material conflicts. Policy describes the intended process; repository source does not prove the deployed bot version or configuration. Where effects are unresolved, recommend maintainer verification without inventing metadata or a closure date.

## Verification and disposition

The verification diagram checks correct team/area, help request, recent release, sufficient information, then validity before priority. Apply the first supported disposition, while routing credible security concerns promptly. Do not erase earlier information when the issue has already been triaged.

| Finding | Recommended handling |
| --- | --- |
| Incorrect team/area | Propose verified routing and continue triage. Check mappings; some areas have multiple teams or no mapped team. |
| Help/configuration request | Explain the specific cause or question and link a suitable community destination; consider `action/question`. A confusing guide may warrant a documentation bug. |
| Old-release-only evidence | Consider `action/old-release` and request current-version verification. The researched bug form requires reproducibility on latest or nightly. Do not call a defect fixed solely because the reported version is old, or apply upstream release support assumptions to a downstream support case. |
| Insufficient report | Consider `action/missing-info` with the precise evidence needed. Agent tool limitations do not make a sufficient report incomplete. |
| Expected behavior/invalid | Consider `action/invalid` only with a specific, sourced explanation. Check whether the claim instead reveals a documentation defect or security concern. |
| Confirmed duplicate | Link the canonical issue, explain the match, and propose an appropriate maintainer closure and reason. No `action/duplicate` was present in the researched action inventory. |
| Already fixed | Verify the same defect and fix status; distinguish merged from released. Recommend the appropriate closure/follow-up without inventing a bot action or released version. |
| Enhancement/new feature | Explain the missing capability versus broken behavior and use the current request/contribution route. Do not reject it without useful routing. |
| Valid bug | Apply priority below. |
| Inconclusive | Keep further triage necessary and name the smallest resolving check. Do not force closure or low priority. |

## Priority decision table

Read in order. “Documented” refers to the affected behavior/use case; cite the relevant documentation. The chart does not define numerical thresholds for “many” or “some,” so explain the population estimate and its uncertainty.

| Condition | Action | Resulting priority in researched bot source |
| --- | --- | --- |
| Documented behavior OR many users blocked, with regression | `action/priority-regression` | `priority/blocker` |
| Documented behavior OR many users blocked, without regression | `action/priority-important` | `priority/important` |
| Neither preceding condition, some users blocked, with regression | `action/priority-important` | `priority/important` |
| Neither preceding condition, some users blocked, without regression | `action/priority-normal` | `priority/normal` |
| None of the preceding conditions, a single user blocked or no blocking | `action/priority-low` | `priority/low` |

Establish regression evidence from comparable versions/configurations, migration guidance, tests, or another supported explanation. If regression status or population remains unknown, show the conditional outcomes instead of treating unknown as “no.” A severe reported symptom may justify prompt investigation even while confidence remains low. Report that urgency separately from the proposed priority.

## Action effects and follow-up

The documented interfaces are an `action/<name>` label or a `~<name>` final comment line. Prefer one interface per selected action. Check issue state, bug labeling, sender permissions, and existing metadata; an action name alone is not a complete description of the transition.

The researched [action definitions](https://github.com/keycloak/keycloak-github-bot/blob/d0c61db5708153007868b5603204116b2dbf160f/src/main/java/org/keycloak/gh/bot/BugActions.java) show:

| Action group | Effects to consider before recommending execution |
| --- | --- |
| `question`, `invalid` | Posts a bot message and closes as not planned. |
| `missing-info`, `old-release` | Posts a bot message, selects the missing-information status, and enables expiration. |
| `priority-regression` | Selects blocker and a milestone. Do not promise a particular delivery date. |
| `priority-important` | Selects important. |
| `priority-normal`, `priority-low` | Posts a message, adds a reaction and contribution/aging labels, and removes the milestone. |

The implementation replaces existing status labels, removes the action label, and can reopen a closed issue for non-closing actions. Its comment-producing actions replace earlier bot comments. Explain relevant effects; do not replay an action merely to restate an existing decision. Comment triggers have additional restrictions described below.

The triage guide documents missing-information expiry after 14 days, low/normal inactivity expiry after 90/180 days, and reaction-based promotion at 10/20 reactions. A reporter reply returns a missing-information issue to triage. It describes removing `status/auto-expire` or `status/auto-bump` to disable those behaviors. Treat these as policy; the discrepancies below prevent assuming every documented effect is live.

For an already-triaged issue, the guide directs adding the new `priority/...` label; the bot removes the previous priority and disables automatic bumping/expiration for important/blocker. Reassess when impact, workarounds, or evidence changes. Avoid automatically replaying the initial priority action and its other side effects.

Consider `backport/<release branch>` only for verified affected, applicable maintained branches. It participates in patch-release tracking and is later replaced by `release/x.y.z`; do not add release labels manually. Separate a backport proposal from approval, implementation, and release evidence.

## Dated discrepancies to recheck

Verified on 2026-11-03 against Keycloak commit `7c989e08081001aae3881e1bd8aadcb5550b5429`, bot commit `d0c61db5708153007868b5603204116b2dbf160f`, and the public label API. Deployed bot revision/configuration was not verified.

- **Missing-information label:** the guide says `status/missing-info`; the live inventory uses `status/missing-information`. The action is `action/missing-info`. Verify resulting status independently from the trigger name.
- **Team bump:** the guide mentions `team/rh-iam`, absent from the retrieved live inventory. Use the current team map; do not manufacture an assignment to increase priority.
- **Expiration:** the [scheduler source](https://github.com/keycloak/keycloak-github-bot/blob/d0c61db5708153007868b5603204116b2dbf160f/src/main/java/org/keycloak/gh/bot/BugActionScheduleAutoExpire.java) uses the configured low-priority cutoff in both searches, conflicting with the documented separate intervals. Report the discrepancy, not an asserted production outcome.
- **Automatic bumping:** the [bump source](https://github.com/keycloak/keycloak-github-bot/blob/d0c61db5708153007868b5603204116b2dbf160f/src/main/java/org/keycloak/gh/bot/BugActionScheduleAutoBump.java) queries auto-expiration rather than auto-bump. Do not promise that removing auto-bump alone disables the deployed behavior without verification.
- **Comment eligibility:** the [handler](https://github.com/keycloak/keycloak-github-bot/blob/d0c61db5708153007868b5603204116b2dbf160f/src/main/java/org/keycloak/gh/bot/BugActionsOnComment.java) checks for an open bug and a user who belongs to the organization. A drafted trigger is not evidence any commenter can execute it.

Keep unresolved live effects in the handoff. Routine triage does not authorize fixing or testing the bot against live issues.
