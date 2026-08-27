UNLEARNING PARAGRAPH-LEVEL EXPERIMENT — EXECUTION README

Experiment root:
/content/drive/MyDrive/Unlearning_Paragraph_Level_LLM_Experiment/paragraph_level_gpt_test_first_v2_20260821

Required order:
1. Run setup/import/input cells with all paid-call switches False.
2. Review Stage 1 preflight; enable ALLOW_PAID_API_CALLS and RUN_STAGE1_GPT_TEST.
3. Run the three Stage 1 provider cells, then Stage 1 analysis.
4. Enable RUN_STAGE2_GPT_TEST and run the three Stage 2 provider cells, then Stage 2 analysis.
5. Run model selection and create the selected-model GPT Test review workbook.
6. Enable RUN_BASELINE_GPT_TEST; run the three baseline provider cells.
7. Run threshold, weight, OOF, repeated-CV, LODO, and significance cells.
8. Review the final GPT Test manual-review workbook.
9. Only then enable RUN_FINAL_GPT_TEST_ALL and run the three final-all provider cells.
10. Run final-all evaluation, audits, reports, and packaging.

Important controls:
- Never overwrite the source workbook or Codebook (revised) sheet.
- Change EXPERIMENT_NAME after changing candidate models, model settings, prompt text,
  schema, source workbook, ROW_LIMIT, or replicate count.
- Keep only one paid stage switch True at a time.
- Every provider has a separate execution cell and append-only JSONL cache.
- A permanent error stops only the affected model configuration.
- Review preflight new-call count and rough cost before enabling paid calls.

Primary inference caveat:
Out-of-fold tuning covers threshold and model weights, but prompt and model selection are
not nested. Prompt/model-selection p-values are exploratory.

API reproducibility caveat:
Hosted LLM APIs are not guaranteed to reproduce identical outputs on fresh requests. The
notebook preserves every successful raw response and reuses it through hash-addressed caches,
so the reported experiment is exactly auditable even though a brand-new API rerun may drift.

GPT Test ALL caveat:
Unlabeled rows are default No and exact GPT Test overlaps exist. Report sensitivity scopes.
