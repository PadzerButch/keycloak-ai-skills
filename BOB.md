# Keycloak AI Skills

When asked to create or scaffold a reusable skill, read [add-skill](skills/add-skill/SKILL.md) and follow its instructions. Resolve that path and its supporting resources from this installed extension directory, not the user's project. Load the skill only when it applies to the request.

When asked to triage a bug in the public Keycloak project, read [triage-bug](skills/triage-bug/SKILL.md) and follow its instructions. Resolve its resources from this installed extension directory. The skill checks duplicates and fixes, follows Keycloak's verification and priority flow, and drafts a report, natural comment, and next actions. It supports GitHub connectors and `gh` CLI; security concerns are routed using the project policy.

When asked to assess a specific Keycloak issue for security impact or CVE relevance, read [triage-cve](skills/triage-cve/SKILL.md) and follow its instructions. Resolve its resources from this installed extension directory. The skill produces a report, proposed comment, and workflow handoff, including security duplicate analysis, urgency, and embargo reasoning where relevant.

When asked to review a Keycloak PR for a bug fix, enhancement, new feature, security hardening, or vulnerability fix, read [review-pr](skills/review-pr/SKILL.md) and follow its instructions. Resolve its resources from this installed extension directory. The skill selects relevant review checks and produces a report and draft review without posting it; a CVE is not required.
