# Kolmogorov Complexity

## Overview
---

In algorithmic information theory (a subfield of computer science and mathematics), the Kolmogorov complexity of an object, such as a piece of text, is the length of a shortest computer program (in a predetermined programming language) that produces the object as output. It is a measure of the computational resources needed to specify the object, and is also known as algorithmic complexity, Solomonoff–Kolmogorov–Chaitin complexity, program-size complexity, descriptive complexity, or algorithmic entropy. It is named after Andrey Kolmogorov, who first published on the subject in 1963.The notion of Kolmogorov complexity can be used to state and prove impossibility results akin to Cantor's diagonal argument, Gödel's incompleteness theorem, and Turing's halting problem.

In particular, no program P computing a lower bound for each text's Kolmogorov complexity can return a value essentially larger than P's own length (see section § Chaitin's incompleteness theorem); hence no single program can compute the exact Kolmogorov complexity for infinitely many texts.


### Kolmogorov Randomness

Kolmogorov randomness defines a string (usually of bits) as being random if and only if any computer program that can produce that string is at least as long as the string itself. To make this precise, a universal computer (or universal Turing machine) must be specified, so that "program" means a program for this universal machine. A random string in this sense is "incompressible" in that it is impossible to "compress" the string into a program that is shorter than the string itself. A counting argument is used to show that for any universal computer, there is at least one algorithmically random string of each length. Whether any particular string is random, however, depends on the specific universal computer that is chosen. This is because a universal computer can have a particular string hard-coded in itself, and a program running on this universal computer can then simply refer to this hard-coded string using a short sequence of bits (i.e. much shorter than the string itself).

This definition can be extended to define a notion of randomness for infinite sequences from a finite alphabet. These algorithmically random sequences can be defined in three equivalent ways. One way uses an effective analogue of measure theory; another uses effective martingales. The third way defines an infinite sequence to be random if the prefix-free Kolmogorov complexity of its initial segments grows quickly enough — there must be a constant c such that the complexity of an initial segment of length n is always at least n−c. This definition, unlike the definition of randomness for a finite string, is not affected by which universal machine is used to define prefix-free Kolmogorov complexity

### Relation to Entropy

For dynamical systems, entropy rate and algorithmic complexity of the trajectories are related by a theorem of Brudno, that the equality K ( x ; T ) = h ( T ) {\displaystyle K(x;T)=h(T)} {\displaystyle K(x;T)=h(T)} holds for almost all x {\displaystyle x} x.[16]

It can be shown[17] that for the output of Markov information sources, Kolmogorov complexity is related to the entropy of the information source. More precisely, the Kolmogorov complexity of the output of a Markov information source, normalized by the length of the output, converges almost surely (as the length of the output goes to infinity) to the entropy of the source. 

### Conditional versions

The conditional Kolmogorov complexity of two strings K ( x | y ) {\displaystyle K(x|y)} {\displaystyle K(x|y)} is, roughly speaking, defined as the Kolmogorov complexity of x given y as an auxiliary input to the procedure.[18][19]

There is also a length-conditional complexity K ( x | L ( x ) ) {\displaystyle K(x|L(x))} {\displaystyle K(x|L(x))}, which is the complexity of x given the length of x as known/input

Read more: https://en.wikipedia.org/wiki/Kolmogorov_complexity


