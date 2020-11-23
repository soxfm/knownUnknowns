# The PingeonHole Principle
> Given a set (A) of pigeons and 
> a set (B) of pigeonholes
> if all the pigeons fly into a pigeonhole
> and pigeons > pigeonholes
> then one of the pigeonholes has to contain more than one pigeon

> The pigeonhole principle states that if (n) items are put into (m) containers,
> with 'n > m' ; then at least one container must contain more than one item.

### Chinese Remainder theorem
establishes that if the remainders of the division of an integer (n)/several integer are known values; we can determine uniquely the remainder of the division of n by the product of these integers. 
"There are certain things whose numbers is unknown. If we count them by thress, we have two left over; by fives, three left over; and by sevens, two left over. How many things are there?" (Sunzi)

Proof of Example C
First consider the sequence
(1)   b, b + m, b + 2m, ..., b + (n - 1)m
The sequence forms a complete residue class, modulo n. To see this, consider the sequence:
(2)   0, m, 2m, 3m, ..., (n - 1)m
Since the greatest common divisor of (m,n) = 1, we have xm ≡ ym (mod n) <=> x ≡ y (mod n). Hence, each element in the sequence (2) is unique. Adding b to the sequence (1) only cyclically permutes the residue class.
By the pigeonhole principle, for any 0 ≤ a < n, we must have b + km ≡ a (mod n) for any k ∈ {0,...,n − 1}.


### Constructive Proofs vs Non Constructive

Finally, a note about the type of proofs pigeonhole proofs belong to. Although useful, a defining characteristic of pigeonhole proofs are that they are non-constructive, i.e. that although they prove the existence of something, they fail to provide an explicit example that proves the theorem. To illustrate the difference, consider two proofs of the same statement, namely that:

`there exists irrational numbers x, y for which x^y is rational`

Non-Constructive Proof
Let x = √2^(√2) and y = √2. We know y is irrational, but we do not know whether x is rational or irrational. If x is irrational, then we have an irrational number to an irrational power that is rational:
xʸ = (√2^(√2))^(√2) = (√2)^(√2 × √2) = (√2)² = 2
If x is rational, then 
yʸ = √2^(√2) = x is rational.
Either way, we have an irrational number to an irrational power that is rational.

Constructive Proof
Let x = √2 and y = log(9). Then 
xʸ = √2^(log(9)) = √2^(log(3²)) = √2^(2log(3)) = (√2^2)^(log(3))^= 2^(log3) = 3
As 3 is rational, we have shown that xʸ = 3 is rational.
We know that x = √2 is irrational. We do not know whether y = log(9) is irrational. Suppose log(9) is rational, so that there are two integers a, b for which  a/b = log(9). Then 2^(a/b) = 9, so 2^(a/b)ᵇ = 9ᵇ, which reduces to 2ᵃ = 9ᵇ. However, we know that 2ᵃ is even and 9ᵇ must be odd, so they cannot equal one another. We have obtained a contradiction and must assume that log(9) is irrational.

