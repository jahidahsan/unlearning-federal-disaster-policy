
# Data and Codebook Versioning

## Current canonical files

| Role | Path | SHA-256 |
|---|---|---|
| Human annotation and latest revised codebook | `data/codebooks/current/Unlearning_Codebook_2026-08_latest.xlsx` | `ae88f0e46bbc4cbc31181e5e905906098be6ec35f87926dc426a4866aafc3208` |
| Paragraph-aligned GPT Test and GPT Test ALL with latest strict wording | `data/benchmarks/current/Unlearning_GPT_Test_Paragraph_Aligned_ALL_strict_codebook.xlsx` | `eea91ee31b51187774880fa395e75f4e0fc7bb90419a16fbaab4bbb99ea55d83` |
| Curated EPA/Kyle-only-removal milestone | `data/benchmarks/historical/Unlearning_Curated_GPT_Test_EPA_Reevaluation_KyleOnly_Removed.xlsx` | `6884dee9ed55b7294d5cc4bfb39579893d479d9cc51bf1c7764f8d9af2f57b60` |

The attached current codebook workbook is cell-for-cell equivalent to the archived `Unlearning Codebook_6April2026_v1 (4).xlsx`; only the directly attached copy is promoted as canonical.

## Aug. 23 immutable run input

| Role | Path | SHA-256 |
|---|---|---|
| Exact workbook used for the completed run | `experiments/2026-08-23_gpt-test-first/inputs/Unlearning_GPT_Test_Paragraph_Aligned_ALL.xlsx` | `a148051e24ccab080b35a2404cebddeff24cd7c0aec9b5af1f45c42a39c85d31` |
| Executed notebook | `notebooks/current/2026-08-23_paragraph_level_gpt_test_first_completed.ipynb` | `d7c2a922bd8bfbc68adff1985365ccab3b111845ad6a3443124b051ee462feeb` |
| Codebook whole-sheet hash recorded by the run | run manifest/report | `892a055512cdecccc191a768792ad1182933fb77ca3df31b2a2e4e470549d1e6` |

The current strict and Aug. 23 workbooks contain the same GPT Test, GPT Test ALL, and Extraction Audit data. Seven cells in `Codebook (revised)` differ, mainly the binary definition, detection rule, positive/negative clarifications, boundary rule, and example. Therefore, the Aug. 23 run is labeled **Target-based pre-final wording**, not “old pillar codebook” and not “exact latest strict codebook.”

## Dataset dimensions

- `GPT Test`: 84 paragraph-level rows plus one header row.
- `GPT Test ALL`: 677 paragraph-level rows plus one header row.
- Aug. 23 final model predictions: 2,031 rows, equal to 677 paragraphs × three selected providers.

## GPT Test ALL label basis

| Label status | Rows |
|---|---:|
| Direct human-labeled/adjudicated | 52 |
| Derived from a human-labeled parent span | 25 |
| Curated No without an explicit human label | 2 |
| Unlabeled and assigned default No under the corpus rule | 598 |

The resulting GPT Test ALL gold column contains 38 Yes and 639 No rows. Because most rows are operational default-No rather than independently adjudicated, GPT Test ALL should not be described as a fully human-labeled external test set.

## Versioning rules

1. Never overwrite a workbook used by a completed run.
2. Save a new version whenever codebook wording, gold labels, row boundaries, or source alignment changes.
3. Record SHA-256 hashes in the experiment manifest before API calls.
4. Preserve old/new gold columns when label changes are analytically relevant.
5. Document whether a reported result uses the old pillar codebook, a pre-final Target-based revision, or the latest strict Target-based version.
