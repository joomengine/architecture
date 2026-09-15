---
title: Sources and bibliography
description: Pinned implementation evidence, scholarly precedents, official technical documentation, and licensing sources.
section: Reference
order: 100
evidence: Source catalogue
---
# Sources and bibliography

## How to use these references

J-series entries identify implementation evidence; R-series entries identify prior work and technical references; L-series entries identify rights and publication guidance. Source observations cite exact repository revisions. Literature comparisons use published papers, author/institutional records, and official documentation. A linked reference is not a claim that every statement in it was independently reproduced or that this is an exhaustive systematic review.

Contemporary JCB revision: `bca4a1520484f3e2c2fbd12964a5995b0d058de1`. Historical revision: `ecf47809f960bd057af8a414168fada6fe22c5f7`. Access/review date for this edition: 15 September 2026.

## J01

Llewellyn van der Merwe. **First commit of free version**, Joomla Component Builder, 30 January 2016, 20:28:43 UTC. Root commit, no parents.

[Commit](https://github.com/joomengine/Joomla-Component-Builder/commit/ecf47809f960bd057af8a414168fada6fe22c5f7) · [License in the same tree](https://github.com/joomengine/Joomla-Component-Builder/blob/ecf47809f960bd057af8a414168fada6fe22c5f7/LICENSE.txt).

Supports repository-recorded date, authorship, and public-source lineage; the executable architectural evidence is J02.

## J02

Llewellyn van der Merwe. **Historical compiler**, `admin/helpers/compiler.php`, JCB root revision. Header, builder properties, constructor, and `buildComponent()`.

[Source](https://github.com/joomengine/Joomla-Component-Builder/blob/ecf47809f960bd057af8a414168fada6fe22c5f7/admin/helpers/compiler.php#L1-L220).

Supports specialized builder arrays, static/dynamic content memory, component data loading, staged structure/content preparation, and later file updating in the 2016 implementation.

## J03

Joomla Component Builder. **README**, contemporary pinned revision.

[Source](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/README.md).

Project documentation for self-generation, reuse, custom-code round trips, and project-domain navigation. Performance language in project documentation remains a project report rather than an independently conducted benchmark.

## J04

JCB. **Compiler initialization**, `Compiler/Initializer.php` under `libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/`.

[Source](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Initializer.php).

Inspected `init()`, `extractCustomCode()`, `buildComponent()`, version handling, directory reset, default bindings, and structure-building methods.

## J05

JCB. **Component state and data enrichment**.

[Component registry](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Component.php) · [Component data](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Component/Data.php#L350-L575).

Inspected load-once component build, joined query, and `energize()` enrichment calls.

## J06

JCB. **Content environments and infusion**.

[ContentOne](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Builder/ContentOne.php) · [ContentMulti](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Builder/ContentMulti.php) · [Infusion excerpt](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Helper/Infusion.php#L50-L220).

Supports key modeling, view scoping, and transformation of component/placeholder values into output-binding memory.

## J07

JCB. **File updating and content emission**.

[Updater](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Extension/Files/Updater.php) · [Dynamic files](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Extension/Files/Dynamic.php) · [FileContent::set](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Extension/FileContent.php#L140-L225).

Supports late dependency work, view-specific file processing, shared-before-local binding, subsequent injection, writing, and newline counting.

## J08

JCB. **Placeholder operations and tracking-marker construction**.

[Source](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Placeholder.php#L290-L485).

Inspected `update()`, `update_()`, and the beginning of `keys()`. Action 3 filters replacement entries absent from the input; it is not a universal unresolved-token validator.

## J09

JCB. **Field acquisition, reuse, and contextual processing**.

[Source](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Field/Data.php#L170-L360).

Inspected indexed retrieval, context-sensitive updating, ID/GUID resolution, guarded remote retry, and field-type join.

## J10

JCB. **Admin-view relationships**.

[Source](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Model/Adminviews.php#L90-L250).

Supports relationship-specific configuration, view enumeration, and nested retrieval of referenced view data.

## J11

JCB. **Installed custom-code extraction**.

[Source](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler/Customcode/Extractor.php).

Inspected marker/state definitions, active-path/file-type enumeration, `run()`, and the beginning of `searchFileContent()`, including GUI delegation, reverse transformation, code capture, insert/update buffers, and contextual fingerprints.

## J12

JCB. **Compiler finalization and packaging orchestration**.

[Source](https://github.com/joomengine/Joomla-Component-Builder/blob/bca4a1520484f3e2c2fbd12964a5995b0d058de1/libraries/vendor_jcb/VDM.Joomla/src/Componentbuilder/Compiler.php).

Inspected constructor and `run()` ordering, including initialization, inherited infusion, file updates, custom-code handling, language/auxiliary output, and packaging.

## R01

Alfred Tarski. **A lattice-theoretical fixpoint theorem and its applications.** *Pacific Journal of Mathematics* 5(2), 285–309, 1955. DOI: [10.2140/pjm.1955.5.285](https://doi.org/10.2140/pjm.1955.5.285). [Journal archive](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-5/issue-2/A-lattice-theoretical-fixpoint-theorem-and-its-applications/pjm/1103044538.full).

Mathematical precedent for monotone fixed-point reasoning. The finite proofs in this paper are presented explicitly and do not claim novelty for that foundation.

## R02

Donald E. Knuth. **Semantics of context-free languages.** *Mathematical Systems Theory* 2, 127–145, 1968. DOI: [10.1007/BF01692511](https://link.springer.com/article/10.1007/BF01692511).

Precedent for attributed structures and inherited/synthesized information. Consult the later correction when studying the original formal development.

## R03

J. Nathan Foster, Michael B. Greenwald, Jonathan T. Moore, Benjamin C. Pierce, and Alan Schmitt. **Combinators for bidirectional tree transformations: A linguistic approach to the view-update problem.** *ACM Transactions on Programming Languages and Systems* 29(3), Article 17, 2007; conference predecessor at POPL 2005. DOI: [10.1145/1232420.1232424](https://doi.org/10.1145/1232420.1232424). [Author-institution account of the 2005 paper](https://www.cs.cornell.edu/information/news/newsitem1371/nate-foster-wins-2015-popl-most-influential-paper-award).

Closest formal comparison for source/view update laws; not evidence that JCB implements a general lens calculus.

## R04

Andrey Mokhov, Neil Mitchell, and Simon Peyton Jones. **Build systems à la carte.** *Proceedings of the ACM on Programming Languages* 2(ICFP), Article 79, 2018. DOI: [10.1145/3236774](https://doi.org/10.1145/3236774). [Authors' institutional publication page](https://www.microsoft.com/en-us/research/publication/build-systems-la-carte/).

Comparison for dependency discovery, scheduling, and rebuilding decisions.

## R05

Todd J. Green, Grigoris Karvounarakis, and Val Tannen. **Provenance semirings.** *Proceedings of PODS*, 2007. DOI: [10.1145/1265530.1265535](https://doi.org/10.1145/1265530.1265535).

Prior formal work on the provenance of combinations and alternatives of contributing data. The proposed VDMT provenance graph is not claimed to implement the full semiring framework.

## R06

GNU Compiler Collection. **Installing GCC: Building.** [Official bootstrap documentation](https://gcc.gnu.org/install/build.html).

Methodological comparison for successive-stage compiler builds and comparisons; not a claim that JCB compiles PHP or follows GCC's exact bootstrap procedure.

## R07

Ken Thompson. **Reflections on trusting trust.** *Communications of the ACM* 27(8), 761–763, 1984. DOI: [10.1145/358198.358210](https://doi.org/10.1145/358198.358210).

Compiler-trust precedent: successful self-reproduction is not by itself a security proof.

## R08

H. Penny Nii. **The Blackboard Model of Problem Solving and the Evolution of Blackboard Architectures, Part One.** *AI Magazine* 7(2), 38–53, 1986. DOI: [10.1609/aimag.v7i2.537](https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v7i2.537).

Architectural comparison for shared problem state and specialized knowledge sources. The article identifies the HEARSAY-II lineage and explains variation across blackboard systems.

## R09

David Gelernter. **Generative communication in Linda.** *ACM Transactions on Programming Languages and Systems* 7(1), 80–112, 1985. DOI: [10.1145/2363.2433](https://doi.org/10.1145/2363.2433).

Comparison for coordination through independently existing tuples. VDMT does not require Linda's matching or communication semantics.

## R10

John R. Anderson, Daniel Bothell, Michael D. Byrne, Scott Douglass, Christian Lebiere, and Yulin Qin. **An integrated theory of the mind.** *Psychological Review* 111(4), 1036–1060, 2004. DOI: [10.1037/0033-295X.111.4.1036](https://doi.org/10.1037/0033-295X.111.4.1036). [Carnegie Mellon repository](https://doi.org/10.1184/R1/6613469) · [ACT-R project](https://act-r.psy.cmu.edu/).

Cognitive comparison involving modules, buffers, production selection, and subsymbolic mechanisms. Software architectural resemblance is not psychological validation.

## R11

Walid Taha and Tim Sheard. **Multi-stage programming with explicit annotations.** *PEPM*, 1997. DOI: [10.1145/258994.259019](https://doi.org/10.1145/258994.259019). Expanded account: **MetaML and multi-stage programming with explicit annotations**, *Theoretical Computer Science* 248(1–2), 211–242, 2000. DOI: [10.1016/S0304-3975(00)00053-0](https://www.sciencedirect.com/science/article/pii/S0304397500000530).

Comparison for explicit stages and typed code construction; string placeholders do not automatically inherit its guarantees.

## R12

PHP Documentation Group. **`str_replace` manual.** [Official documentation](https://www.php.net/manual/en/function.str-replace.php).

Technical reference for the array-based replacement primitive used by the inspected JCB placeholder implementation.

## R13

Charles L. Forgy. **Rete: A fast algorithm for the many pattern/many object pattern match problem.** *Artificial Intelligence* 19(1), 17–37, 1982. DOI: [10.1016/0004-3702(82)90020-0](https://www.sciencedirect.com/science/article/pii/0004370282900200).

Prior algorithm for efficient production-system matching. No Rete implementation is inferred from JCB's registry lookups.

## R14

Stanislas Dehaene, Michel Kerszberg, and Jean-Pierre Changeux. **A neuronal model of a global workspace in effortful cognitive tasks.** *PNAS* 95(24), 14529–14534, 1998. DOI: [10.1073/pnas.95.24.14529](https://doi.org/10.1073/pnas.95.24.14529). [Full primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC24407/).

Comparison for specialized processing and broader availability in cognitive modeling, not a claim of consciousness in a compiler.

## R16

LLVM Project. **LLVM Language Reference Manual.** [Official specification](https://llvm.org/docs/LangRef.html).

Comparison for explicitly specified intermediate representations. The VDMT framework does not require LLVM or SSA.

## R18

Donald Michie. **“Memo” Functions and Machine Learning.** *Nature* 218, 19–22, 1968. DOI: [10.1038/218019a0](https://www.nature.com/articles/218019a0).

Historical reference for retaining computational results. Recollection, caching, and learned cognition remain distinct concepts in this paper.

## L01

Creative Commons. **Attribution 4.0 International: legal code.** [Controlling license](https://creativecommons.org/licenses/by/4.0/legalcode) · [Human-readable deed](https://creativecommons.org/licenses/by/4.0/).

Controls reuse of the original explanatory work under the repository's stated scope. The deed summarizes but does not replace the legal code.

## L02

United States Copyright Office. **What Does Copyright Protect?** [Official guidance](https://www.copyright.gov/help/faq/faq-protect.html) · [Computer-program registration guidance](https://www.copyright.gov/register/tx-programs.html).

Used to explain the distinction between protected expression and ideas/methods. This is jurisdiction-specific official guidance, not a legal opinion determining rights in every country.

## L03

GitHub. **Publishing sources and custom domains for GitHub Pages.** [Publishing-source configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) · [Managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

Operational reference for the publication workflow. A repository `CNAME` file does not independently configure account settings or DNS.

## Citation practice

Cite the theory edition for its definitions and propositions, the pinned JCB file for implementation behavior, and the original scholarly work for inherited ideas. Do not use the theory's historical implementation date as the publication date of this manuscript. No DOI, institutional endorsement, or academic degree is asserted for this edition.
