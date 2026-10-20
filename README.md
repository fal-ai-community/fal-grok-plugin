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

The plugin ships no scripts, hooks or binaries and stores no credentials.

## Skills

The bundled skills cover practical fal.ai workflows:

- Provider-level Fal discovery and exact named-model routing
- Model routing and catalog navigation
- Prompting for specific model families
- Commercial/product asset production
- Marketing campaign assets
- UGC/talking-head ads
- Cinematography and storytelling
- Character design and game assets
- 3D experience generation
- Multi-step fal.ai workflow planning

## Review

Hero workflow scenarios are documented in `evals/hero-workflows.json`. Negative trigger tests are documented in `evals/non-invocation.json`.

## Legal

- Website: https://fal.ai
- Privacy policy: https://fal.ai/legal/privacy-policy
- Terms of service: https://fal.ai/legal/terms-of-service
- Support: support@fal.ai

The MIT license covers the files in this repository only. It does not cover fal's service, the models you run through it, or the media they produce: those are governed by the fal Terms of Service and each model's own license terms. The fal name and logo are trademarks of fal and are not licensed for other use.
