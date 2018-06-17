# Algorithms: Design and Analysis
by Tim Roughgarden (Stanford University)

## Notes:

### Introduction

* Divide and Conquer - Divide problem into subproblems, that are solved recursively and then the results are joined.

* **Merge Sort**:
    - Split the array into two smaller arrays.
    - Sort those smaller arrays.
    - Merge the results.

* _Base cases_ are cases that don't need to go through de algorithm.

* To do the merge:
    - Tranverse both smaller arrays in parallel.
    - Take always the smallest element.

* _Merge Subroutine running time_ - less or equal to _4n+2_ (loop _n_ times, in each do 4 operations plus two initializations). We can approximate this by saying less or equal to _6n_.

* _Merge Sort running time_ - less or equal to _6n log2 n + 6n_.

* Proof of this claim might be done using a _recursion tree_:
    - The maximum level of this tree will be log2 of n (size of the input array) plus 1. 
    - The last level will have single element arrays (base cases).
    - At each level j, there are _2^j_ problems, each of size _n/(2^j)_.

* At a given level j, the number of operations will be less or equal to _2^j * 6 * n/(2^j)_ which results in _6n_. So the total number of operations will be the work per level times the number of level, ie, less or equal to _6n (log2 n + 1)_.

* Guiding principles of the course:
    - Worst case analysis vs average case analysis and benchmarks (the later requires domain knowledge).
    - Not worrying about small changes or constant factors.
    - Assymptotic analysis, ie., focusing on large inputs.
    - Fast algorithm - worst-case running time grows slowly with input size.


