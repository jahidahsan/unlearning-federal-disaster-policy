# Paragraph-Level Unlearning LLM Experiment Report

- Experiment: `paragraph_level_gpt_test_first_v2_20260821`
- Generated UTC: `2026-08-23T17:05:07.955481+00:00`
- Source workbook SHA-256: `a148051e24ccab080b35a2404cebddeff24cd7c0aec9b5af1f45c42a39c85d31`
- Codebook whole-sheet SHA-256: `892a055512cdecccc191a768792ad1182933fb77ca3df31b2a2e4e470549d1e6`

## Design

All prompt, model, threshold, and weight decisions were made on GPT Test. GPT Test ALL was called only after those decisions were frozen, using exactly one selected model from each provider and the final prompt.

The source workbook and Codebook (revised) sheet were treated as immutable inputs. The prompt scaffold, checklist, direct baseline instruction, output request, and codebook rendering follow the latest `Unlearning_Final_FullPDF_AB_Evaluation_Pipeline.ipynb`.

## Prompt selection on GPT Test

### Examples-column A/B

| prompt_name                         | prompt_hash                                                      |   mean_precision |   mean_recall |   mean_f1 |   mean_auroc |   mean_auprc |   mean_accuracy |   mean_brier |   model_configurations |   providers | selected   |
|:------------------------------------|:-----------------------------------------------------------------|-----------------:|--------------:|----------:|-------------:|-------------:|----------------:|-------------:|-----------------------:|------------:|:-----------|
| codebook_no_examples_no_checklist   | 606c2c59c87cbb99cf42d3aac351a881ecbf0328ca0c2ef249fd9da313710dfe |         0.79385  |      0.293651 |  0.421117 |     0.692555 |     0.686579 |        0.603175 |     0.276399 |                      3 |           3 | True       |
| codebook_with_examples_no_checklist | c81e46faac5d0f8d24ff99cf635f491a89e69c02d901ccedbc210e3f59965053 |         0.751165 |      0.357143 |  0.472223 |     0.724112 |     0.716269 |        0.611111 |     0.254363 |                      3 |           3 | False      |

### Checklist A/B

| prompt_name                         | prompt_hash                                                      |   mean_precision |   mean_recall |   mean_f1 |   mean_auroc |   mean_auprc |   mean_accuracy |   mean_brier |   model_configurations |   providers | selected   |
|:------------------------------------|:-----------------------------------------------------------------|-----------------:|--------------:|----------:|-------------:|-------------:|----------------:|-------------:|-----------------------:|------------:|:-----------|
| codebook_no_examples_with_checklist | 5ef0ed097ed63718a949e101ae68ad12b372d8fb0b0f5d1f6902d6007c2fa4c9 |         0.898551 |      0.269841 |  0.399397 |     0.726096 |     0.722129 |        0.607143 |     0.279974 |                      3 |           3 | True       |
| codebook_no_examples_no_checklist   | 606c2c59c87cbb99cf42d3aac351a881ecbf0328ca0c2ef249fd9da313710dfe |         0.79385  |      0.293651 |  0.421117 |     0.692555 |     0.686579 |        0.603175 |     0.276399 |                      3 |           3 | False      |

Prompt-comparison confidence intervals and p-values are exploratory because the same GPT Test rows were used for selection.

## Selected model per provider

| provider   | run_name                               | model_requested           |   precision |   recall |       f1 |   accuracy |    auroc |    auprc |    brier |   n |   predicted_positive_count |
|:-----------|:---------------------------------------|:--------------------------|------------:|---------:|---------:|-----------:|---------:|---------:|---------:|----:|---------------------------:|
| openai     | openai_gpt_5_6_terra_low               | gpt-5.6-terra             |    1        | 0.214286 | 0.352941 |   0.607143 | 0.754252 | 0.76071  | 0.308287 |  84 |                          9 |
| anthropic  | anthropic_claude_haiku_4_5_no_thinking | claude-haiku-4-5-20251001 |    0.695652 | 0.380952 | 0.492308 |   0.607143 | 0.691043 | 0.660127 | 0.257737 |  84 |                         23 |
| google     | google_gemini_3_1_flash_lite_low       | gemini-3.1-flash-lite     |    1        | 0.214286 | 0.352941 |   0.607143 | 0.732993 | 0.74555  | 0.273899 |  84 |                          9 |

