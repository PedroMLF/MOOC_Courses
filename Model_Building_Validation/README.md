# Model Building and Validation
by Rishi Pravahan and Don Dini (Udacity/AT&T)

## Notes:

### Lesson 1: Intro to the QMV Process

- Three phases of analysis: Questioning, Modeling and Validating.

- Classification (eg. before, after a certain time) vs Regression (eg. time value).

- The data has _locality_ if a given unknown point has the same label that the points that surround it.

- Statistical Inference: eg. Point estimation, confidence sets, classification, hypothesis testing, parameter estimation.

- Keeping a log of the decisions taken is a good way to evaluate what work and what didn't work and to plan what to try next.

- Questioning:
    - What are the metrics that will be used?
    - What statistical inference problem will be examined?
    - Which features are important and are going to be selected?

- Modeling:
    - Choose a model that takes advantage of the structure of the data.

- Validation:
    - How well does the model generalize to unseen data?

### Lesson 2: The Questioning Phase

- The problem that is being studied is how long until someone tweets something.

- The first approach was too define a regression that, from the time between tweets, tries to predict when will the next one occur. In this case it is a good idea to plot an histogram. With the histogram it is verified that the data follows an exponential distribution.

- [Markov's Inequalty](https://en.wikipedia.org/wiki/Markov%27s_inequality):

> Being X a nonnegative random variable and t > 0, then the probability of X being greater than t is the expectation of X divided by t, Pr{X > t} <= E(X)/t.

> By making X equal to |X-u| we get the [_Chebyshev's inequalty_](https://en.wikipedia.org/wiki/Chebyshev%27s_inequality).

- Using Chebyshev's inequalty it is possible to get an estimate of how many points are needed in order to have the probability of the deviation between the true value of the parameter beta below a certain threshold.

- A better estimate may be obtained using [Hoeffding's Inequalty](https://en.wikipedia.org/wiki/Hoeffding%27s_inequality).

- It is possible to add two more factors to the exponential expression. An alpha that multiplies the expression and a constant c.

- The second approach is to use data with (delta_t, p), where delta_t is the time elapsed and p is the time until the next tweet.


