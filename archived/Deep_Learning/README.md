# Deep Learning

This folder contains my solutions to the practical problems and some key notes regarding the course **Deep Learning** taught at EPFL by François Fleuret. The original page of the course may be found [here](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/).

---

### Lecture 1 - Introduction and Tensors [Slides(1)](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-slides-1a-introduction.pdf) [Slides(2)](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-slides-1b-tensors.pdf)

- Techniques used in practice consist of:
    - Defining a parametric model.
    - Optimizing its parameters by finding the ones that work best on a training set.

- Artificial Neural Networks consist of deep stacks of parametrized processing.

- Deep Learning is builts on a generalization of a neural network: **graph of tensor operators**.

- A tensor is a generalized matrix:
    - 1d tensor -> Vector
    - 2d tensor -> Matrix (ex. grayscale image)
    - 3d tensor -> Vector of identically sized matrices (ex. rgb image)
    - 4d tensor -> Matrix of identically sized matrices (ex. series of rgb images)
    - etc.

- The default tensor type **torch.Tensor** is an alias for **torch.FloatTensor** (32-bit floating point).

- In-place operations are suffixed with an underscore.

- _narrows_ function intuition: first entry is the dimension, the second is the starting index and the third is how many of the following will be used.

- _transpose_ intuition: simply think that a dimension is being exchanged by the other. For instance, transpose 0 with 2 means that the first "depth" coordinate now will be the first column and the first column will be composed of the elements of the first "depth".

- **Broadcasting** automatically expands dimensions of size 1, by replicating its coefficientes to the necessary dimensions to make the computations legal. For instance, summing a 4x1 tensor with a 1x5 tensor will yield a 4x5 tensor.

- A tensor is a view of a **storage**, which a low-level 1d vector. The first coefficient of a tensor is at _storage offset_ in _storage_. To increment its index by k, it is necessary to move strike(k) elements in storage. For instance, to transform a storage with 20 blocks from 0 to 19 into a 3x2 [5,6; 9,10; 13,14] the storage offset is 5, the size is (3,2) and the stride is (4,1). Since the tranposed tensor shares the storage with the original tensor, we cannot "flatten" it into a 1d contiguous vector without a memory copy.

---

### Lecture 2 - Machine Learning Fundamentals [Slides](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-handout-2-ml-basics.pdf)

**Learning from data**

- Three categories of inference:
    - Classification
    - Regression
    - Density estimation

- In _classification_ we want to estimate the argument of y (the class) that maximizes the probability of P(Y=y|X=x). In _regression_ we want to estimate the expected value of Y given X=x. And in _density estimation_ we want to estime the probability distribution of x.

- **Generative** classification methods have an explicit data model, whereas **discriminative** don't.

**Risk**

- Learning consists of finding a good function or set of parameters through a loss. For _classification_ it's usually a binary loss, for _regression_ something like the squared error and for _density estimation_, minus the logarithm of a estimated distribuion.

- We are looking for a f with a small expected risk, being R(f) the expected value of the loss of a given _f_ on a given training example, _z_. Assuming the training samples are i.i.d we can obtain an estimate, the _empirical risk_. It is an unbiased estimator of the expected risk.

**Over and under-fitting**

- When the error of the model decreases on the training set but increses in a independent test set, then the model is _overfitting_.

- Using regularization may help attenuate this problem.

- The _capacity_ of a set of predictors is the ability to model an arbitrary functional.

- Over-fitting might be reduced by impoverishing the space of possible functions (less functionals, early stopping) or by making the choice of parameters less dependent on data (penalty on coefficients, margin maximization, ensemble methods).

**Bias-variance dilemma**

- The expect value of the squared error may be decomposed into a bias and a variance term. The _bias term_ quantifies how much the model fits to the data on average. The _variance term_ quantifies how much the model changes across datasets.

- Reducing the capacity of the model increases the bias term. Increase the capacity of the models makes it vary a lot with the training data, and therefore increases variance.

**Is all this probabilistic?**

- Model fitting and regularization may be interpreted as Bayesian inference. This consists of modeling the parameters of a model as random quantities with a certain prior. With the values of the training data it is possible to estimate a posterior distribution of the parameters and from that, their most likely values.

- The value of the distribution of a certain parameter for a given data set may be decomposed into a portion of gaussian noise on Ys and a portion of gaussian noise on As. This leads to the intuition of regularization that, the stronger the prior, the more evidence needed to deviate from it.

**Proper evaluation protocols**

- Deep learning perfomance relies on parameter optimization, so one should be careful about parameter over-fitting through experiments. This means, don't use the test set scores to correct parameters.

- The ideal development cycle is:
    - Write code
    - Train (iterate this)
    - Test
    - (Paper) 

- Another way to deal with this is to:
    - Use a development set.
    - If the data is scarce, use cross-validation.

**Standard clustering and embedding**

- _K-means_, finds k centroids that span uniformly the training population.

- _PCA_, looks for an "affine subspace" that spans the data.

---






















