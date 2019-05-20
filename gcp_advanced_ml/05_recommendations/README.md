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