>God may not play dice with the universe, but something strange is going on with the prime numbers.-Paul Erdős


## The Challenge:

1. The challenge is to explore the hypothesis that prime-encodings are algorithmically random and that prime numbers have a maximum entropy distribution [1].

2. Conventional mathematical wisdom, at present, suggests that this hypothesis might be false. There might be 'conspiracies' among arbitrarily large subsequences of prime encodings, i.e. predictable behaviour, which may be exploited by a machine learning algorithm [2].

3. In fact, this hypothesis implies a non-trivial interpretation of the prime number theorem. The Prime Number Theorem says how the prime numbers are distributed but not why. On the other hand, an information-theoretic analysis of the Prime Number Theorem indicates that they are distributed in this way because prime encodings are algorithmically random and the prime numbers have a maximum entropy distribution.

It is not possible to prove that a particular object is incompressible within algorithmic information theory so
the best we can do is perform rigorous experimental analysis using machine learning methods. Hence this challenge.

**Note:** For more information, please check the [Monte Carlo Hypothesis](https://github.com/AidanRocke/Monte-Carlo-Hypothesis/blob/main/monte-carlo-hypothesis.pdf) as well as the latest survey, [The current status of the Monte Carlo Hypothesis](https://keplerlounge.com/statistical/physics/2021/08/27/current-monte-carlo.html). 

## Getting started guides:

The maximum entropy distribution of the prime numbers and the algorithmic randomness of prime encodings are naturally divided into two separate challenges. In this repository, a getting started guide has been provided for each challenge as well as
methods for generating the relevant datasets.

## Submissions:

Important progress on this challenge ultimately requires a combination of insights from math, physics and computation.
If you think you have made significant progress, feel free to open a pull request.

## Prizes:

The best submission by a team or individual combining strong experimental and
theoretical work, presented before the 3rd of November 2021, will be awarded
a 150 cL Château Lafite-Rothschild Magnum from 2012 on the 24th of December 2021.

## Frequently Answered Questions:

**What is the precise definition of asymptotic incompressibility?**

For more information on asymptotic incompressibility and its relation to algorithmic randomness, you may want to
read a [concise explanation](https://github.com/AidanRocke/Monte-Carlo-Hypothesis/blob/main/theory/asymptotic_incompressibility.pdf) of how a scientist may identify data-generating processes that are asymptotically incompressible using methods from machine learning.

**Have you benchmarked prime encodings against pseudo-random number generators?**

Yes. Against state-of-the-art machine learning algorithms pseudorandom number generators fail the weighted next bit test, unlike prime encodings.

**Might this hypothesis have any connection with the Riemann Hypothesis?**

That is correct. If we find very strong experimental evidence for the hypothesis
that prime encodings are asymptotically incompressible then it is impossible for
us to prove the Riemann Hypothesis if it is true.

This would provide an important instance of Gödel's incompleteness theorem that in a
mathematical system that is sufficiently sophisticated to contain arithmetic there
are statements that are true that can't be proved.

## An introduction to number theory:
1. [Fermat's little theorem](https://keplerlounge.com/number-theory/2021/04/17/fermat-little.html)
2. [Euler's totient function and Euler's theorem](https://keplerlounge.com/number-theory/2021/04/19/euler-theorem.html)
3. [The multiplicative group of integers modulo n](https://keplerlounge.com/number-theory/2021/04/21/modulo-group.html)
4. [Lagrange's theorem and its applications](https://keplerlounge.com/number-theory/2021/04/22/lagrange-theorem.html)
5. [Almost all integers are incompressible](https://keplerlounge.com/information-theory/2021/04/26/incompressible-integers.html)
6. [All the information in the integers is stored in the prime numbers](https://keplerlounge.com/information-theory/2021/07/13/integer-information.html)
7. [Using the incompressibility method for counting prime numbers](https://keplerlounge.com/information-theory/2021/04/27/AIT-counting-primes.html)
8. [An introduction to normal numbers](https://keplerlounge.com/information-theory/2021/05/10/normal-numbers.html)
9. [Compression bounds on the Copeland-Erdős constant](https://keplerlounge.com/information-theory/2021/05/11/copeland-erdos.html)

## An introduction to probabilistic number theory:

1. [A complexity bound on Gödel numbers](https://keplerlounge.com/formal/systems/2021/05/11/godel-numbers.html)
2. [An elegant proof of Mertens' theorem](https://keplerlounge.com/number/theory/2021/05/23/mertens-theorem.html)
3. [Abel summation and Mertens' second theorem](https://keplerlounge.com/number-theory/2021/05/30/mertens-second.html)
4. [The Hardy-Ramanujan theorem](https://keplerlounge.com/number-theory/2021/05/31/hardy-ramanujan.html)
5. [The Erdős-Kac theorem](https://keplerlounge.com/number-theory/2021/06/01/erdos-kac.html)
6. [A curious relation concerning the distribution of primes](https://keplerlounge.com/number-theory/2021/06/09/PNT-relation.html)
7. [A probabilistic proof of Cramér's conjecture](https://keplerlounge.com/number-theory/2021/06/04/cram%C3%A9r-conjecture.html)
8. [The computational complexity of prime sieving](https://keplerlounge.com/number-theory/2021/06/27/eratosthenes.html)

## References:

1. Aidan Rocke (https://mathoverflow.net/users/56328/aidan-rocke), information-theoretic derivation of the prime number theorem, URL (version: 2021-02-20): https://mathoverflow.net/q/384109

2. Terence Tao. Structure and randomness in the prime numbers: A small selection of results in number theory. Slides. 2007.

3. A. N. Kolmogorov Three approaches to the quantitative definition of information. Problems of Information and Transmission, 1(1):1--7, 1965

4. G. J. Chaitin On the length of programs for computing finite binary sequences: Statistical considerations. Journal of the ACM, 16(1):145--159, 1969.

5. R. J. Solomonoff A formal theory of inductive inference: Parts 1 and 2. Information and Control, 7:1--22 and 224--254, 1964.

6. Schnorr, C. P. (1971). "A unified approach to the definition of a random sequence". Mathematical Systems Theory.

7. Peter D. Grünwald. The Minimum Description Length Principle . MIT Press. 2007.

8. David Deutsch. Quantum theory, the Church–Turing principle and the universal quantum computer. 1985.

9. Don Zagier. Newman’s short proof of the Prime Number Theorem. The American Mathematical Monthly, Vol. 104, No. 8 (Oct., 1997), pp. 705-708

10. John A. Wheeler, 1990, "Information, physics, quantum: The search for links" in W. Zurek (ed.) Complexity, Entropy, and the Physics of Information. Redwood City, CA: Addison-Wesley.

11. Guillermo Valle Pérez, Chico Camargo, Ard Louis. Deep Learning generalizes because the parameter-function map is biased towards simple functions. 2019.

12. Aidan Rocke (https://cstheory.stackexchange.com/users/47594/aidan-rocke), Understanding the Physical Church-Turing thesis and its implications, URL (version: 2021-02-22): https://cstheory.stackexchange.com/q/48450

13. Igor V. Volovich. Number Theory as the Ultimate Physical Theory. Pleiades Publishing. 2010.

14. Yang-Hui He. Deep-Learning the Landscape. 2018.
