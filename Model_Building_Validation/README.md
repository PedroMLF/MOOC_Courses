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

- _Inherent Variance_ happens when, for the same input point, the measured value is differente due to some process noise.

- Uncaptured features may increase a lot the variance/uncertainty on the data.

- _Entropy_ allows to measure the degree of skew in a probability distribution. It is calculated as minus the sum of each probability times its log. Entropy has a minimum value of zero (absolute certainty about the value a given probability distribution will take) and has maximum value of one (every value of a given probability distribution is equally probable).

- Given X and Y, if entropy H(X) is greater than H(X | Y=y1), then this means that knowing that value of y has an impact. Consequently, the expected value of reduction of the entropy of X due to knowing Y is H(X) - H(X | Y), where H(X|Y) is the sum of entropy conditioned on y for every point of Y. This means that, the variable that has the biggest impact on the entropy of X is the one that reduces the entropy of X the most. The best feature to describe X is the one that keeps its entropy the largest.

- This _information gain_ means that we want to use as modelling variables the ones that keep the entropy of the to-be predicted variable as high as possible (since not using them would cause us to miss a lot of information).

- When using _covariance_ keep in mind that it is only concerned about linear variations. Calculating Cov(x,y) for y = x^2 yields a value of zero and clearly shows this. It's common that real-life problems have variables that don't correlate linearly between each other.