Model winner-versus-runner comparisons are also exploratory for the same selection reason.

## Threshold and weighted ensemble optimization

| system_name                            | search_type                |   n |   positive_prevalence |   threshold |   predicted_positive_count |   tn |   fp |   fn |   tp |   accuracy |   precision |   recall |       f1 |    auroc |    auprc |    brier | meets_recall_guardrail   | meets_positive_count_guardrail   | eligible_primary   | configuration         |   weight__openai_gpt_5_6_terra_low |   weight__anthropic_claude_haiku_4_5_no_thinking |   weight__google_gemini_3_1_flash_lite_low |
|:---------------------------------------|:---------------------------|----:|----------------------:|------------:|---------------------------:|-----:|-----:|-----:|-----:|-----------:|------------:|---------:|---------:|---------:|---------:|---------:|:-------------------------|:---------------------------------|:-------------------|:----------------------|-----------------------------------:|-------------------------------------------------:|-------------------------------------------:|
| openai_gpt_5_6_terra_low               | individual_model_threshold |  84 |                   0.5 |        0.13 |                         30 |   34 |    8 |   20 |   22 |   0.666667 |    0.733333 | 0.52381  | 0.611111 | 0.754252 | 0.76071  | 0.308287 | True                     | True                             | True               | individual_model      |                             nan    |                                              nan |                                     nan    |
| anthropic_claude_haiku_4_5_no_thinking | individual_model_threshold |  84 |                   0.5 |        0.26 |                         33 |   32 |   10 |   19 |   23 |   0.654762 |    0.69697  | 0.547619 | 0.613333 | 0.691043 | 0.660127 | 0.257737 | True                     | True                             | True               | individual_model      |                             nan    |                                              nan |                                     nan    |
| google_gemini_3_1_flash_lite_low       | individual_model_threshold |  84 |                   0.5 |        0.16 |                         41 |   30 |   12 |   13 |   29 |   0.702381 |    0.707317 | 0.690476 | 0.698795 | 0.732993 | 0.74555  | 0.273899 | True                     | True                             | True               | individual_model      |                             nan    |                                              nan |                                     nan    |
| equal_weight_final_prompt_ensemble     | equal_weight_threshold     |  84 |                   0.5 |        0.32 |                         26 |   37 |    5 |   21 |   21 |   0.690476 |    0.807692 | 0.5      | 0.617647 | 0.754819 | 0.784154 | 0.258881 | True                     | True                             | True               | equal_weight_ensemble |                             nan    |                                              nan |                                     nan    |
| weighted_probability_ensemble          | nan                        |  84 |                   0.5 |        0.24 |                         23 |   40 |    2 |   21 |   21 |   0.72619  |    0.913043 | 0.5      | 0.646154 | 0.758503 | 0.803991 | 0.277551 | True                     | True                             | True               | weighted_ensemble     |                               0.35 |                                                0 |                                       0.65 |

The deployment weights and threshold were selected by maximizing precision subject to recall >= 0.50 and at least 5 predicted positives.

## Optimized ensemble versus direct-only baseline on GPT Test

| system                                          |   n |   positive_prevalence |   threshold |   predicted_positive_count |   tn |   fp |   fn |   tp |   accuracy |   precision |   recall |       f1 |    auroc |    auprc |    brier |
|:------------------------------------------------|----:|----------------------:|------------:|---------------------------:|-----:|-----:|-----:|-----:|-----------:|------------:|---------:|---------:|---------:|---------:|---------:|
| direct_only_simple_average_selected_models      |  84 |                   0.5 |        0.5  |                         13 |   40 |    2 |   31 |   11 |   0.607143 |    0.846154 | 0.261905 | 0.4      | 0.673186 | 0.710252 | 0.258074 |
| locked_full_gpt_test_weighted_ensemble_apparent |  84 |                   0.5 |        0.24 |                         23 |   40 |    2 |   21 |   21 |   0.72619  |    0.913043 | 0.5      | 0.646154 | 0.758503 | 0.803991 | 0.277551 |
| oof_optimized_final_prompt_weighted_ensemble    |  84 |                 nan   |      nan    |                         23 |   37 |    5 |   24 |   18 |   0.654762 |    0.782609 | 0.428571 | 0.553846 | 0.749433 | 0.793635 | 0.278903 |

