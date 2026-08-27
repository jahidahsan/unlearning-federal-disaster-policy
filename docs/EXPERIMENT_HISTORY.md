
# Experiment History

## Status labels

- **Current completed:** latest finished experiment used for the present review.
- **Completed historical:** execution completed, but later data or methodology superseded it.
- **Provisional:** technically complete, but conclusions depend on incomplete or historical gold labels.
- **Partial:** contains useful outputs but ended with an interruption or stored error.
- **Deferred:** intentionally omitted until complete.

## 1. Initial McGuire paragraph pilot

**Purpose:** establish whether LLMs could identify organizational-unlearning passages at paragraph level in a single article.  
**Key artifacts:** `notebooks/historical/completed/initial_mcguire_4o_mini_executed.ipynb`, early Katrina workbooks, and pilot prediction files in `archive/legacy_exports/`.  
**Outcome:** provided the first passage-level workflow and exposed the need for a clearer codebook, structured outputs, and human adjudication.

## 2. Prompt and provider A/B tests

**Purpose:** compare direct prompting, codebook definitions, examples, metadata, and model/provider variants while keeping prompt conditions comparable.  
**Key artifacts:** output-bearing prompt-A/B notebooks, raw provider predictions, metrics, and prompt-result workbooks in `notebooks/historical/` and `archive/legacy_exports/`.  
**Rationale for change:** early results varied substantially with prompt wording and provider implementation, so later pipelines separated providers and recorded prompt/model manifests.

## 3. Combined human benchmark and revised codebook

**Purpose:** replace isolated labels with a combined human test set and improve conceptual clarity.  
**Key artifacts:** `data/codebooks/`, `data/benchmarks/historical/`, and the integrated human-annotation workbook.  
**Major change:** the original pillar framework was replaced by targets of unlearning—Leadership; Laws, Plans, and Policies; Capabilities; Funds and Resource Allocation; and Miscellaneous Organizational—alongside the affected government agency. Old and new gold labels were retained to make the transition auditable.

## 4. Local-context and evidence-first work

**Purpose:** determine whether surrounding paragraphs, explicit evidence requirements, and stricter definitions improved classification.  
**Key artifacts:** local-context benchmark versions, executed local-context notebook, provider prediction files, and grouped-context review workbooks.  
**Outcome:** neighboring context sometimes reduced performance or increased ambiguity, so target-only paragraph text remained the default for later locked comparisons. Evidence/checklist logic remained important because it reduced keyword-only and diagnosis-only positives.

## 5. Five-document extraction and annotation

**Purpose:** move from a single article to a five-document federal-policy corpus with verifiable paragraph provenance.  
**Key artifacts:** five PDFs in `data/source_documents/`, executed production notebooks, extraction workbooks, and annotated review PDFs.  
**Rationale for change:** paragraph alignment and source reconciliation were required to prevent incomplete excerpts, duplicate spans, and mismatched document titles from contaminating the benchmark.

## 6. Full pre-LangChain A/B experiment — completed but provisional

**Folder:** `experiments/2026-07-23_prelangchain-ab-v1.2/`  
**Execution:** completed July 23, 2026 across OpenAI, Anthropic, and Gemini, with 882 phase-1, 1,008 phase-2, 252 phase-3, and 630 stability predictions.  
**Design:** compared direct versus definition-based conditions, context choices, and one-stage versus two-stage workflows with resumable provider logs.  
**Critical caveat:** the corrected July 24 audit found final gold incomplete and zero conditions eligible under the corrected gates. Selections are therefore preserved as historical/provisional, not final winners.

## 7. Probability post-processing — completed historical

**Folder:** `experiments/2026-08-07_probability-postprocessing/`  
**Purpose:** evaluate probabilities rather than hard labels alone.  
**Additions:** calibration, threshold search, repeated cross-validation, post-processing, ensembles, coverage-accuracy curves, review queues, and comparisons with historical runs.  
**Role:** established the post-processing machinery later used more defensibly in the GPT-Test-first experiment.

## 8. Full-PDF evaluation — partial and superseded

**Notebook:** `notebooks/historical/incomplete/full_pdf_evaluation_partial.ipynb`  
**Purpose:** integrate full-corpus extraction, prompt comparisons, final model selection, and statistical testing.  
**Status:** substantial outputs were produced, but the notebook ended with a stored error and was later superseded by the paragraph-aligned GPT-Test-first design.

## 9. Paragraph-aligned GPT-Test-first evaluation — current completed

**Folder:** `experiments/2026-08-23_gpt-test-first/`  
**Notebook:** `notebooks/current/2026-08-23_paragraph_level_gpt_test_first_completed.ipynb`  
**Execution:** completed August 23, 2026 with no stored notebook error outputs and a passing final hard-validation report.

The sequence was intentionally locked:

1. Compare codebook examples versus no examples on GPT Test.
2. Compare checklist versus no checklist on GPT Test.
3. Select one model per provider.
4. Compare the selected codebook condition with a direct-target-only baseline.
5. Select thresholds and ensemble weights on GPT Test, including out-of-fold post-processing analysis.
6. Freeze all choices.
7. Call GPT Test ALL only with the locked prompt and selected models.

This design reduced leakage from using GPT Test ALL for iterative decisions, while preserving the limits of selection on a small benchmark.

## 10. LangChain retrieval experiment — deferred

The ongoing retrieval-based experiment is intentionally absent from this repository version. It will be added only after the notebook has stored outputs and its output folder, exact input hash, provider completion status, and final audits are available.
