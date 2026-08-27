
# Decision Log

## D001 — Use targets rather than the original pillars

**Decision:** use Leadership; Laws, Plans, and Policies; Capabilities; Funds and Resource Allocation; and Miscellaneous Organizational as the target taxonomy, with the affected government agency recorded separately.

**Rationale:** the targets identify what an institution is being asked to abandon or fundamentally rethink. This was more operational for paragraph coding than broad epistemic, normative, technical, and integrative pillars.

## D002 — Retain old and new gold labels

**Decision:** preserve both old and new gold-label columns in the benchmark.

**Rationale:** codebook refinement and later adjudication changed some labels. Keeping both versions allows historical results to be interpreted against the labels that existed at the time and makes codebook A/B comparisons auditable.

## D003 — Remove Kyle-only rows from the primary curated benchmark

**Decision:** exclude rows labeled only by Kyle while retaining rows also reviewed by Anmol or Prerana.

**Rationale:** the final benchmark prioritized the reviewed/adjudicated label set rather than treating all isolated labels as equivalent gold. Individual labeler columns were retained so performance by labeler could still be examined.

## D004 — Incorporate Prerana’s EPA re-evaluation

**Decision:** revise the EPA labels after re-review under the updated codebook and preserve the earlier labels in the old-gold fields.

**Rationale:** the stricter unlearning boundary distinguishes problem diagnosis, additive reform, and routine improvement from deliberate subtraction or discontinuity. EPA passages were a major source of disagreement under the earlier interpretation.

## D005 — Align excerpts to complete source paragraphs

**Decision:** reconcile curated excerpts against PyMuPDF-extracted source text, split multi-paragraph spans, and flag uncertain extraction matches.

**Rationale:** paragraph-level evaluation is only defensible when each row represents a complete and traceable unit of analysis. The alignment step also produced an extraction audit rather than silently accepting imperfect matches.

## D006 — Separate GPT Test from GPT Test ALL

**Decision:** make prompt, model, threshold, and weight decisions on GPT Test, then apply a frozen configuration to GPT Test ALL.

**Rationale:** this prevents iterative use of the full corpus from influencing configuration choices and gives the final deployment a clear audit trail.

## D007 — Do not use examples in the Aug. 23 locked prompt

**Decision:** select the no-examples condition for the Aug. 23 run.

**Rationale:** the prespecified comparison prioritized precision. No examples produced higher mean precision across the three selected provider configurations, although examples produced higher recall, F1, AUROC, and AUPRC. The decision should therefore be described as objective-dependent, not as proof that examples were uniformly worse.

## D008 — Use the checklist in the Aug. 23 locked prompt

**Decision:** select the checklist condition.

**Rationale:** the checklist raised mean precision and strengthened explicit checks for a prior practice, inadequacy, and subtraction/discontinuity. It lowered mean recall and F1 at the default threshold, so it was retained for a precision-oriented screening objective rather than because it improved every metric.

## D009 — Select one model per provider

**Decision:** retain one OpenAI, one Anthropic, and one Google model before ensemble tuning.

**Rationale:** this reduced the final deployment grid, kept provider comparison interpretable, and avoided overweighting providers with more candidate models.

## D010 — Tune with guardrails rather than maximize precision without constraint

**Decision:** maximize precision subject to recall of at least 0.50 and at least five predicted positives; then estimate post-processing performance out of fold.

**Rationale:** unconstrained precision can be achieved by predicting very few positives. The guardrails forced the selected configuration to retain a minimum level of case discovery.

## D011 — Preserve the Aug. 23 run’s exact codebook wording

**Decision:** do not replace the run input with the later strict workbook.

**Rationale:** the Aug. 23 run used the correct Target-based taxonomy but an earlier wording revision of the binary definition. Replacing the file would break provenance. Future runs use the strict canonical workbook and receive a new experiment ID.

## D012 — Do not version unfinished LangChain results

**Decision:** defer the retrieval experiment until its notebook has stored outputs and the run package is complete.

**Rationale:** partial provider coverage—especially a rate-limit interruption—cannot be treated as a completed, reviewable experiment.

## D013 — Private-first repository

**Decision:** keep this repository private until data, results, licenses, source-document redistribution, identifiers, and interpretation are verified by the team.

**Rationale:** the repository contains source PDFs, human-label provenance, raw model responses, historical drafts, and provisional analyses that require team review before public release.