Primary performance uses out-of-fold threshold/weight tuning. This reduces post-processing optimism, but prompt and model selection were not nested inside the folds.

### Paired inference

_No rows._

### Exact McNemar test

| system_a                                   | system_b                                     |   a_correct_b_wrong |   a_wrong_b_correct |   discordant_pairs |   exact_two_sided_p_value |
|:-------------------------------------------|:---------------------------------------------|--------------------:|--------------------:|-------------------:|--------------------------:|
| direct_only_simple_average_selected_models | oof_optimized_final_prompt_weighted_ensemble |                   4 |                   8 |                 12 |                  0.387695 |

### Document-cluster bootstrap sensitivity

_No rows._

## Final GPT Test ALL application

| dataset      | system                   | system_type                           | scope                   |   n |   predicted_positive_count |   tn |   fp |   fn |   tp |   accuracy |   precision |   recall |       f1 |      auroc |      auprc |     brier |   applied_threshold |
|:-------------|:-------------------------|:--------------------------------------|:------------------------|----:|---------------------------:|-----:|-----:|-----:|-----:|-----------:|------------:|---------:|---------:|-----------:|-----------:|----------:|--------------------:|
| GPT Test ALL | locked_weighted_ensemble | locked_gpt_test_weights_and_threshold | all_rows                | 677 |                         66 |  593 |   46 |   18 |   20 |   0.905465 |    0.30303  | 0.526316 | 0.384615 |   0.866032 |   0.338944 | 0.0522616 |                0.24 |
| GPT Test ALL | locked_weighted_ensemble | locked_gpt_test_weights_and_threshold | human_labeled_only      |  79 |                         22 |   39 |    2 |   18 |   20 |   0.746835 |    0.909091 | 0.526316 | 0.666667 |   0.776958 |   0.809521 | 0.260008  |                0.24 |
| GPT Test ALL | locked_weighted_ensemble | locked_gpt_test_weights_and_threshold | review_unflagged        | 642 |                         60 |  570 |   43 |   12 |   17 |   0.91433  |    0.283333 | 0.586207 | 0.382022 |   0.892952 |   0.359784 | 0.0449556 |                0.24 |
| GPT Test ALL | locked_weighted_ensemble | locked_gpt_test_weights_and_threshold | example_leakage_safe    | 676 |                         65 |  593 |   46 |   18 |   19 |   0.905325 |    0.292308 | 0.513514 | 0.372549 |   0.862412 |   0.307633 | 0.0523362 |                0.24 |
| GPT Test ALL | locked_weighted_ensemble | locked_gpt_test_weights_and_threshold | exact_gpt_test_overlap  |  79 |                         22 |   39 |    2 |   18 |   20 |   0.746835 |    0.909091 | 0.526316 | 0.666667 |   0.776958 |   0.809521 | 0.260008  |                0.24 |
| GPT Test ALL | locked_weighted_ensemble | locked_gpt_test_weights_and_threshold | non_gpt_test_exact_text | 598 |                         44 |  554 |   44 |    0 |    0 |   0.926421 |    0        | 0        | 0        | nan        | nan        | 0.0248168 |                0.24 |

Interpret all-rows GPT Test ALL metrics with caution: rows not explicitly retained as human-labeled positives were assigned No during dataset construction, and the dataset contains exact GPT Test overlaps. Human-labeled-only, overlap, non-overlap, extraction-safe, and example-leakage-safe scopes are reported separately.

The direct-only baseline was not rerun on GPT Test ALL; the requested baseline comparison is performed on GPT Test, while the final all-corpus call remains selected-model-only.

## Integrity and reproducibility

