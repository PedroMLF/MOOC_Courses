# Recommendation Systems with TensorFlow on GCP

---

## Week 1 - Course Overview

![](images/01.png)

## Week 1 - Recommendation Systems

1. Recommendation systems:
- Help users find related content.
- Help users explore new items.
- Improve user decision making.

2. For producers:
- Increase user engagement.
- Learn more about customers.
- Change user behavior.

3. Recommendation systems provide a way to model people's preferences.

4. One of the core concepts is the `user-item` matrix, where rows are users, and columns are items.

5. Types of recommendation systems:
- Content-based recommender system.
- Collaborative filtering.
- Knowledge-based.
- Deep neural networks.

6. _Content-based filtering_ uses item features to recommend new items similar to what the user has liked in the past.

7. _Collaborative filtering_ uses similarities between users and items simultaneously to determine recommendations. It often involves matrix factorization.

8. _Knowledge-based_ recommender systems use explicit knowledge about the users, items, and recommendation criteria.

9. _Deep neural networks_ can combine information such as sequences of previously seen videos, genres, artists, etc., and train it to correctly predict the user rating to a given video.

10. Recommender systems pitfalls:
- The user and produce spaces are _sparse_ (most items are rated by very few users and most users only rate a small portion of items), and _skewed_ (some properties are very popular and some users are very prolific).
- There's the problem of _cold start_ when there are not enough interactions for a given user or item.

11. Explicit feedback is often rare or unobservable. It is much more common to use implicit feedback mechanisms: number of clicks, play counts, fraction of the video watched, site navigation, time spent on page, etc.

## Week 1 - Building a Simple Vector-Based Model

1. If we have embeddings of items we can use similarity functions to calculate which products are more similar between themselves.

2. It is possible to create a _user feature vector_ (given the properties of the items, and the ratings given by the user).

![](images/02.png)

3. Having user feature vectors, it is possible to find _user item ratings_ to make recommendations (given the user feature vector, and the properties of the items).

![](images/03.png)

