
# Public Release Checklist

Do not make the repository public until every applicable item is complete.

## Scientific verification

- [ ] Team confirms the canonical codebook and benchmark hashes.
- [ ] Results intended for publication use the correct stated codebook version.
- [ ] The completed LangChain experiment is either added and reviewed or explicitly outside the public release.
- [ ] Nonfatal evidence-quote and target-consistency flags are adjudicated or clearly disclosed.
- [ ] GPT Test ALL is not misrepresented as fully human-adjudicated.
- [ ] Historical/provisional results are clearly separated from final evidence.
- [ ] Tables and narrative claims match the underlying CSV/Excel outputs.

## Data and privacy

- [ ] Team approves whether human labeler names remain visible.
- [ ] Raw provider request identifiers, cost data, and absolute Drive paths are reviewed.
- [ ] No confidential comments, emails, or internal-only notes are present.
- [ ] A full secrets scan passes.

## Copyright and licensing

- [ ] Redistribution rights are checked for each source PDF, especially the journal article.
- [ ] Source PDFs without clear redistribution permission are replaced by citations, URLs, filenames, and checksums.
- [ ] A code license is selected.
- [ ] A data license or data-use statement is selected.
- [ ] `CITATION.cff` and a public citation are added after team approval.

## Repository quality

- [ ] `python scripts/validate_repository.py` passes.
- [ ] All current notebooks contain outputs and complete without unresolved errors.
- [ ] The README reflects the public release rather than the private verification snapshot.
- [ ] Large binary files are moved to Git LFS or a release/archive service if needed.
- [ ] A versioned GitHub release and immutable archive are created.
