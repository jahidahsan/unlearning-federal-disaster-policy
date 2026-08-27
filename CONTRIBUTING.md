
# Contributing

## Branch and review workflow

Use a branch for each substantial research change, open a pull request, and request review from at least one team member before merging into `main`.

Suggested branch names:

- `data/<short-description>`
- `experiment/<short-description>`
- `docs/<short-description>`
- `fix/<short-description>`

## What belongs in the changelog

Add a changelog entry when a change affects the research question, codebook, gold labels, benchmark construction, prompt factors, model/provider design, evaluation protocol, post-processing, or interpretation of results.

Routine bug fixes, path corrections, retries, API serialization fixes, and notebook-cell repairs should be described in the commit or pull request, not promoted to a major changelog milestone unless they alter results.

## Notebook policy

- Commit only notebooks with stored outputs.
- Preserve the exact executed notebook for each completed release.
- Mark partial notebooks clearly and keep them under `notebooks/historical/incomplete/`.
- Do not clear outputs from the only execution record of a completed experiment.

## Experiment policy

Every completed experiment should contain or reference:

- exact input data and SHA-256 hash;
- prompt text and prompt hash;
- model/provider configuration;
- raw or append-only response logs;
- materialized predictions;
- evaluation tables and audits;
- environment/package snapshot;
- an output-bearing notebook;
- a concise report stating limitations.

Never overwrite a completed experiment. Create a new dated folder and update `docs/CHANGELOG.md`, `docs/EXPERIMENT_HISTORY.md`, and the manifests.
