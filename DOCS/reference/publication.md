---
title: Publication, downloads, and maintenance
description: The Markdown-first website contract, domain configuration, reproducible build, review artifacts, and deployment boundary.
section: Reference
order: 95
evidence: Repository tooling and official hosting documentation
---
# Publication, downloads, and maintenance

The publication is authored in Markdown under `DOCS/`. HTML pages, navigation, search, downloadable editions, and machine-readable indexes are generated from that source. A second independently maintained prose version is not required.

`site.json` supplies the title, author, publisher, edition, canonical domain, repository, and reading sections. The template uses text-based JCB architecture headings and retains the small VDM mark. System-following light/dark mode and an explicit user override are part of the reading interface.

## Every article has an exact Markdown equivalent

An article at `DOCS/compiler/binding.md` is published as an HTML page at `/compiler/binding/` and an exact source alternate at `/markdown/compiler/binding.md`. The page's Markdown action and alternate metadata point to that source. The build preserves the Markdown bytes, including front matter, rather than reconstructing prose from HTML.

Article-to-article links in source use relative `.md` paths. The renderer resolves them to the correct HTML destinations while the source remains usable as a connected Markdown corpus. Heading anchors, descriptions, and reading order are checked during publication.

## Complete editions and indexes

The build produces:

| Artifact | Purpose |
| --- | --- |
| `/downloads/jcb-architecture-complete.md` | A combined reading edition |
| `/downloads/jcb-architecture-markdown.zip` | All article sources in their directory structure |
| `/articles.json` | Article metadata, canonical/Markdown addresses, and SHA-256 hashes |
| `/search.json` | Searchable titles, descriptions, and article text |
| `/llms.txt` | Machine-readable publication entry points |
| `/llms-full.txt` | Full-text corpus for tools and offline analysis |
| `/sitemap.xml` | Canonical public page locations |

The article-level Markdown alternate remains the exact source. The combined reading edition can add separators and rewritten cross-article addresses for usability; it is not substituted for the source hash of an individual article.

## Build and inspect locally

From a checkout of the publication repository:

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

The vendor step acquires the pinned browser dependencies and records their hashes. Mathematical rendering uses the selected MathJax SVG output; diagrams use the pinned Mermaid bundle. The publication does not require a hosted third-party rendering service for each reader's equation or diagram.

## Pull-request validation and production deployment

The workflow archives the reviewed source before running the checks. It then tests the executable mechanisms and publication tooling, runs the demonstration, builds the site, checks article/Markdown consistency, and tests browser behavior. Review artifacts include the built site archive and validation evidence.

Pull requests do not deploy. Only a successful build of `main` reaches the GitHub Pages deployment job. The maintainer reviews and merges the branch; editorial work does not independently change the production domain or release the compiler.

## Domain configuration

The intended address is **`architecture.joomlacomponentbuilder.com`**. The repository generates its canonical addresses and a descriptive `CNAME` artifact from `site.json`. With a custom GitHub Actions Pages deployment, GitHub's repository Pages setting—not that generated file—controls the custom-domain association.

The maintainer should configure/verify the custom domain in GitHub Pages and create the subdomain's DNS CNAME pointing to **`joomengine.github.io`**, without a repository suffix. HTTPS activation and DNS validation are hosting operations separate from the source rewrite. Follow the [official GitHub custom-domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

Do not leave an unclaimed DNS alias pointing at a disabled Pages site. Retaining an old address as a redirect requires control of that old host; the new publication cannot create an HTTP redirect on another domain merely by changing its canonical URL.

## Edition history and maintenance

The earlier manuscript remains in repository history at `c833d39f606d2b237eeaecbd5c41a350dde823cb`. This edition replaces its framing and article structure while retaining useful publishing infrastructure, attribution, and research references.

When implementation changes, update the affected source correspondence, worked trace, and mathematical assumptions together. When only a publication URL changes, update the canonical configuration, citation metadata, downloads, and generated indexes consistently. Stable article paths and explicit edition records make those changes inspectable.

The [verification guide](../engineering/verification.md) distinguishes publication integrity from source, artifact, and runtime verification. A successful site build establishes that the explanation is published correctly; it is not a substitute for testing the compiler's generated applications.
