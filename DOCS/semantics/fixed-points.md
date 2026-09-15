---
title: Fixed points and closure laws
description: Conditional proofs of stabilization, least closure, monotonicity, and idempotence for a finite positive derivation model.
section: Semantics
order: 23
evidence: Formal deductions
---
# Fixed points and closure laws

## Assumptions

Fix a finite fact universe $U$, a seed $K_0\subseteq U$, and a deterministic operator $G:\mathcal{P}(U)\to\mathcal{P}(U)$ that is monotone. Require all reachable facts to be mutually compatible under the chosen key/value relation. Define

$$
F(K)=K\cup G(K),\qquad K_{n+1}=F(K_n).
$$

These assumptions describe a bounded positive fragment of VDMT. They do not describe arbitrary string rewriting, unrestricted plugins, or source mutations between epochs.

## Proposition 1 — finite stabilization

There is an $n\leq |U\setminus K_0|$ such that $K_{n+1}=K_n$.

**Proof.** $K_n\subseteq K_{n+1}$ by construction. Every strict transition adds at least one previously absent member of the finite set $U\setminus K_0$. There can be at most $|U\setminus K_0|$ strict transitions. Once equality occurs, determinism gives the same result on every subsequent application. The algorithm may perform one additional evaluation to detect equality. $\square$

This is a bound on strict growth rounds, not on the cost of each round.

## Proposition 2 — least closed superset

The stabilized result $K^*$ is the least set containing $K_0$ such that $G(K^*)\subseteq K^*$.

**Proof.** Stabilization gives $K^*=K^*\cup G(K^*)$, hence closure. Let $Y$ contain $K_0$ and satisfy $G(Y)\subseteq Y$. By induction, $K_n\subseteq Y$: the base is immediate; the step follows from monotonicity, since $G(K_n)\subseteq G(Y)\subseteq Y$. Therefore $K^*\subseteq Y$. $\square$

This explains what “complete the context” means within the rule system: no consequence licensed by those rules is missing. It does not mean that every relevant real-world fact has been discovered.

## Proposition 3 — closure operator laws

Let $\operatorname{cl}(K)$ be the stabilized result from seed $K$. Then

$$
K\subseteq\operatorname{cl}(K),
$$
$$
K\subseteq L\Longrightarrow\operatorname{cl}(K)\subseteq\operatorname{cl}(L),
$$
$$
\operatorname{cl}(\operatorname{cl}(K))=\operatorname{cl}(K).
$$

**Proof.** Extensivity follows from accumulating union. Monotonicity follows by induction on paired iterations, using monotonicity of $G$. Idempotence follows because the first result is already closed, so iteration from it adds nothing. $\square$

This is the precise mathematical counterpart of recollecting a completed context without repeatedly discovering the same consequences.

## Relationship to established results

The construction uses the established fixed-point tradition associated with Knaster, Tarski, Kleene, and later work on program analysis. Tarski's general theorem concerns monotone maps on complete lattices; the elementary finite proof above avoids claiming that a general infinite-domain fixed point is computable in finitely many steps. [R01](../reference/bibliography.md#r01)

## Counterexamples that delimit the result

With $G(K)=\{n+1:n\in K\}$ over the natural numbers and seed $\{0\}$, knowledge grows indefinitely. Finite termination has been lost.

With an instruction “toggle the value of flag,” the state can alternate forever. Inflationary accumulation has been lost.

With a rule “derive `fallback` only when `label` is absent,” later knowledge can invalidate an earlier interpretation. Monotonicity has been lost unless the absence test is evaluated against a closed earlier stratum.

These examples do not refute VDMT. They explain why a serious implementation must identify the fragment in which it claims the closure laws and handle other behavior with a different contract.
