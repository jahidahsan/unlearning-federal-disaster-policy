
# Known Limitations

## Data and gold labels

- GPT Test is small and was used for prompt selection, model selection, and post-processing decisions.
- GPT Test ALL is not fully human-adjudicated: 598 of 677 rows were assigned default No because no retained human paragraph-level label existed, and two additional rows were curated No without an explicit human label.
- Paragraphs derived from a labeled parent span inherit a label based on the rationale and revised paragraph-level codebook; they are not independent new annotations.
- Labeler-priority and Kyle-only exclusion decisions affect the benchmark composition and must be reported with results.

## Codebook version

- The Aug. 23 run used the correct Target taxonomy but pre-final wording of the strict binary definition.
- Much of the later strict logic was represented in the selected checklist, but the run is not an exact test of the latest codebook wording.
- A final paper result that claims use of the latest strict codebook should be rerun with the canonical strict benchmark or superseded by a later completed experiment using that file.

## Evaluation and selection

- Out-of-fold optimization applies to threshold and weights; prompt and model selection were not nested.
- Prompt-comparison confidence intervals and p-values are exploratory because the same rows were used for selection.
- The locked ensemble assigns zero weight to the selected Anthropic model. Anthropic predictions remain useful for provider comparison, but the optimized final probability is driven by OpenAI and Gemini.
- Precision-oriented selection can reduce recall. The examples and checklist results should be presented as metric trade-offs rather than simple “better/worse” conclusions.

## Output audits

The Aug. 23 final hard validation found complete materialization and no duplicate prediction keys, while retaining nonfatal flags rather than silently repairing them:

- 13 target-label consistency flags across audited tables;
- 97 evidence-quote validity flags across audited tables;
- 47 evidence-quote flags in the final GPT Test ALL selected-model table.

These rows require review before claims based on target labels or quoted evidence are finalized.

## Historical experiments

- The pre-LangChain v1.2 workflow completed technically, but its corrected post-hoc audit found final gold incomplete and zero eligible conditions. Its selections are provisional historical records.
- Several partial output-bearing notebooks are retained for audit history. They are not current executable entry points.

## Reproducibility and external services

- Exact model availability, provider APIs, pricing, and behavior may change.
- Re-running paid API calls requires team-managed credentials that are intentionally absent.
- Some notebooks contain absolute Colab/Google Drive paths that must be updated for a new environment.

## Public-release risks

- Source-PDF redistribution rights have not been cleared for every document.
- Raw responses contain full prompts and source passages, and may contain provider request identifiers or cost metadata.
- Human labeler names and annotation history remain visible in several private workbooks.