| stage                                     | dataset      | prompt_names                                                           | run_names                                                                                          |   expected_materialized_rows |   observed_materialized_rows |   missing_rows |   duplicate_materialized_keys | complete   |
|:------------------------------------------|:-------------|:-----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|-----------------------------:|-----------------------------:|---------------:|------------------------------:|:-----------|
| stage1_examples_ab_gpt_test               | GPT Test     | codebook_no_examples_no_checklist; codebook_with_examples_no_checklist | openai_gpt_5_6_terra_low; anthropic_claude_haiku_4_5_no_thinking; google_gemini_3_1_flash_lite_low |                          504 |                          504 |              0 |                             0 | True       |
| stage2_checklist_ab_gpt_test              | GPT Test     | codebook_no_examples_no_checklist; codebook_no_examples_with_checklist | openai_gpt_5_6_terra_low; anthropic_claude_haiku_4_5_no_thinking; google_gemini_3_1_flash_lite_low |                          504 |                          504 |              0 |                             0 | True       |
| final_prompt_all_candidates_gpt_test      | GPT Test     | codebook_no_examples_with_checklist                                    | openai_gpt_5_6_terra_low; anthropic_claude_haiku_4_5_no_thinking; google_gemini_3_1_flash_lite_low |                          252 |                          252 |              0 |                             0 | True       |
| selected_models_final_prompt_gpt_test     | GPT Test     | codebook_no_examples_with_checklist                                    | openai_gpt_5_6_terra_low; anthropic_claude_haiku_4_5_no_thinking; google_gemini_3_1_flash_lite_low |                          252 |                          252 |              0 |                             0 | True       |
| selected_models_direct_baseline_gpt_test  | GPT Test     | direct_target_only                                                     | openai_gpt_5_6_terra_low; anthropic_claude_haiku_4_5_no_thinking; google_gemini_3_1_flash_lite_low |                          252 |                          252 |              0 |                             0 | True       |
| selected_models_final_prompt_gpt_test_all | GPT Test ALL | codebook_no_examples_with_checklist                                    | openai_gpt_5_6_terra_low; anthropic_claude_haiku_4_5_no_thinking; google_gemini_3_1_flash_lite_low |                         2031 |                         2031 |              0 |                             0 | True       |

| object                         | hash_at_load                                                     | hash_at_final_audit                                              | unchanged   |
|:-------------------------------|:-----------------------------------------------------------------|:-----------------------------------------------------------------|:------------|
| archived_source_workbook       | a148051e24ccab080b35a2404cebddeff24cd7c0aec9b5af1f45c42a39c85d31 | a148051e24ccab080b35a2404cebddeff24cd7c0aec9b5af1f45c42a39c85d31 | True        |
| Codebook (revised) whole sheet | 892a055512cdecccc191a768792ad1182933fb77ca3df31b2a2e4e470549d1e6 | 892a055512cdecccc191a768792ad1182933fb77ca3df31b2a2e4e470549d1e6 | True        |

Raw provider responses are checkpointed to append-only JSONL immediately after each call. Run keys include model settings, prompt hash, schema hash, exact normalized paragraph hash, and replicate number. Exact GPT Test passages are reused in GPT Test ALL without another API call.
Hosted LLM APIs are not guaranteed to return bit-for-bit identical outputs on a completely fresh rerun. Reproducibility here therefore means fixed inputs/settings plus preservation and reuse of the exact raw responses that generated the reported results.

## Key files

- GPT Test manual review: `/content/drive/MyDrive/Unlearning_Paragraph_Level_LLM_Experiment/paragraph_level_gpt_test_first_v2_20260821/exports/GPT_Test_Selected_Models_and_Ensembles_Manual_Review.xlsx`
- GPT Test ALL final results: `/content/drive/MyDrive/Unlearning_Paragraph_Level_LLM_Experiment/paragraph_level_gpt_test_first_v2_20260821/exports/GPT_Test_ALL_Final_Selected_Models_Locked_Ensemble.xlsx`
- Comprehensive Excel report: `/content/drive/MyDrive/Unlearning_Paragraph_Level_LLM_Experiment/paragraph_level_gpt_test_first_v2_20260821/reports/Unlearning_Experiment_Comprehensive_Report.xlsx`
