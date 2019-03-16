# Production ML Systems

---

## Week 1 - Architecting Production ML Systems

### The components of an ML system

#### Data ingestion
1. It might require streaming or batching.
2. GCP offers three solutions, PubSub (streaming), BigQuery (structured batch), and Cloud Storage (unstructured batch, for example, to train on that data later).

#### Data analysis
1. Poor data might introduce bugs that are really hard to catch.
2. Looking at its distribution is usually a good way of catching differences in its pattern.

#### Data validation
1. Some questions to understand whether the data is "healthy" or not (after a drop in performance):
- Is the new distribution similar enough to the old one?
- Are all expected features present?
- Are any unexpected features present?
- Do the features have the expected type?
- Does an expected proportion of the examples contain the feature?
- Do the examples have the expected number of values for feature?

#### Data transformation
1. Tranformations used at training should be also used at serving time.
2. GCP offer solutions such as Dataflow, Dataproc, and Dataprep

#### Trainer
1. It should support data and model parallelism, while scaling for multiple workers.
2. It should log and monitor key metrics, as well as support experimentation.
3. It should support hyperparameter tuning.
4. GCP offers ML Engine and GKE (Kubeflow).

#### Tuner
1. ML Engine support different strategies of hyperparameter tuning.

#### Model evaluation and validation
1. Ensures that the models are good before moving them into production.
2. Two main characteristics:
- It's safe (unlikely to crash, robust, and efficient)
- It outputs good predictions
3. Models are first evaluated offline.
4. Model validation ensures that there are warnings when certain thresholds are reached.
5. GCP offers this through TFX Model Analysis.

#### Serving
1. The serving component must be:
- Low latency
- Highly efficient
- Scale horizontally
- Reliable and robust
- Easy to update versions
2. GCP offers this through ML Engine and TF Serving (through kubernetes).

#### Logging
1. All logs should be easily accessible and integrated-
2. Offered through Cloud Reliability.

#### Shared config
1. Not having shared configuration might result in glue code, code written to join parts together. It's common when research teams write production code without taking the whole project into consideration. To solve this:
- Establish a common architecture for both R&D and production deployment
- Embed the teams together, so that engineering can influence the design of code from its inception
2. Orchestration glues all the components together. On GCP it is done with Cloud Composer. Another option is to use Argo, on GKE (Google Kubernetes Engine).3. Steps to compose a workflow in cloud composer:
- Define the Ops
- Arrange into a DAG
- Upload to the environment
- Explore DAG Run in Web UI

![](images/01.png)

#### Integrated frontend
1. The users of the system need to be able to easily accomplish their tasks, and as central a location as possible.
2. GCP offers ML Engine and TensorBoard.

#### Pipeline storage
1. Offered through Cloud Storage.


### Design Decisions

#### Training design decisions
1. Training might be static or dynamic. The major difference between them is that dynamic training requires the deployed model to keep gathering data, to re-train itself.

![](images/02.png)

2. Examples:
- Spam detection -> Static or dynamic (depending on how quickly spammers change)
- Android voice to text -> Static (global model) or Dynamic (personalized model)
- Shopping an conversion rate -> Static

3. Commonly, you might want to use dynamic, but in practice you start with static, since it's simpler.

4. Reference architecture for static training

![](images/03.png)

5. There are three potential architectures for dynamic training:
- Cloud Functions (for asynchronous training jobs)
- App Engine (for user-triggered training jobs)
- Cloud Dataflow (for continuous training)

6. Using Cloud Functions:

![](images/04.png)

7. Using Cloud Composer:

![](images/05.png)

8. Using AppEngine:

![](images/06.png)

9. Using Dataflow

![](images/07.png)

#### Serving design decisions
1. It is possible to serve statically or dinamically. The decision is based on a tradeoff between storage costs, CPU costs, and latency.

![](images/08.png)

![](images/09.png)

2. We might also think about in terms of:
- *Peakedness*, which is how concentrated the distribution is
- *Cardinality*, number of values in the set

3. The peakedness vs cardinality space gives us which type of serving to use. The hybrid approach has the most common values stored, and the long tail being dinamically computed, as requested.

![](images/10.png)

4. Examples:
- Spam detection -> Dynamic (low peakedness, high cardinality)
- Android voice to text -> Dynamic/hybrid
- Shopping ad conversion rate -> Static

5. Until now we've used dynamic serving (request in, model predicts, and we output it). If we were to use a static approach, we would have to make the following changes:
- Change Cloud MLE from online to batch prediction job
- Model accepts and passes keys as input
- Write predictions to a data warehouse (e.g. BigQuery)

### Serving on Cloud MLE

![](images/11.png)

### Designing an Architecture from Scratch

1. Things to keep in mind:
- What sort of training architecture is appropriate?
- What is the relationship between the features and labels like?
- Reasoning about the peakedness and cardinality of the data.

---

## Week 1 - Ingesting Data for Cloud-Based Analytics and ML

### Introduction

1. Data must be on the cloud to be leveraged by ML models.

2. Some challenges to get the data onto the cloud:
- Too much data
- Too little bandwidth
- Checksumming, encryption, firewalls
- No time and few resources

