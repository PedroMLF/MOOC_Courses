# Sequence Models fot Time Series and Natural Language Processing

---

## Week 1

### Working with Sequences

1. Sequences are data points that can be meaningfully ordered, such that earlier observations provide information about later observations. You should also be able to take a slice of observations and use those to get a better than chance prediction of some later observations.

2. Types of Sequence Models:
- One-to-sequence
- Sequence-to-one
- Sequence-to-sequence

3. If we want to transform a sequence of values in features, by concatenating the values (something like [t0, ..., t10; t1, ..., t11; ...; tseqlen-10, ..., tseqlen]), we will use a sliding window with a certain _n_. In the end, we will have _t-n_ rows with _n_ entries, where in this case, t = seqlen and n = 10.

4. In order to choose a good _lag_ value it is possible to use autocorrelation graphs.

![](images/01.png)

5. Sometimes time dependencies are known, and thus, it is possible to choose a suitable time lag based on that.
