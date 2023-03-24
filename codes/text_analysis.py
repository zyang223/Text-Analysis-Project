# Part 1 Parsing the reviews from IMDB
"""
we are using the api provided from instruction page by Professor Li to parse the movie review from IMDB
We are taking the example of Young Sheldon which is my favorite TV show as an example to show how to parse the data

Randomly Selected 10 different movie review from IMDB and collect them in a text file
1. Define a random number function
2. parse the review from IMDB
3. copy and write them in to a txt file
"""
# Preparation
import random
from imdb import Cinemagoer


# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search movie
"""input information"""
movie_name = "Young Sheldon"  # You could Substitue the movie name from here
total_review = 24
num_review = 24

movie = ia.search_movie(movie_name)[0]  # here is an example of how to parse the
print(f"The movieid you chose is :{movie.movieID}")
# '6226232'

movie_reviews = ia.get_movie_reviews(movie.movieID)
# print(movie_reviews['data']['reviews'][24]['content'])

"""ATTENTION
Since the api of the IMDB could only show the first 24th of the review, so we would take them all

"""


def random_num():
    """random number generataor"""
    review_number = []
    for i in range(num_review):
        n = random.randrange(0, total_review)  # number could be substitued from here
        review_number.append(n)
    print(review_number)
    return review_number


def parse_review():
    """get the review from API and store it in a dictonary format with according number"""
    sheldon_reviews = {}
    review_number = random_num()
    movie_reviews = ia.get_movie_reviews(movie.movieID)
    for number in review_number:
        review_text = movie_reviews["data"]["reviews"][number]["content"]
        sheldon_reviews[number] = review_text
    print(sheldon_reviews)
    return sheldon_reviews


sheldon_reviews = parse_review()

"""make the review into a file"""
import pickle

with open("sheldon_reviews.pickle", "wb") as f:
    pickle.dump(sheldon_reviews, f)


def main():
    parse_review()


if __name__ == "__main__":
    main()