4. If we have multiple users we stack the several matrices into a tensor, shaped as (#users, #movies, #features).

## Week 1 - Building a Content-Based Recommendation System with a Neural Network

1. It is possible to user user + movie features to train a model with a given objective (star rating, movie id, next content id, etc.)

## Week 1 - ALS, Matrix Factorization Algorithm for Collaborative Filtering

1. Content-based recommendations use similarities between items in an embedding space. This might be a limitation.

2. Collaborative filtering learns latent factors and can explore outside the user's personal bubble.

3. Collaborative filtering recommendations use similarities between item and users simultaneously in an embedding space.

4. It is based on a user-item matrix. Sometimes it is based on explicit feedback (rating), but most often it uses implicit feedback (user behavior with regard to a given item).

5. We can organize items according to several dimensions. Users will be categorized according to those dimensions as well. Then, it is possible to find how well a pair of user-item matches by taking the dot product between the two vectors.

6. These item and users embeddings might be learned from data. In particular, the data is compressed to find the best generalities to rely on, called _latent factors_.

![](images/04.png)

7. Steps of collaborative filtering:
- Factorize user-interactions matrix into user-factors and item-factors.
- Given user ID, multiply by item-factors to get predicted ratings for all items.
- Return top k rated items for this user.

8. Factorizing the matrix resembles the problem of least squares. There are several ways to solve it:
- SGD (Flexible, Parallel, but it is Slow, Hard to handle unobserved interaction pairs)
- Alternating Least Squares, ALS (Parallel, Fast, Easily handles unobserved interaction pairs, but only works for Least Squares)

![](images/05.png)

9. To handle unobserved user-interaction matrix pairs it is possible to use SVD, which sets all missing values to zero, or ALS, which ignores the missing values.

9. It is also possible to use a Weighted ALS (WALS), which uses weights instead of zeros.

![](images/06.png)

10. The ALS algorithm alternates between rows and columns to factorize tha matrix, as follows:

![](images/07.png)

![](images/08.png)

![](images/09.png)

11. To transform data (such as `userid` and `itemid`) into something that can be used by the ALS algorithm, we need to create a mapping function for those values.

12. Even though the update depends on the full column factor, it is possible to distribute WALS by precomputing the Gramian G (Gramian is the determinant if the matrix inner product X transpose X).

![](images/10.png)

## Week 1 - Implementing ALS in TensorFlow

1. WALS requires whole rows or columns, therefore the data has to be preprocessed to provide SparseTensors of rows/columns.

![](images/11.png)

![](images/12.png)

2. WALS Matrix Factorization Estimator:

![](images/13.png)

3. The input function has to read the files and create sparse tensors for the rows and columns.

![](images/14.png)

![](images/15.png)

4. Decode the TF Record files and invoke sparse_merge to create the necessary SparseTensor.

![](images/16.png)

![](images/17.png)

5. Remap keys to SparseTensor to fix re-indexing after batching

![](images/18.png)

![](images/19.png)

![](images/20.png)

![](images/21.png)

![](images/22.png)

![](images/23.png)

![](images/24.png)

6. Typically only the top K items by user are stored (or vice-versa).

7. Tensorflow Transform uses Cloud DataFlow in the analysis stage to create assets that TensorFlow uses in training and prediction:
- Read Google Analytics data from BigQuery.
- TF-Transform for analysis.
- Transform function that TF will use.
- Create vocabulary of VisitorID -> UserId and ContentId->ItemID
- Create the group-by dataset
- Convert to TF Records
- Write to cloud storage

![](images/25.png)

8. Collaborative filtering.
- Pros: No domain knowledge; Serendipity; Great starting point.
- Cons: Fresh items/users?; Context features?

9. To solve cold-start problems we might use a hybrid of content+collaborative filtering.

![](images/26.png)

---

## Week 2 - Neural Networks for Recommendation Systems

1. Real-world recommendation systems are a hybrid of three broad theoretical approaches:

![](images/27.png)

![](images/28.png)

2. Designing a movie recommendation system.
- Content based ideas:

![](images/29.png)

- Collaborative filtering ideas:

![](images/30.png)

- Knowledge-base systems ideas:

![](images/31.png)

## Week 2 - Incorporating Context

1. Example of context components
- Mood at the time
- Where you are
- Who you are with
- When you are experiencing the item
- etc.

2. Context-aware recommendation systems (CARS)
- Matrix is: users x items x context

3. There are three types of CARS algorithms:
- Contextual prefiltering.
- Contextual postfiltering.
- Contextual modeling.

4. Contextual prefiltering:
- A context matrix is used to filter some results.
- There are several different algorithms within contextual prefiltering. In _Item splitting_, where items are split into item context pairs. It uses the t-test to find splits. Similarly, there is _User splitting_. Finally, there is _User-item splitting_, which makes splits across both user and item dimensions at the same time.

![](images/32.png)

5. Contextual postfiltering:
- The main methods are _weight_ (weight calculated based on similar users) and _filter_ (filter items with value below a given threshold.).

![](images/33.png)

![](images/34.png)

![](images/35.png)

6. Contextual modeling:
- One of the main algorithms is the _Deviation-Based Context-Aware Matrix Factorization_. This implies knowing: How is user's rating deviated?; Contextual rating deviation (CRD); Looking at the deviations of users across context dimensions.

![](images/36.png)

7. For example, in the figure below, this means that the ratings for `Home` are usually 0.8 higher than for `Theater`, etc.

![](images/37.png)

![](images/38.png)

![](images/39.png)

![](images/40.png)

8. YouTube case study - Overview
- It uses two neural networks to recommend videos.

![](images/41.png)

9. YouTube case study - Candidate Generation

![](images/42.png)

![](images/43.png)

![](images/44.png)

10. YouTube case study - Ranking
- Video are weighted based on their watch time.

![](images/45.png)

![](images/46.png)

![](images/47.png)

![](images/48.png)

## Week 2 - Building an End-to-End Recommendation System

1. In recommendation systems it is necassary to automatically refresh the data, retrain the model, and redeploy the model.

![](images/49.png)

2. Two methods for running automated workflows on ML datasets will be explored:
- Regular end of the day schedule.
- Triggered workflow.

**Apache Airflow Environment**

3. Apache Airflow DAGs (Directed Acyclic Graph) can be used to orchestrate GCP services.

4. Cloud Composer is to Apache Airflow as Cloud ML Engine is to TensorFlow.

**DAGs and Operators**

5. The DAGs folder is simply a GCS bucket where the pipeline code is loaded into.

6. Airflow workflows are written in Python. This file creates a DAG.

7. Airflow uses _operators_ in your DAG to orchestrate other GCP services. Generally, you will only see one operator per task. These include _BigQuery operators_, _MLEngine Operators_, etc. Example of workflow using operators:

![](images/50.png)

8. Bad upstream data can ruin workflows. Therefore it is necessary to incorporate _health checks_ directly into the workflow (for instance the _BigQueryCheckOperator_ and the _BigQueryIntervalCheckOperator_).

![](images/51.png)

![](images/52.png)

9. The end of the provided code should set up the DAG dependencies. The visual UI is a great way to verify that everything is defined correctly.

**Workflow Scheduling**

10. Scheduling operations:
- Periodic
- Event-driven

![](images/53.png)

**Monitoring and Logging**

11. Monitor and alert based on pipeline status and auto retry in case of failure.

12. Monitor and troubleshoot Airflow step errors in logs.

13. Monitor Dataflow and Cloud Function health in Stackdriver.

14. It is good practice to manually run the DAG before scheduling or triggering it.

