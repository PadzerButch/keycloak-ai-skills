# Client compatibility

The skills use Agent Skills frontmatter, relative resource paths, and Markdown instructions. Root `plugin.json` defines the Agent Plugins package. Client-specific files provide installation and discovery while using the same `skills/` directory.

| Client | Integration |
| --- | --- |
| Codex | Root plugin and `.agents/plugins/marketplace.json` |
| Claude Code | `.claude-plugin/` |
| GitHub Copilot CLI | Root plugin and `.claude-plugin/marketplace.json` |
| Gemini CLI | `gemini-extension.json` and `skills/` |
| IBM Bob Shell | `bob-extension.json` and `BOB.md` |
| IBM Bob IDE | Standalone skills in the IDE's discovery directory; see [client support](../skills/add-skill/references/client-support.md) |

Installation, skill discovery, and invocation are separate capabilities. Check the installed client's supported paths and reload behavior when diagnosing availability. Bob Shell extensions and Bob IDE skill discovery are separate integrations.

Collection checks cover package metadata, local resource links, shared-reference synchronization, containment, and standalone relocation. CI runs on Linux and Windows with Python 3.10 and 3.14. See the README's [maintenance instructions](../README.md#maintain) for commands and the [scenario guide](skill-validation.md) for workflow checks.

Installation contracts: [Codex plugins](https://developers.openai.com/plugins/build/plugins), [Claude plugins](https://code.claude.com/docs/en/plugins-reference), [Copilot plugins](https://docs.github.com/en/copilot/concepts/customizations/plugins), [Gemini extensions](https://geminicli.com/docs/extensions/reference/), [Bob IDE skills](https://bob.ibm.com/docs/ide/features/skills).
