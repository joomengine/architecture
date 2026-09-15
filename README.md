# Vast Development Method Theory

**VDMT — a formal framework for contextual recollection, staged synthesis, and persistent editorial reconciliation.**

**Originator:** Llewellyn van der Merwe · **Publisher:** Vast Development Method  
**Publication:** https://theory.vdm.io · **Specification:** 0.1.0 · **Document edition:** 15 September 2026

VDMT describes how a system gathers a structured context, follows dependencies revealed by that context, recollects and derives information in scoped stores, expands reusable definitions into distinct occurrences, binds that information into artifacts in ordered stages, and preserves explicitly marked human adaptations across regeneration. It is language-independent: PHP, Joomla, files, and string placeholders are implementation choices rather than its mathematical definition.

The key abstraction is **contextual closure followed by staged materialization, with a persistent, explicitly bounded feedback path**. The inner loop completes the knowledge required for a build. The outer loop incorporates admissible edits between builds. These loops have different state spaces and different correctness conditions; treating them as one unrestricted recursion obscures the architecture.

## Read the work

Start with [the overview](DOCS/index.md), the [white paper](DOCS/white-paper.md), and the [reading guide](DOCS/reading-guide.md). The complete Markdown corpus is in **`DOCS/`**. Every published article has its own same-origin Markdown URL, a Markdown download action, source link, citation information, and stable HTML URL. The build also produces a complete Markdown edition, an article manifest with SHA-256 hashes, an `llms.txt` index, and a full-text research corpus. Markdown is the source of truth, not an export maintained separately from the website.

The publication separates:

* **Foundations and semantics:** typed state, context closure, guarded derivation, fixed points, determinism, confluence, composition, and termination.
* **Mechanisms:** contextual memory, nested gathering, definition/occurrence identity, hierarchical reuse, staged binding, materialization, round-trip editing, reconciliation, invalidation, provenance, and self-generation.
* **Evidence and evaluation:** the JCB implementation case study, historical source, related work, reference-model tests, performance methodology, cognitive hypotheses, and review obligations.

## First disclosed implementation

The method is publicly embodied in **Joomla Component Builder**, developed by Llewellyn van der Merwe. The authoritative repository is [joomengine/Joomla-Component-Builder](https://github.com/joomengine/Joomla-Component-Builder).

Its root commit, [`ecf47809f960bd057af8a414168fada6fe22c5f7`](https://github.com/joomengine/Joomla-Component-Builder/commit/ecf47809f960bd057af8a414168fada6fe22c5f7), records **30 January 2016, 20:28:43 UTC** (22:28:43 at UTC+02:00), names Llewellyn van der Merwe as author and committer, and is titled “first commit of free version.” The [compiler in that same commit](https://github.com/joomengine/Joomla-Component-Builder/blob/ecf47809f960bd057af8a414168fada6fe22c5f7/admin/helpers/compiler.php) already contains specialized builder arrays, static/dynamic content stores, database loading, staged file construction, and a later file-update pass. The provenance therefore rests on executable source, **not on the GPL license text alone**.

**30 January 2016 is the historical public-source provenance date of the method's implementation.** This repository's 2026 edition formalizes and names its abstractions; it does not backdate this manuscript, the present class layout, or every subsequently introduced feature. The author places private development approximately two years before public release and reports independent development without prior awareness of the related theories surveyed here. Those recollections are identified as author testimony, while earlier mathematical and architectural work is explicitly credited. See [provenance](DOCS/foundations/provenance.md).

The contemporary case study is pinned to JCB commit `bca4a1520484f3e2c2fbd12964a5995b0d058de1`. JCB is the originating implementation studied here, not a dependency of VDMT and not a claim that no comparable earlier systems existed.

## Scientific status

This is a research white paper and formal architectural specification, **not a claim of an awarded doctorate or completed peer review**. Conditional propositions are proved for the explicitly defined model. Observations of JCB, author reports, mathematical deductions, proposed extensions, and empirical hypotheses are labeled separately. In particular, self-generation does not establish Turing completeness, and neither source inspection nor an impressive line-count expansion establishes universal performance or cognitive optimality.

The reported 30,000-to-1.3-million-line build in approximately 60 seconds is retained as an author-reported observation with a reproducibility protocol, not relabeled as a benchmark conducted for this paper.

## Build and test

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/vendor.py
python scripts/build.py
python scripts/check_site.py
python -m http.server 8000 --directory site
```

The reference model is runnable with `python examples/demo.py`. It is deliberately smaller than JCB and tests the abstract laws rather than pretending to reproduce Joomla compilation. See [implementation guidance](DOCS/engineering/implementation-guide.md).

GitHub Actions builds and tests pull requests without publishing them. A merge to `main` publishes the checked `site/` artifact through GitHub Pages. Repository Pages settings and DNS must select `theory.vdm.io`; the `CNAME` file alone does not configure those services. See [publication and maintenance](DOCS/reference/publication.md).

## Attribution and licenses

Original explanatory prose, mathematical exposition, and authored diagrams: **[CC BY 4.0](LICENSE)**. Original website tooling and executable reference examples: **[MIT](LICENSES/MIT.txt)**. VDM brand assets and separately identified third-party material retain their own rights and notices.

Suggested citation:

> van der Merwe, Llewellyn. *Vast Development Method Theory: Contextual Recollection, Staged Synthesis, and Persistent Editorial Reconciliation*. Version 0.1.0, Vast Development Method, 2026. https://theory.vdm.io. Historical public implementation: Joomla Component Builder, 30 January 2016.

Use `CITATION.cff` for machine-readable attribution. CC BY retains copyright and requires attribution for reuse of the licensed expression; it does not create exclusive ownership of mathematical ideas or independently implemented algorithms. See [the licensing analysis](DOCS/reference/licensing.md).
