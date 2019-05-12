# Sequence Models fot Time Series and Natural Language Processing

---

## Week 1 - Working with Sequences

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

### Modelling Sequences with Linear Models

### Modelling Sequences with DNNs

1. Sometimes it is important that models agree with how we think the underlying relationship between the features and the labels works.

2. We might want more recent observations to be more important. This can be obtained with exponential smoothing.

### Modelling Sequences with CNNs

1. Locality is important for both images and sequences.

2. A deeper model is more specific (the same as with deep CNNs, whose deeper layers capture more specific patterns).

3. Steps in applying a convolution:
- Flatten the input sequence.
- Use `conv1d` to apply a number of filters to the sequence.
- Use `max_pooling1d` to add some spatial invariance and downscaling.
- Flatten the resulting output into a sequence.
- Send it through a fully connected layer with the appropriate output node.

### The variable-length problem

1. In the sequence domain it is important that models are robust to changes in the length of the pattern.

2. Two techniques to handle variable length inputs and outputs:
- Cutting and padding.
- Bagging.

3. By padding we end up multiplying by zero certain inputs.

4. By cutting to the shortest sequence-length we end up losing information.

5. Bagging does not hold information about the sequence (as it does something like the average of all).

---

## Week 1 - Recurrent Neural Networks

### Recurrent Neural Networks

1. Formulate the problem as "Representing a single event given what has come before".

2. Two key ideas:
- RNNs learn a compact hidden state that represents the past.
- The input to a RNN is a concatenation of the original, stateless input and the hidden state.

![](images/02.png)

3. Optimized with backpropagation through time (each parameter is updated using the average of the partial derivatives from out iterations).

![](images/03.png)

4. With RNNs the output isn't just a class label, it's a sequence.

5. These models might learn representations and memorize patterns, but are unable to learn relationships between concepts.

6. RNNs are subject to the problem of vanishing gradient.

![](images/04.png)

---

## Week 1 - Dealing with Longer Sequences

### LSTMs, GRUs, and RNNs in TensorFlow

1. Problem with long term dependencies.

![](images/05.png)

2. LSTM cells

![](images/06.png)

![](images/07.png)

3. GRUs have similar performance, and computationally more efficient.

![](images/08.png)

5. A simple RNN has 1 matrix of weights, a LSTM has 4, and GRUs have 3. The number of matrixes does not depend on the number of time steps.

6. Implementing one in TensorFlow:

![](images/09.png)

### Deep RNNs

1. Deep RNNs in TensorFlow.

![](images/10.png)

2. Usually we only take into account the values from the last layer.

### Improving our Loss Function

1. If for instance we use only the last prediction to classify a whole sequence, measure the loss not only on the final prediction in the sequence, but for the last _k_ time steps. Then it is possible to use the average of those losses for a more robust value.


### Training with real data

1. If we have a long sequence, we can split it into smaller sequences, which are easier to train.

2. When splitting up sequences, there are two things to consider: the length of the sequences, and how much they overlap.

3. If we don't overlap continuous sequences we can propagate the info between splits, by initializing the hidden states of the next split with the last hidden state of the previous split.

![](images/11.png)

4. It also might be necessary to predict multiple time steps ahead. One way to tackle this issue is to feed a prediction to the model, and keep proceeding like this with predicted inputs. The more predicted inputs we use, the more error we are adding.

5. It might be useful to "resample data". For instance, by averaging all available points for one day.

6. It is also possible to use different models for different sensors, assuming they are providing different information. A better way to tackle this would be to enrich the model with some discrete variable, regarding the location of the sensor, for instance. These kind of features should be added to the final DNN layer.