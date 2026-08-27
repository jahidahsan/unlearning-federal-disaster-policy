
# Data Directory

- `codebooks/current/` contains the confirmed current integrated human-annotation/codebook workbook.
- `codebooks/historical/` contains major old, Target-based pre-final, and integrated annotation milestones.
- `benchmarks/current/` contains the current strict paragraph-aligned GPT Test and GPT Test ALL workbook.
- `benchmarks/historical/` contains major curation, EPA re-evaluation, Kyle-only-removal, local-context, and initial-pilot milestones.
- `source_documents/` contains the five private source PDFs used for paragraph extraction.
- `source_selection/` contains the broader initial document-discovery registry.
- `manifests/` records source-document and dataset-version hashes.

The exact input used by a completed experiment remains inside that experiment folder, even when a newer canonical benchmark exists.
