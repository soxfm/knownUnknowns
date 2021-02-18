
en.wikipedia.org
Principle of explosion
Contributors to Wikimedia projects
6-8 minutes

"Ex falso quodlibet" redirects here. For the musical form, see Quodlibet. For the related tag editor and library organizer, see Ex Falso.

In classical logic, intuitionistic logic and similar logical systems, the principle of explosion (Latin: ex falso [sequitur] quodlibet, 'from falsehood, anything [follows]'; or ex contradictione [sequitur] quodlibet, 'from contradiction, anything [follows]'), or the principle of Pseudo-Scotus, is the law according to which any statement can be proven from a contradiction.[1] That is, once a contradiction has been asserted, any proposition (including their negations) can be inferred from it; this is known as deductive explosion.[2][3]

The proof of this principle was first given by 12th-century French philosopher William of Soissons.[4] Due to the principle of explosion, the existence of a contradiction (inconsistency) in a formal axiomatic system is disastrous; since any statement can be proven, it trivializes the concepts of truth and falsity.[5] Around the turn of the 20th century, the discovery of contradictions such as Russell's paradox at the foundations of mathematics thus threatened the entire structure of mathematics. Mathematicians such as Gottlob Frege, Ernst Zermelo, Abraham Fraenkel, and Thoralf Skolem put much effort into revising set theory to eliminate these contradictions, resulting in the modern Zermelo–Fraenkel set theory.

As a demonstration of the principle, consider two contradictory statements—"All lemons are yellow" and "Not all lemons are yellow"—and suppose that both are true. If that is the case, anything can be proven, e.g., the assertion that "unicorns exist," by using the following argument:

    We know that "Not all lemons are yellow," as it has been assumed to be true.
    We know that "All lemons are yellow," as it has been assumed to be true.
    Therefore, the two-part statement "All lemons are yellow OR unicorns exist” must also be true, since the first part is true.
    However, since we know that "Not all lemons are yellow" (as this has been assumed), the first part is false, and hence the second part must be true, i.e., unicorns exist.

In a different solution to these problems, a few mathematicians have devised alternate theories of logic called paraconsistent logics, which eliminate the principle of explosion.[5] These allow some contradictory statements to be proven without affecting other proofs.
Symbolic representation[edit]

In symbolic logic, the principle of explosion can be expressed schematically in the following way:

    {\displaystyle P,\lnot P\vdash Q} For any statements P and Q, if P and not-P are both true, then it logically follows that Q is true.

Proof[edit]

Below is a formal proof of the principle using symbolic logic
Step  Proposition   Derivation
1   P   Assumption
2   \neg P  Assumption
3   P\lor Q   Disjunction introduction (1)
4   Q   Disjunctive syllogism (2,3)

This is just the symbolic version of the informal argument given in the introduction, with P standing for "all lemons are yellow" and Q standing for "Unicorns exist." We start out by assuming that (1) all lemons are yellow and that (2) not all lemons are yellow. From the proposition that all lemons are yellow, we infer that (3) either all lemons are yellow or unicorns exist. But then from this and the fact that not all lemons are yellow, we infer that (4) unicorns exist by disjunctive syllogism.
Semantic argument[edit]

An alternate argument for the principle stems from model theory. A sentence P is a semantic consequence of a set of sentences \Gamma only if every model of \Gamma is a model of P. However, there is no model of the contradictory set {\displaystyle (P\wedge \lnot P)}. A fortiori, there is no model of {\displaystyle (P\wedge \lnot P)} that is not a model of Q. Thus, vacuously, every model of {\displaystyle (P\wedge \lnot P)} is a model of Q. Thus Q is a semantic consequence of {\displaystyle (P\wedge \lnot P)}.
Paraconsistent logic[edit]

Paraconsistent logics have been developed that allow for sub-contrary forming operators. Model-theoretic paraconsistent logicians often deny the assumption that there can be no model of \{\phi , \lnot \phi \} and devise semantical systems in which there are such models. Alternatively, they reject the idea that propositions can be classified as true or false. Proof-theoretic paraconsistent logics usually deny the validity of one of the steps necessary for deriving an explosion, typically including disjunctive syllogism, disjunction introduction, and reductio ad absurdum.
Usage[edit]

The metamathematical value of the principle of explosion is that for any logical system where this principle holds, any derived theory which proves ⊥ (or an equivalent form, \phi \land \lnot \phi) is worthless because all its statements would become theorems, making it impossible to distinguish truth from falsehood. That is to say, the principle of explosion is an argument for the law of non-contradiction in classical logic, because without it all truth statements become meaningless.

Reduction in proof strength of logics without ex falso are discussed in minimal logic.
See also[edit]

    Consequentia mirabilis – Clavius' Law
    Dialetheism – belief in the existence of true contradictions
    Law of excluded middle – every proposition is true or false
    Law of noncontradiction – no proposition can be both true and not true
    Paraconsistent logic – a family of logics used to address contradictions
    Paradox of entailment – a seeming paradox derived from the principle of explosion
    Reductio ad absurdum – concluding that a proposition is false because it produces a contradiction
    Trivialism – the belief that all statements of the form "P and not-P" are true

References[edit]

    ^ Carnielli, Walter, and João Marcos. [2000] 2001. "Ex contradictione non sequitur quodlibet (PDF)." Bulletin of Advanced Reasoning and Knowledge 1:89–109. CiteSeerx: 10.1.1.107.70.
    ^ Başkent, Can (2013-01-31). "Some topological properties of paraconsistent models". Synthese. 190 (18): 4023. doi:10.1007/s11229-013-0246-8.
    ^ Carnielli, Walter; Coniglio, Marcelo Esteban (2016). Paraconsistent Logic: Consistency, Contradiction and Negation. Logic, Epistemology, and the Unity of Science. 40. Springer International Publishing. ix. doi:10.1007/978-3-319-33205-5. ISBN 978-3-319-33203-1.
    ^ Priest, Graham. 2011. "What's so bad about contradictions?" In The Law of Non-Contradicton, edited by Priest, Beal, and Armour-Garb. Oxford: Clarendon Press. p. 25.
    ^ Jump up to: a b McKubre-Jordens, Maarten (August 2011). "This is not a carrot: Paraconsistent mathematics". Plus Magazine. Millennium Mathematics Project. Retrieved January 14, 2017.

