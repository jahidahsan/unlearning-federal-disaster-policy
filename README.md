
# Organizational Unlearning in Federal Disaster Policy

Private research repository for developing and evaluating LLM-assisted paragraph-level identification of organizational unlearning in post-Hurricane Katrina federal policy documents.

**Snapshot:** `v0.9.0-private-prelangchain`  
**Latest completed experiment:** `2026-08-23_gpt-test-first`  
**Current status:** consolidated and review-ready; the unfinished LangChain retrieval experiment is deliberately deferred to the next version.

## Start here

- `docs/EXPERIMENT_HISTORY.md` — how the research design evolved.
- `docs/DECISION_LOG.md` — major decisions and their rationale.
- `docs/DATA_VERSIONING.md` — exact codebook and benchmark versions.
- `docs/RESULTS_GUIDE.md` — how to interpret the latest completed results.
- `docs/KNOWN_LIMITATIONS.md` — caveats that must accompany peer review.
- `docs/GITHUB_UPLOAD.md` — how to initialize and push the extracted folder to a private GitHub repository.
- `experiments/2026-08-23_gpt-test-first/reports/Unlearning_Experiment_Report.md` — generated report for the latest completed run.

## Canonical inputs

| Artifact | Repository path | SHA-256 |
|---|---|---|
| Latest human-annotation/codebook workbook | `data/codebooks/current/Unlearning_Codebook_2026-08_latest.xlsx` | `ae88f0e46bbc4cbc31181e5e905906098be6ec35f87926dc426a4866aafc3208` |
| Latest strict paragraph-aligned benchmark | `data/benchmarks/current/Unlearning_GPT_Test_Paragraph_Aligned_ALL_strict_codebook.xlsx` | `eea91ee31b51187774880fa395e75f4e0fc7bb90419a16fbaab4bbb99ea55d83` |
| Exact input used in the Aug. 23 run | `experiments/2026-08-23_gpt-test-first/inputs/Unlearning_GPT_Test_Paragraph_Aligned_ALL.xlsx` | `a148051e24ccab080b35a2404cebddeff24cd7c0aec9b5af1f45c42a39c85d31` |

The Aug. 23 experiment used the correct **Target-based** codebook categories, not the original pillar taxonomy. It used an earlier wording revision of the binary definition. The run remains immutable and is documented as a historical result; the strict workbook above is canonical for future runs.

## Repository structure

```text
.
├── data/          Current inputs, historical benchmark milestones, and five source PDFs
├── notebooks/     Only notebooks with stored outputs; current, completed historical, and partial audit records
├── experiments/   Immutable completed experiment packages and raw provider outputs
├── archive/       Deduplicated legacy exports, result workbooks, presentations, and annotated documents
├── docs/          Research history, decisions, limitations, and release guidance
├── manifests/     File inventory, notebook audit, exclusions, and checksums
└── scripts/       Repository validation and checksum refresh utilities
```

## Validate the snapshot

```bash
python scripts/validate_repository.py
```

The validator checks required hashes, notebook outputs, GitHub’s 100 MiB file limit, the deliberate exclusion of the workshop paper and unfinished LangChain notebook, and common secret-token patterns.

## Working rules

1. Never overwrite a completed experiment directory; create a new dated directory.
2. Record the exact input-workbook and prompt hashes for every run.
3. Commit notebooks only after they contain outputs.
4. Use the changelog for major research changes, not routine debugging.
5. Keep API keys in local environment variables or Colab secrets; no credentials belong in Git.

The source audit covered 704 files across the three supplied archives. Every source instance is represented by an included file or an explicit exclusion record.

This repository is private and has no public license. See `PRIVATE_REPOSITORY_NOTICE.md`.
