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

---

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

---

### Lesson 3: The Modeling Phase

- For the medicare data set the main question is "How do we detect anamolous charges?", followed by, how are anomalies defined After setting this, the question is what are the variables of interest.

- Next we check if the correlation of the data is linear or non-linear using a scatter plot.

- Scale variables: (f - min(f))/(max(f)-min(f))

- The [pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient) is given by covariance divided by the product of the standard deviation of x and y variables. 

- Scaling the feature keeps the correlation between variables the same, while making easier to visualize them and to make computations with them.

- The first model approach will be a non-parametric, via a [Kernel Density Estimation](https://en.wikipedia.org/wiki/Kernel_density_estimation) with derived variable x = abs(f0-f1)/f0. Non-parametric models are very useful to go from discrete data to probability distributions.

- Examples of kernels:
    - [Parzen windows](http://www.personal.reading.ac.uk/~sis01xh/teaching/CY2D2/Pattern2.pdf) 
    - [Gaussian Kernel](http://www.stat.wisc.edu/%7Emchung/teaching/MIA/reading/diffusion.gaussian.kernel.pdf.pdf)

- We can vary the bandwidth to play around the bias and the variance.

- To validate the estimation for the probability density there are two methods:
    - Minimize [MISE (Mean Integrated Squared Error)](https://en.wikipedia.org/wiki/Mean_integrated_squared_error) or AMISE (Assymptotic MISE).
    - Minimize KL Divergence.

- In the case of AMISE we get three terms as an approximation:
    - A term that is inherent of the variance of the data.
    - A squared bias term, that determines the smoothness of the estimate for differente bandwidths.
    - A variance term that determines jaggedness of the estimate.

- This means that choosing the bandwidth is choosing a trade-off between the bias and the variance of the prediction.

- Bandwidth selection:
    - For dimension 1 and kernel gaussian, Silverman's Rule of Thumb, h=((4 times sd^5)/(3n))^(1/5).
    - For d dimensions, use Scott's Rule, H = (1/n^(d+4)) times squared(covariance matrix).

- The [Kullback-Leibler Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) is a general method to compate probability distribution functions. IT can be thought as the information that is lost when a pdf g is used to approximate another pdf, f.

- Using Multivariate KDEs give us joint pdfs, that may be used to draw conditional probabilities. 

- The KDEs allow to get the shape of the data very easily and quickly.

- On finding outliers:
    - Use [Mahalanobis Distance](https://en.wikipedia.org/wiki/Mahalanobis_distance). Measures how far the values of data are from the central tendencies of the distributions.

- Food for thought:
    - Are outliers in bivariate data indicative of true outliers when the data has more dimensions?

Answer:

> Mahalanobis Distance is ideal for samples drawn from identical distribution. To find outliers in multidimensional data it is better to use richer methods, such as k-means. Ideally, we should inspect all variables that are uncorrelated to find outlier. 

---

### Lesson 4: The Validation Phase

- The trained models should be tested on unseen data.

- How to split the data:
    - _Training data_, used to train the model.
    - _Validation data_, used to select the model.
    - _Test data_, used to report the perfomance of the model.

- The ratio of the splits depends on the ammount of data it is available.

- It is also necessary to clean the data and to select the features.

- The chosen features are the ones with the highest disriminating power. (using techniques such as PCA and scaling the features).

- **Loss function**: measures how far an estimated value of a quantity from the true value.

- NOTE: Squared error loss is more sensible to outliers. The absolute error loss is not smooth when the difference is 0 which makes it troublesome to differentiate.

- **Risk**: It's the expected value of the loss.

- The expected value of the squared error loss will derive in three terms:
    - _Irreducible Error_, variance around the true mean inherent in the data.
    - _Squared Bias_
    - _Variance_

- Minimizing bias or variance requires a trade-off between them, since it may be impossible to reduce both at the same time.

- Low complexity -> Low Variance/High Bias, may lead to underfitting the data

- High complexity -> High Variance/Low Bias, may lead to overfitting the data

- The [Vapnik-Chervonenkis dimension](https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory) allows to measure the complexity of the model. This quantity allows to bound the error of the model on the test set with a given accuracy. For linear models the expression is simply, h = m+1, where m is the number of dimensions/features.

- The choice of the loss/risk depends on the problem formulation, which on its turn depends on the purpose of the model.

- _Learning curves_ plot the risk/cost/score of a model vs the size of the training set and test set. The interest in using this kind of curves is that we may find that using a certain amount of data points yields the same results as using more. If it is possible to use less data, the models may be simpler, which has its advantages.

- **Accuracy**: 
    - Fraction of the predictions that are correct.
    - Zero-one loss function
    - Missclassification: Risk
    - Ratio between the sum of (true positive + true negatives) by the number of examples.

- Depending of the application, the cost of a false positive might outweigh the cost of a false negative. An example is, for instance, a money transaction fraud detection. It's better to decline a transaction that is honest than letting an illegal one through.

- A [Confusion matrix](https://en.wikipedia.org/wiki/Confusion_matrix) is a very effective way of analyzing True/False Positive/Negative.

- Type I Error: False Positive (Predicted positive when it was negative).

- Type II Error: False Negative (Predicted negative when it was positive).

- **Sensitivity**: Ratio between true positive and the sum of (True positives plus false negatives). This means it is the ratio of actual positives that were correctly predicted.

- **Specificity**: Ratio between true negatives and the sum of (True negatives plus false positives). This means it is the ratio of actual negatives that were correctly predicted.

- We can approach this problem by hypothesis testing. Given an Hypothesis I (null hypothesis) and Hypothesis II (alternate hypothesis). If the type I error for a given "cut value" for a given hypothesis is less then a predifined value (_significance value_), we fail to reject that class/reject the null hypothesis. The **power of the test is given by 1-sensititivy**.

- A [ROC](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) (receiver operating characteristic curve) plots the value of _sensitivity_ and _specificity_ for different "cut values". 

- **Iso-perfomance lines**, are lines in ROC-space that lie in the same straight line. The perfomance of the models is given by the slope of the line. The models with more **AUC** (area under the curve), tend to perform better than the other models.

- Now using a **one vs all** aproach instead of binary classification.

- **Precision**: The ratio of true positive by the sum of (true positives plus false positives). Therefore it gives the ratio of positive predictions that were correct. It is a good metric to deal with classes where the samples are skewed, i.e., number of positive instances are small.

- **Recall**: The ratio of true positives by the sum of (true positive plus false negatives). It's the same as sensitivity.

- They are analyzed in a similar way of ROC curves, using _precision recall curves_.

- Another way of combining precision and recall is through [F-beta score](https://en.wikipedia.org/wiki/F1_score). For instance, the F1 score is the [harmonic mean](https://en.wikipedia.org/wiki/Harmonic_mean) between the precision and the recall.

- F2 weights recall higher than precision. F0.5 weights precision highter than recall.
