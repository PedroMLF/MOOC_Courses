# Deep Learning

This folder contains my solutions to the practical problems and some key notes regarding the course **Deep Learning** taught at EPFL by François Fleuret. The original page of the course may be found [here](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/).

---

### Lecture 1 - Introduction and Tensors [Part1](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-slides-1a-introduction.pdf) [Part2](https://documents.epfl.ch/users/f/fl/fleuret/www/dlc/dlc-slides-1b-tensors.pdf)

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
