# Contributing to VDMT

The paper welcomes criticism, counterexamples, independent implementations, source corrections, and reproducible measurements. Agreement with the author's hypotheses is not a condition of contribution.

## One article, one source

Write each article in `DOCS/` as UTF-8 Markdown. Include YAML front matter with `title`, `description`, `section`, `order`, and `evidence`. Give the page one H1, then descriptive H2/H3 sections. Use ordinary relative `.md` links, fenced code, and `$...$` / `$$...$$` mathematics. Do not maintain separate HTML prose or separate hand-edited Markdown exports. The build creates both from the same source and checks their correspondence.

A new nuance should receive a focused article when it has its own definitions, assumptions, example, failure conditions, or evidence. Link it to its prerequisites and implications. Do not split a sentence into several pages merely to inflate the count.

## Evidence discipline

Label claims using the taxonomy in `DOCS/foundations/epistemic-status.md`. Source observations require a repository revision, path, relevant method or line range, and an explanation of what was inspected. Experiments require input and environment descriptions and a procedure that another researcher can run. Propositions require all assumptions and an argument; a test does not become a proof by passing. Cite prior work at the point of comparison.

Do not silently promote a proposed feature to an observed JCB property. Do not equate the historical public implementation date with the date of this manuscript. Do not use a marketing claim or a generated line count as evidence of cognitive optimality.

## Review workflow

Create a branch from `main`. Make focused commits, run the repository tests, build the publication, and open a pull request explaining substantive changes. A formal change should state which definitions and propositions depend on it. A source correction should state whether it affects an implementation observation or the abstract specification. A historical correction must retain a transparent record of the prior wording.

PRs are checked but never deployed to the public domain. Only an approved merge to `main` publishes. Large changes to definitions should increment the specification version and explain compatibility.

## Rights and attribution

Contribute only material you have the right to share. Contributions to original paper text and diagrams are offered under CC BY 4.0; original software contributions under MIT. Contributors retain their own copyright unless separately agreed. Preserve upstream rights for quotations and dependencies. Do not add invented author identities, institutional affiliations, degrees, ORCID identifiers, DOIs, or publication dates.

The theory's originator is Llewellyn van der Merwe. Maintain that attribution without erasing the contributions of collaborators or the priority of related published work.
