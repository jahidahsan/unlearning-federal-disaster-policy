
# Changelog

This changelog records major research and data-design changes. Routine debugging and notebook maintenance belong in commit messages and pull requests.

## v0.9.0-private-prelangchain — 2026-08-26

- Consolidated the project into a private, review-oriented GitHub structure.
- Promoted the latest strict Target-based codebook and paragraph-aligned benchmark to canonical status.
- Preserved the completed Aug. 23 run as an immutable experiment tied to its exact pre-final Target-based codebook wording.
- Included all unique notebooks with stored outputs; discarded every outputless notebook.
- Added experiment, file, exclusion, checksum, and notebook-execution manifests.
- Deliberately excluded the unfinished LangChain retrieval experiment and the team workshop paper.

## v0.8.0 — 2026-08-23: GPT-Test-first paragraph-aligned evaluation

- Used GPT Test for prompt, model, threshold, and ensemble decisions before applying the locked configuration to GPT Test ALL.
- Tested examples and checklist factors separately.
- Selected one model per provider and compared the final codebook prompt against a direct-target-only baseline.
- Added constrained threshold and ensemble-weight selection, out-of-fold post-processing analysis, document- and labeler-level metrics, paired tests, source/prompt integrity checks, and a peer-review report package.
- Materialized complete predictions for 677 GPT Test ALL paragraphs across three selected providers.

## v0.7.0 — 2026-08-07: Probability post-processing

- Moved from hard labels alone to probability-based comparison.
- Added calibration, threshold tuning, cross-validated post-processing, ensemble evaluation, coverage-accuracy analysis, review queues, and historical comparison tables.

## v0.6.0 — 2026-07-24: Corrected pre-LangChain audit

- Preserved the full pre-LangChain multi-provider A/B experiment.
- Added a frozen snapshot, completeness checks, evidence-quote audits, target-taxonomy checks, tiered review, and an adjudication template.
- Reclassified the apparent winners as provisional because final gold adjudication was incomplete and no configuration passed the corrected eligibility gates.

## v0.5.0 — 2026-07-23: Full pre-LangChain A/B experiment

- Compared direct prompts, old and current codebook definitions, context windows, and one-stage versus two-stage workflows.
- Added provider-separated execution, API hardening, resumable append-only logs, stability runs, and constrained condition selection.

## v0.4.0 — July 2026: Multi-document and local-context expansion

- Expanded beyond the initial article to five source PDFs.
- Added verified PDF extraction, source reconciliation, local-context variants, and annotated review PDFs.
- Evaluated whether target-only text or neighboring paragraphs improved classification; context was not retained as the default final input.

## v0.3.0 — June–July 2026: Human benchmark and revised Target taxonomy

- Combined human annotations into a shared benchmark.
- Replaced the earlier pillar-oriented taxonomy with targets of unlearning: Leadership; Laws, Plans, and Policies; Capabilities; Funds and Resource Allocation; and Miscellaneous Organizational, plus the affected government agency.
- Retained old and new gold labels to support codebook comparisons.
- Incorporated later rationale review and EPA re-evaluation.

## v0.2.0 — Early 2026: Prompt and provider A/B testing

- Compared direct prompting, definitions, examples, metadata, and provider/model variants.
- Added provider-specific outputs, usage summaries, reliability tables, and review workbooks.

## v0.1.0 — Initial pilot

- Built the first McGuire/Katrina paragraph dataset.
- Used an LLM to produce paragraph-level unlearning labels and created the first human-versus-model review artifacts.
