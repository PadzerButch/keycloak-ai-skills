# Automation discrepancies to recheck

Read when a proposed action depends on resulting status/team labels, expiration, automatic bumping, or comment-trigger eligibility. Refresh the relevant sources; this historical evidence does not establish deployed behavior. The [public workflow](keycloak-workflow.md) governs routine decisions.

Source baseline: Keycloak commit `7c989e08081001aae3881e1bd8aadcb5550b5429` and bot commit `d0c61db5708153007868b5603204116b2dbf160f`. Check current labels and deployed bot behavior before relying on these discrepancies.

- **Missing-information label:** the guide says `status/missing-info`; the live inventory uses `status/missing-information`. The action is `action/missing-info`. Verify resulting status independently from the trigger name.
- **Team bump:** the guide mentions `team/rh-iam`, absent from the retrieved live inventory. Use the current team map; do not manufacture an assignment to increase priority.
- **Expiration:** the [scheduler source](https://github.com/keycloak/keycloak-github-bot/blob/d0c61db5708153007868b5603204116b2dbf160f/src/main/java/org/keycloak/gh/bot/BugActionScheduleAutoExpire.java) uses the configured low-priority cutoff in both searches, conflicting with the documented separate intervals. Report the discrepancy, not an asserted production outcome.
- **Automatic bumping:** the [bump source](https://github.com/keycloak/keycloak-github-bot/blob/d0c61db5708153007868b5603204116b2dbf160f/src/main/java/org/keycloak/gh/bot/BugActionScheduleAutoBump.java) queries auto-expiration rather than auto-bump. Do not promise that removing auto-bump alone disables the deployed behavior without verification.
- **Comment eligibility:** the [handler](https://github.com/keycloak/keycloak-github-bot/blob/d0c61db5708153007868b5603204116b2dbf160f/src/main/java/org/keycloak/gh/bot/BugActionsOnComment.java) checks for an open bug and a user who belongs to the organization. A drafted trigger is not evidence any commenter can execute it.

Keep unresolved live effects in the handoff. Routine triage does not authorize fixing or testing the bot against live issues.
