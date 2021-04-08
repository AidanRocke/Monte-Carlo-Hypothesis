## The Challenge:

1. The challenge is to explore the hypothesis that prime-encodings are algorithmically random and that prime numbers have a maximum entropy distribution [1].

2. Conventional mathematical wisdom, at present, suggests that this hypothesis might be false i.e. there might be 'conspiracies' among arbitrarily large subsequences of prime encodings, i.e. predictable behaviour, which may be exploited by a machine learning algorithm [2].

3. In fact, this hypothesis implies a non-trivial interpretation of the prime number theorem. The Prime Number Theorem says how the prime numbers are distributed but not why. On the other hand, an information-theoretic analysis of the Prime Number Theorem indicates that they are distributed in this way because prime encodings are algorithmically random and the prime numbers have a maximum entropy distribution.

It is not possible to prove that a particular object is incompressible within algorithmic information theory so
the best we can do is perform rigorous experimental analysis using machine learning methods. Hence this challenge.

**Note:** For more information, please check the [Monte Carlo Hypothesis](https://github.com/AidanRocke/Monte-Carlo-Hypothesis/blob/main/monte-carlo-hypothesis.pdf).

## Getting started guides:

The maximum entropy distribution of the prime numbers and the algorithmic randomness of prime encodings are naturally divided into two separate challenges. In this repository, a getting started guide has been provided for each challenge as well as
methods for generating the relevant datasets.

## Submissions:

Important progress on this challenge ultimately requires a combination of insights from math, physics and computation.
If you think you have made significant progress, feel free to post your answer on the MathOverflow: https://mathoverflow.net/q/384109

Alternatively, you may contact the organiser directly: aidanrocke@gmail.com

## Prizes:

The best submission by a team or individual combining strong experimental and
theoretical work, presented before the 3rd of November 2021, will be awarded
a 150 cL Château Lafite-Rothschild Magnum from 2012 on the 24th of December 2021.

## Frequently Answered Questions:

**In what sense do the prime numbers have a maximum entropy distribution?**

This was carefully explained on the MathOverflow: https://mathoverflow.net/q/384109

**In what sense are prime encodings algorithmically random?**

I shall first assume that you have read both pages of [the complete challenge description](https://github.com/AidanRocke/Monte-Carlo-Hypothesis/blob/main/monte-carlo-hypothesis.pdf) and the theory behind this hypothesis: https://mathoverflow.net/q/384109
Given these assumptions, let's consider a thought experiment.

We shall first note that the locations of the primes are necessary and sufficient to define a prime encoding of any
length. Now, let's suppose you have a small fortune and enter a Casino which only offers one game. Given a prime encoding
of finite length, predict the location of the next prime number. Every time you are correct you win a dollar and every
time you are incorrect you lose a dollar.

If a profitable betting strategy exists, you may design an algorithm to implement this strategy. However, the statement
that prime encodings are algorithmically random implies that if you play the game long enough you won't make any profit
whatsoever. Moreover, given that the prime numbers have a maximum entropy distribution if you play this game long enough
you will eventually lose all your money.

**Have you benchmarked prime encodings against pseudo-random number generators?**

Yes, I have empirically verified that against state-of-the-art machine learning algorithms
pseudorandom number generators fail the weighted next bit test, unlike prime encodings.

**Might this hypothesis have any connection with the Riemann Hypothesis?**

That is correct. If we find very strong experimental evidence for the hypothesis
that prime encodings are asymptotically incompressible then it is impossible for
us to prove the Riemann Hypothesis if it is true.

This would provide an important instance of Gödel's incompleteness theorem that in a
mathematical system that is sufficiently sophisticated to contain arithmetic there
are statements that are true that can't be proved.

## References:

1. Aidan Rocke (https://mathoverflow.net/users/56328/aidan-rocke), information-theoretic derivation of the prime number theorem, URL (version: 2021-02-20): https://mathoverflow.net/q/384109

2. Terence Tao. Structure and randomness in the prime numbers: A small selection of results in number theory. Slides. 2007.

3. Marcus Hutter. Algorithmic information theory. Scholarpedia. 2007.

4. Schnorr, C. P. (1971). "A unified approach to the definition of a random sequence". Mathematical Systems Theory.

5. Peter D. Grünwald. The Minimum Description Length Principle . MIT Press. 2007.

6. David Deutsch. Quantum theory, the Church–Turing principle and the universal quantum computer. 1985.

7. Don Zagier. Newman’s short proof of the Prime Number Theorem. The American Mathematical Monthly, Vol. 104, No. 8 (Oct., 1997), pp. 705-708

8. John A. Wheeler, 1990, "Information, physics, quantum: The search for links" in W. Zurek (ed.) Complexity, Entropy, and the Physics of Information. Redwood City, CA: Addison-Wesley.

9. Guillermo Valle Pérez, Chico Camargo, Ard Louis. Deep Learning generalizes because the parameter-function map is biased towards simple functions. 2019.

10. Aidan Rocke (https://cstheory.stackexchange.com/users/47594/aidan-rocke), Understanding the Physical Church-Turing thesis and its implications, URL (version: 2021-02-22): https://cstheory.stackexchange.com/q/48450

11. Igor V. Volovich. Number Theory as the Ultimate Physical Theory. Pleiades Publishing. 2010.
