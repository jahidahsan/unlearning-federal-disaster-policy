
# Latest Results Guide

This guide summarizes the generated Aug. 23 report without replacing the underlying tables.

## Prompt-factor decisions on GPT Test

### Examples

- No examples: mean precision 0.794, recall 0.294, F1 0.421, AUROC 0.693.
- With examples: mean precision 0.751, recall 0.357, F1 0.472, AUROC 0.724.

The no-examples condition was selected because the comparison objective prioritized precision. Examples were better on several other metrics, so the result is a trade-off rather than a universal rejection of examples.

### Checklist

- Checklist: mean precision 0.899, recall 0.270, F1 0.399, AUROC 0.726.
- No checklist: mean precision 0.794, recall 0.294, F1 0.421, AUROC 0.693.

The checklist was selected for the precision-oriented objective and because it formalized the intended evidence boundary. It did not improve every default-threshold metric.

## Selected model per provider at threshold 0.5

| Provider | Model | Precision | Recall | F1 | AUROC |
|---|---|---:|---:|---:|---:|
| OpenAI | GPT-5.6 Terra, low reasoning | 1.000 | 0.214 | 0.353 | 0.754 |
| Anthropic | Claude Haiku 4.5, no thinking | 0.696 | 0.381 | 0.492 | 0.691 |
| Google | Gemini 3.1 Flash-Lite, low thinking | 1.000 | 0.214 | 0.353 | 0.733 |

## Locked ensemble

- Threshold: 0.24
- OpenAI weight: 0.35
- Anthropic weight: 0.00
- Gemini weight: 0.65
- Selection objective: maximize precision subject to recall ≥ 0.50 and at least five predicted positives.

### Apparent GPT Test performance

Precision 0.913, recall 0.500, F1 0.646, AUROC 0.759, and AUPRC 0.804.

### Out-of-fold post-processing estimate

Precision 0.783, recall 0.429, F1 0.554, AUROC 0.749, and AUPRC 0.794.

### Direct-only simple-average baseline

Precision 0.846, recall 0.262, F1 0.400, AUROC 0.673, and AUPRC 0.710.

## Interpretation boundary

The out-of-fold estimate reduces optimism from threshold and weight tuning, but prompt and model selection were not nested inside the folds. The same GPT Test rows informed several decisions, so prompt-comparison intervals and p-values are exploratory. GPT Test ALL is mostly operational default-No and should be used primarily for locked-corpus screening, review prioritization, and descriptive deployment analysis—not as an independent fully adjudicated test set.

For exact tables and audits, use `experiments/2026-08-23_gpt-test-first/reports/Unlearning_Experiment_Report.md` and the CSV/Excel outputs in that experiment folder.
