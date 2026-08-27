
# Reproducibility Guide

## Validate the repository first

```bash
python scripts/validate_repository.py
```

## Reproduce the Aug. 23 analysis exactly

Use the immutable package under `experiments/2026-08-23_gpt-test-first/` and the executed notebook in `notebooks/current/`.

1. Read `experiments/2026-08-23_gpt-test-first/reports/README_EXECUTION.txt`.
2. Use the input workbook inside that experiment folder, not the later strict canonical workbook.
3. Confirm the source-workbook hash is `a148051e24ccab080b35a2404cebddeff24cd7c0aec9b5af1f45c42a39c85d31`.
4. Use the prompt and checkpoint files already stored in the package.
5. Reuse the raw JSONL logs and materialized prediction snapshots to reproduce analysis without new API calls when possible.
6. Use `manifests/pip_freeze.txt` and `manifests/package_versions.csv` for the recorded environment.

The experiment’s `audits/final_validation_report.json` is the authoritative completion check.

## Run a new strict-codebook experiment

Do not modify the Aug. 23 directory.

1. Create a new dated experiment directory.
2. Use `data/benchmarks/current/Unlearning_GPT_Test_Paragraph_Aligned_ALL_strict_codebook.xlsx`.
3. Record its SHA-256 hash before any API calls.
4. Save all rendered prompt text and prompt hashes.
5. Keep append-only provider logs and resumable checkpoints.
6. Save the final notebook with outputs.
7. Run integrity, completion, and source-hash audits.
8. Update the changelog, experiment history, decision log if needed, and repository manifests.

## API credentials

No API keys are included. Use environment variables, Colab secrets, or a team-approved secret manager. Never paste credentials into a notebook cell or commit `.env` files.

## Historical packages

- `experiments/2026-07-23_prelangchain-ab-v1.2/` preserves the complete workspace, frozen snapshot, raw provider logs, reports, and corrected post-hoc analysis.
- `experiments/2026-08-07_probability-postprocessing/` preserves raw provider responses, reports, plots, and the experiment manifest.

Treat their recorded gold basis and caveats as part of the experiment, not as details to be retroactively changed.
