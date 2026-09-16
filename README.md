# Joomla Component Builder: Contextual Compilation Architecture

**A technical white paper by Llewellyn van der Merwe**  
Published by Vast Development Method · Architecture edition 1.0.0 · 16 September 2026

**Publication:** https://architecture.joomlacomponentbuilder.com  
**Official implementation:** https://github.com/joomengine/Joomla-Component-Builder

This publication explains how Joomla Component Builder turns structured development intent into complete native extensions. The compiler is the centre of the account: it acquires definitions and dependencies, interprets their uses in context, distributes their consequences into specialised intermediate stores, completes deferred work, and materialises components, modules, and plugins through ordered generation stages.

Blueprint export, repository discovery, local import, installed-component extrusion, and regeneration connect that compiler to a larger development lifecycle. Definitions are portable working knowledge; generated applications are deployable products. Their relationship is demonstrated using the Hello World blueprint and its three generated extension repositories.

The white paper expresses these mechanisms through language-neutral definitions, transition systems, graphs, equations, pseudocode, and worked traces. Source correspondence and primary references accompany the explanation. The formal model describes the architecture rather than replacing it with an unrelated idealised compiler.

## Reading

Start with the [overview](DOCS/index.md), [white paper](DOCS/white-paper.md), and [reading guide](DOCS/reading-guide.md). All articles are authored in `DOCS/`. The website provides an exact Markdown alternate for every article, a complete Markdown edition, a ZIP of the article sources, an article manifest with SHA-256 hashes, a search index, and a machine-readable full-text corpus.

The reading path covers the model and its identity system, blueprint exchange, compiler execution, generated application concerns, installed-component extrusion, public worked examples, formal semantics, and implementation guidance. The reference section supplies source maps, terminology, provenance, and the bibliography.

## Build and validate

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m unittest discover -s tests -v
python examples/demo.py
python scripts/vendor.py
python scripts/prepare_evidence.py
python scripts/build.py
python scripts/check_site.py
python -m playwright install chromium
python scripts/browser_check.py
python scripts/archive.py
python -m http.server 8000 --directory site
```

The reference demonstration exercises discrete mechanisms explained in the paper. It is not a replacement for installing Joomla and running the full compiler. The publication checks validate article structure, exact Markdown alternatives, links and anchors, mathematics, diagrams, search, theme selection, and desktop/mobile rendering.

GitHub Actions validates pull requests without publishing them. Only a successful build of `main` can deploy through GitHub Pages. Repository-side domain configuration is generated from `site.json`; Pages settings and DNS must separately point to the intended domain.

## Authorship and reuse

The architecture and explanatory account are by **Llewellyn van der Merwe**. **Vast Development Method** publishes the work. The account preserves the architecture's independent development history and credits established research where the mechanisms have retrospective correspondences.

Original prose, mathematical exposition, and authored diagrams are licensed under [CC BY 4.0](LICENSE). Publication tooling and executable reference examples are under [MIT](LICENSES/MIT.txt). VDM branding and identified third-party materials retain their respective notices. Source references do not transfer ownership of upstream work.

Use [CITATION.cff](CITATION.cff) for citation metadata. The version identifies this architectural publication, not a Joomla Component Builder software release.
