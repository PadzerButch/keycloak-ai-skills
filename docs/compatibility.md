# Compatibility checks

The shared skills use Agent Skills frontmatter, relative resource paths, and ordinary Markdown instructions. Root `plugin.json` is an Agent Plugins 1.0 package. Client-specific files handle installation; they do not contain separate copies of the workflows.

Package `0.2.0` includes `add-skill`, `triage-cve`, and `review-pr`. Its manifests, packaged resources, and local links pass the collection validator; the 43 Python validation tests pass on Linux with Python 3.14.7. These structural checks do not verify client discovery or review/triage behavior.

The client checks below are historical checks of the initial `add-skill` package. They have not been repeated for `0.2.0`; discovery and invocation of `triage-cve` and `review-pr` remain unverified.

| Client | Integration | Local verification |
| --- | --- | --- |
| Codex CLI 0.164.0 | Root plugin and `.agents/plugins/marketplace.json` | Fresh installation, discovery, and headless invocation passed with the portable manifest and shared skill. The generated skill also passed the bundled validator. |
| Claude Code 2.1.311 | `.claude-plugin/` | Native validation, local marketplace installation, and component discovery passed; inventory lists `add-skill`. Invocation has not been tested. |
| GitHub Copilot CLI 1.0.104 | Root plugin; shared `.claude-plugin/marketplace.json` | Local marketplace installation reported one skill installed and enabled. Invocation has not been tested. |
| Gemini CLI 0.65.0 | `gemini-extension.json`; shared `skills/` | Native validation, clean installation, and skill discovery passed; `add-skill` is enabled. Invocation has not been tested. |
| IBM Bob Shell 1.0.6 | `bob-extension.json` and `BOB.md` | Native extension validation passed. Installation and context-driven invocation have not been tested. |
| IBM Bob IDE | Agent Skills in Bob's discovery directories | Documented format compatibility; IDE installation and activation have not been tested here. |

Local Python checks run on Linux with Python 3.14.7. CI covers Linux and Windows with Python 3.10 and 3.14; hosted runs start after publication.

Installation, discovery, and invocation are separate checks. During the historical checks, no GitHub-hosted installation was tested because the checkout had not been published. Codex created the requested test skill under `skills/summarize-notes/`; automatic discovery of that generated standalone skill was not tested. An earlier test's sandbox made `.agents/` read-only. Temporary Codex installation was removed and the original configuration restored; other installation checks used temporary client settings.

Gemini's first installation attempt hit the sandbox's OS user-lookup restriction. A clean reinstall outside that sandbox completed successfully. Claude's validator reports optional marketplace-description, author, and public-directory icon warnings; local installation and discovery pass without them.

Installation contracts: [Codex plugins](https://developers.openai.com/plugins/build/plugins), [Claude plugins](https://code.claude.com/docs/en/plugins-reference), [Copilot plugins](https://docs.github.com/en/copilot/concepts/customizations/plugins), [Gemini extensions](https://geminicli.com/docs/extensions/reference/), [Bob IDE skills](https://bob.ibm.com/docs/ide/features/skills).
