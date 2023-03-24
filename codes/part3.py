"""
Natural Language Process

since the last part of filtering out the adjective from the list is not successful, 
I decided to give a score by using SentimentIntensityAnalyze to each review we have. 
Because we have stored the review in a dictonary format, we need to transfer it into string """


from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pickle

# SentimentIntensityAnalyze expect a string

with open("sheldon_reviews.pickle", "rb") as f:
    review_hist = pickle.load(f)


def nlp_process():
    scores = []
    for review in review_hist.values():
        # convert review to string
        review_str = str(review)
        # get polarity scores
        score = SentimentIntensityAnalyzer().polarity_scores(review_str)
        scores.append(score)
    return scores


scores = nlp_process()
# print(scores)

# pip install fuzzywuzzy
# pip install python-Levenshtein
from fuzzywuzzy import fuzz


def showsimilar_review():
    reference_review = "Not sure how people are crapping on this show,.. it is wholesome,charming and reminds me of a better version of Wonder Years..how they made a better version of wonder years i have no idea,.. but here it is,..maybe it's the influx of mindless remakes and zombie movies since early 2000s that have made people forget what good programming / writing and Casting look like!?"
    similar_reviews = {}
    for key, review in review_hist.items():
        score = fuzz.ratio(reference_review, review)
        if score > 40:  # set a threshold for similarity
            similar_reviews[key] = review
    """we selected a review from the review_hist and put it as a reference_review. 
    The result turned out that the model could found out it and we set the loop only print out the score larger than 99 and it successfuly print out 
    but if we only type several key words in there the similarity score is much lower than we expected."""
    return similar_reviews


# print(showsimilar_review())


# The clustering section helped by chatgpt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# install it from the terminal pip install matplotlib


def clustering():
    # Create TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Fit-transform on reviews
    tfidf_matrix = tfidf_vectorizer.fit_transform(review_hist.values())

    # Calculate cosine similarity matrix
    cosine_sim_matrix = cosine_similarity(tfidf_matrix)

    # Apply MDS to the distance matrix
    mds = MDS(n_components=2, dissimilarity="precomputed")
    mds_coordinates = mds.fit_transform(1 - cosine_sim_matrix)

    # Plot the coordinates
    plt.scatter(mds_coordinates[:, 0], mds_coordinates[:, 1])
    plt.show()


def main():
    print(scores)
    print(showsimilar_review())
    clustering()


main()

if __name__ == "__main__":
    main()