3. How to get your data on GCP?

![](images/12.png)

### Data Scenarios - Data On-Premise

1. Simply drag and drop into a GCP bucket.

2. Use `gsutil` to move the data.

3. `gsutil` has several "expected" commands. Using the flag `-m` enables multi-threading.

4. There are 4 types of GC storage:

![](images/13.png)

### Data Scenarios - Large Datasets

1. Large means > 60TB of data.

2. It is possible to use a physical google device, called _Transfer Appliance_, a high-capacity storage server (1PB).

3. If online transfer would take more than a week, then use transfer appliance.

4. Networks bottleneck at big data scale

![](images/14.png)

### Data Scenarios - Data on Other Clouds

1. `gsutil` allows you to transfer data from buckets setup on other regions, or even from S3 instances, etc.

2. It is possible to use the _transfer service_, using the GUI.

### Data Scenarios - Existing Databases

1. Choosing where your data should be stores

![](images/15.png)

2. Examples:
- Structured log data from monitoring IoT applications -> BigTable or Spanner
- Migrating your data analytics and reporting warehouse -> BigQuery
- Existing legacy Hadoop jobs -> DataProc (and run those jobs inside of a fully managed service)

3. BigQuery data transfer service

![](images/16.png)

4. Migrate databases to Cloud SQL/Spanner/Big Table

![](images/17.png)

5. Migrate Hadoop or HDFS to Cloud Dataproc

![](images/18.png)

### Demo: Automatic ETL Pipelines into GCP

1. ETL Pattern 1: Push solution architecture. This architecture is best for those wanting ad-hoc or invent based loading.

![](images/19.png)

2. ETL Pattern 2: Pull solution architecture. This architecture is best when you have repeatable processes and scheduled intervals.

![](images/20.png)

---

## Week 2 - Designing Adaptable ML Systems

### Adapting to Data

1. Things that might change with time and affect performance of the model:
- The upstream model
- Data sources maintained by another teams
- The relationship between features and labels (e.g. correlations that might hold only for certain splits of the data)
- The distribution of inputs

### Adapting to Data - Changing Distributions

1. It can happen that either labels or features change their distributions over time.

2. Extrapolation (generalize outside the bounds of what the model has seen on the training data) vs Interpolation (generalize within the bounds of the training data).

3. How to protect yourself from distribution changes:
- Monitor descriptive statistics for your inputs and outputs
- Monitor your residuals (difference between the predictions and your labels) as a function of your inputs
- Use custom weights in your loss function to emphasize data recency
- Use a dynamic training architecture and regularly retrain your model

4. _Legacy features_, are older features added at the time because they were valuable, but since then redundant with better features that were added afterwards.

5. _Bundled features_, are features added as part of a bundle, which are valuable collectively, but might not be individually.

6. Both legacy and bundled features represent additional unnecessary data dependencies.

7. There is _code smell_ in ML development as well. This is connected to "code that we can't inspect and are unable to easily modify, but that's added nonetheless to production frameworks".

### Adapting to Data - Right and Wrong Decisions

1. Some decisions are a matter of weighting cost versus benefit, such as short-term performance goals against long-term maintainability. Other are plainly about right and wrong.

2. Examples:
- Data leakage (e.g. using data that is not available at inference time, cross-contamination, etc.)

### Adapting to Data - System Failure

1. System fail - For example in e-commerce, if the transaction and payment server goes down on a certain time-period, the model sees data where people click on products, but don't buy them. One possible solution would be to roll back the model to a time prior to the model polution.

2. Feedback loops - Models have to be updated with regard to new users, new products, and new patterns. This is known as the cold start problem. The solution would be to dynamically retrain the model on newer data, besides undestanding the limits of the model. This is also true on adversarial environments, such as fraud detection.

### Mitigating Training-Serving Skew

1. Caused by:
- A discrepancy between how you handle data in the training and serving pipelines
- A change in the data between when you train and when you serve
- A feedback loop between your model and your algorithm

2. How code can create it:
- Different library versions that are functionally equivalent but optimized differently
- Different library versions that are not functionally equivalent
- Re-implemented solutions

### Lab: Serving ML Predictions in batch and real-time

![](images/21.png)

[code](https://github.com/GoogleCloudPlatform/training-data-analyst/tree/master/courses/machine_learning/deepdive/06_structured/serving)

### Debugging a Production Model

1. Example - Predicting widget demand

![](images/22.png)

2. Suddenly sales and inventory storage is down
- Feedback loop! Bad data -> ML Model -> Predicts low demand -> Product turnover increases -> ML Model
- Also a reminder that we often optimize for someting other than what we ultimate care about. In this case we were optimizing for matching predicted demand, when what we cared about was minimizing carrying costs in order to maximize profits.

3. Avoid treating dependent entries as independent, as they might fool the model.

4. Pause deployment whenever something out of the ordinary happens (avoids collecting poor data).

### Summary

1. Keep humans in the loop.

2. Prioritize maintainability.

3. Get ready to roll back.

---

## Week 2 - Designing High-performance ML Systems

_tbd_

---

## Week 2 - Hybrid ML Systems

_tbd_
