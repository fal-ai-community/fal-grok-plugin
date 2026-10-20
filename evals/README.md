# fal.ai Plugin Evals

Use these cases during manual or automated review to confirm that the agent chooses
the fal.ai plugin for media production work, avoids it for unrelated tasks, and
respects connector safety behavior.

## Hero Workflows

`hero-workflows.json` contains positive cases that should use fal.ai tools. A
passing run should:

- Call `recommend_model` when the user did not name a specific endpoint.
- Inspect the chosen endpoint schema before constructing model input.
- Check pricing before expensive, repeated, long-running, video, 3D, or
  training work.
- Use `submit_job`, `check_job`, and `get_job_result` for video, 3D, training,
  and other long-running work.
- Avoid write or cancel actions unless the user explicitly asked for them.
- Return endpoint IDs, request IDs when available, output URLs, and any known
  quality defects.

## Negative Trigger Cases

`non-invocation.json` contains prompts that should not call fal.ai tools. These
catch over-eager plugin activation for ordinary coding, weather, or text-editing
requests.

## Review Fixture Notes

The example URLs are placeholders for reviewer-owned or demo-account assets.
Replace them with accessible review assets before running live generation. Do
not use private user media unless the reviewer has supplied it for that run.
