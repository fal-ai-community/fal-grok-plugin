# fal.ai Grok Plugin

Grok Bot, Grok Build and Cursor plugin package for fal.ai. This repository contains only the plugin manifests, the MCP server reference, skills, assets, and review/eval notes. The MCP server implementation lives separately and is referenced by URL.

## Contents

- `.grok-plugin/plugin.json` - Grok plugin manifest
- `.cursor-plugin/plugin.json` - Cursor plugin manifest (also used by Grok Bot)
- `.mcp.json`, `mcp.json` - fal MCP server reference (`https://mcp.fal.ai/mcp-relay`)
- `skills/*/SKILL.md` - Workflow instructions for fal.ai media production
- `assets/fal.png` - Plugin icon/logo asset
- `evals/hero-workflows.json` - Hero workflow review/eval scenarios
- `evals/non-invocation.json` - Negative prompts that should not trigger fal.ai

## MCP server

- URL: `https://mcp.fal.ai/mcp-relay` (Streamable HTTP)
- Auth: OAuth browser sign-in with your fal account (`mcp.fal.ai`, `authkit.fal.ai`). No API key to paste.
- Generated media is served from fal's CDN (`*.fal.media`). Runs are billed to the signed-in fal account.

The plugin stores no credentials and installs no hooks or bundled binaries.
It includes an explicit package-refresh script; it does not run automatically on installation.

## Skills

The plugin bundles six focused entry points:

| Skill | Deliverable |
| --- | --- |
| `fal-media` | Current model discovery, native execution, job recovery and specialist guidance |
| `product-ad-campaign` | Consistent campaign assets and channel variants |
| `game-asset-production` | Transparent frames, atlas and engine import metadata |
| `storyboard-to-short-film` | Finished cut, shot table and audio stems |
| `ecommerce-product-photography` | Consistent hero, detail and lifestyle photos by SKU |
| `localize-and-repurpose` | Localized speech, timed captions and channel cuts |

The local guides keep stable production and QA checks. The fal router retrieves
specialist guidance, current model contracts and prices through live tools only
when the task needs them. It reuses returned guide versions and avoids extra
lookups for simple generation. If guidance is unavailable, it uses the local
checks and reports any stage it cannot complete or verify.

Rendering requires an available local renderer or supported host tool. The
plugin skill bundle does not install CLI runtimes or renderer dependencies.

## Review

Hero workflow scenarios are documented in `evals/hero-workflows.json`. Negative trigger tests are documented in `evals/non-invocation.json`.

## Legal

- Website: https://fal.ai
- Privacy policy: https://fal.ai/legal/privacy-policy
- Terms of service: https://fal.ai/legal/terms-of-service
- Support: support@fal.ai

The MIT license covers the files in this repository only. It does not cover fal's service, the models you run through it, or the media they produce: those are governed by the fal Terms of Service and each model's own license terms. The fal name and logo are trademarks of fal and are not licensed for other use.

## Canonical source and package updates

The full 36-skill library remains in
[fal-ai-community/skills](https://github.com/fal-ai-community/skills). This plugin
ships a generated hybrid selection. `skills-source.lock.json` records the reviewed
source commit, bundle type, entry points and hash registry. Edit canonical skills
in that repository, then regenerate this package.

```sh
python3 -m venv .venv
.venv/bin/pip install PyYAML==6.0.3
.venv/bin/python scripts/sync-skills.py --check
```

Remove `--check` to refresh from the existing source pin. To adopt a new reviewed
source, update the lock's commit and retain `bundle: "hybrid"`, regenerate, inspect
the diff and commit it. Git operations use SSH. The sync script changes only the
skill payload and its lock; native manifests, marketing copy, connector/MCP
configuration, icons and evals remain maintained in this package.

See the [installation guide](https://github.com/fal-ai-community/skills/blob/b83a9ed0273f291c7016119e3f0792d6504639a5/docs/install.md)
for standalone full-library installation and package build options. CI verifies
every generated skill file against the locked source. Native authentication,
marketplace installation and paid creative output remain manual checks.
