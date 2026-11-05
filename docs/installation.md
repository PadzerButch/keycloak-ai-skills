# Installation

Use the [client installation commands](../README.md#quick-start) to install the collection. Start a new session after installing or updating it. New collection skills become available after the updated plugin is released and installed.

## Manual download

Download `keycloak-ai-skills-X.Y.Z.tar.gz` and its accompanying `.tar.gz.sha256` file from the [latest release](https://github.com/lhanusov/keycloak-ai-skills/releases/latest). Save both in the same directory. Replace `X.Y.Z` with the downloaded version, then verify and extract:

```bash
sha256sum --check keycloak-ai-skills-X.Y.Z.tar.gz.sha256
tar -xzf keycloak-ai-skills-X.Y.Z.tar.gz
```

These verification commands require `sha256sum` and `tar`. The extracted directory contains the plugin manifests and `skills/`. Extraction alone does not install or activate the skills: use your client's local plugin installer or copy the desired standalone skill folder into its supported discovery directory, preserving the skill's references, assets, and scripts.

For standalone skill locations, see [client support](../skills/add-skill/references/client-support.md). Keep hidden client integration directories when installing the complete plugin.

## Bob IDE and other clients

The Bob Shell extension command installs the Shell integration. Bob IDE uses separate [skill discovery](https://bob.ibm.com/docs/ide/features/skills); install standalone skill folders through the IDE's supported mechanism.

Other Agent Skills clients can use the same skill folders through their own installer. Follow the target project's conventions and confirm the installed client's discovery directory.

## If a skill is unavailable

1. Confirm that the plugin or extension is installed in the client you are using.
2. Start a new session after installation or an update.
3. Check the client's skill list; Gemini CLI exposes `/skills list`.
4. Try the explicit [invocation syntax](usage.md#invocation).
5. For a standalone skill, check its location against [client support](../skills/add-skill/references/client-support.md).

Installation, discovery, and invocation are separate steps. Repository validation checks packaging and local references; it does not establish that a particular client has loaded a skill.

Client documentation: [Codex plugins](https://developers.openai.com/plugins/build/plugins), [Claude plugins](https://code.claude.com/docs/en/plugins-reference), [Copilot plugins](https://docs.github.com/en/copilot/concepts/customizations/plugins), [Gemini extensions](https://geminicli.com/docs/extensions/reference/), and [Bob IDE skills](https://bob.ibm.com/docs/ide/features/skills).
