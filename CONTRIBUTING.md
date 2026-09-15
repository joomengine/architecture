# Contributing to the architectural publication

This repository documents Joomla Component Builder's architecture. Proposed compiler changes belong in the official implementation repository; the white paper should explain implemented behaviour rather than quietly prescribe a different system.

## Editorial standard

Keep the compiler at the centre. Connect a mechanism's problem, operation, state, mathematical description, worked example, and source correspondence. Prefer precise ordinary terminology before introducing specialised notation. Define symbols once and use them consistently.

Preserve the distinction between definitions, contextual occurrences, intermediate contributions, emitted artifacts, and repository indexes. Describe the actual ordering and effects of the implementation. Do not infer universal confluence, transactional publication, immutable stores, or a general inverse compiler from mechanisms that do not supply those guarantees.

Describe measured builds with their input and output boundaries. Do not present generated volume as manually written code, or convert repeated engineering measurements into conjectures. Distinguish an archival artifact comparison from a fresh runtime compilation.

## Sources and references

Compiler citations use the official Joomla Component Builder repository and immutable revisions. A cited file must support the nearby statement. Newer implementation coverage must identify its edition scope rather than attribute absent code to an older revision. Public examples and documentation retain their own repository identities.

Credit primary research and official documentation for architectural correspondences. Preserve independent development history without inventing either intellectual influence or historical priority. Comparisons should explain mechanisms, not rank products.

## Article and website contract

Every article belongs in `DOCS/`, has YAML metadata, exactly one first-level heading, a stable path, a description, a section, and a reading order. Relative links to other articles use `.md` paths. Inline mathematics uses `$...$`, display mathematics uses `$$...$$`, and diagrams use fenced `mermaid` blocks. Explain figures in prose as well.

The build must publish exact source bytes as the Markdown alternate. Search, downloads, the article manifest, citation metadata, and canonical URLs must all agree with `site.json`. Keep navigation keyboard-accessible and mathematical content usable on narrow screens. Retain the small VDM mark and text-based JCB architecture identity; do not restore the oversized homepage wordmark.

Run the complete checks in `README.md`. Submit coherent commits on a review branch and record the validation scope in the pull request. Do not merge or change production hosting as a side effect of editorial work.
