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
