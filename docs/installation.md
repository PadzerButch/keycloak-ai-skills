# Installation

Use the [client installation commands](../README.md#quick-start), then start a new session. To get newly released skills, update the plugin and start another session.

## Manual download

Download `keycloak-ai-skills-X.Y.Z.tar.gz` and its accompanying `.tar.gz.sha256` file from the [latest release](https://github.com/lhanusov/keycloak-ai-skills/releases/latest). Save both in the same directory. Replace `X.Y.Z` with the downloaded version, then verify and extract:

```bash
sha256sum --check keycloak-ai-skills-X.Y.Z.tar.gz.sha256
tar -xzf keycloak-ai-skills-X.Y.Z.tar.gz
```

These commands require `sha256sum` and `tar`. After extracting, install the directory with your client's local plugin installer, or copy an entire skill folder into its supported skill directory. Include the skill's references, assets, and scripts.

For standalone skill locations, see [client support](../skills/add-skill/references/client-support.md). Keep hidden client integration directories when installing the complete plugin.

## Bob IDE and other clients

The Bob Shell extension command installs the Shell integration. Bob IDE uses separate [skill discovery](https://bob.ibm.com/docs/ide/features/skills); install standalone skill folders through the IDE's supported mechanism.

Other Agent Skills clients can use the same skill folders through their own installer.

## If a skill is unavailable

1. Confirm that the plugin or extension is installed in the client you are using.
2. Start a new session after installation or an update.
3. Check the client's skill list; Gemini CLI exposes `/skills list`.
4. Try the explicit [invocation syntax](usage.md#invocation).
5. For a standalone skill, check its location against [client support](../skills/add-skill/references/client-support.md).

Passing repository checks does not confirm that your client has loaded the skills.

Client documentation: [Codex plugins](https://developers.openai.com/plugins/build/plugins), [Claude plugins](https://code.claude.com/docs/en/plugins-reference), [Copilot plugins](https://docs.github.com/en/copilot/concepts/customizations/plugins), [Gemini extensions](https://geminicli.com/docs/extensions/reference/), and [Bob IDE skills](https://bob.ibm.com/docs/ide/features/skills).
