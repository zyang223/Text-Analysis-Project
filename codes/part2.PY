# Part IIData cleanning and text analysis process
"""
1. open the file saved from part 1
2. doing a cleaning
3. Characterizing by Word Frequencies
4.Computing Summary Statistics
5.Removing Stop words
6.NLP
7.Text similarity
8. Text clustering



"""
import pickle

with open("sheldon_reviews.pickle", "rb") as f:
    review_hist = pickle.load(f)

# print(review_hist)


""" Concatenate the text strings"""
text = ""
for key in review_hist:
    text += review_hist[key] + " "

"""Remove unnecessary characters"""  # cleanning help from chat gpt
import re

text = re.sub(r"[^\w\s]", "", text)
text = re.sub(r"\d+", "", text)

# Split into individual words
review_clean = text.split()


"""section 1 statistics and cleaning"""

# Count the total number of word
def total_words():
    """count the total words"""
    totalword_count = len(review_clean)
    print("Total words:", totalword_count)
    return totalword_count


def different_words():
    """list the different words in the review"""
    return len(review_clean)


def frequency_words(review_clean):
    """find out the frequency of the word and show it in a descending order"""
    word_freq = {}
    for word in review_clean:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq


# frequency_words(review_clean)


def select_common(sorted_freq):
    res = []
    stopwords = []
    with open("stopwords.txt", "r") as f:
        for line in f:
            stopwords.append(line.strip().lower())  # Convert to lowercase

    for words, freq in sorted_freq:
        if words.lower() not in stopwords:  # Check if lowercase word is in stopwords
            res.append((freq, words))
        else:
            continue
    return res


sorted_freq = frequency_words(review_clean)
# select_common(sorted_freq)


word_common = select_common(sorted_freq)

"""In this part I was trying to receive help from chatgpt to filter out the adjective only here,
 because I found out while I filtered out the stopwords
there are still to many nouns and other common words in the list. 
I was trying to let adjective here stay only by using the ntlk and word_toknenize.
 But it seems its not working here """

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from collections import Counter


def filter_adj(review_clean):
    word_list = [word for word in review_clean if isinstance(word, str)]
    text = " ".join(word_list)
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)

    filtered_pos_tags = [(word, tag) for word, tag in pos_tags if tag == "JJ"]
    adj_list = [word for word, tag in filtered_pos_tags]

    return adj_list


def main():
    total_words()
    print(different_words())
    print("the result of frequncy words are :")
    print(frequency_words(review_clean))
    print("the result of filter stop_words are:")
    print(select_common(sorted_freq))
    print("the result of filter adjective are:")
    print(filter_adj(review_clean))


if __name__ == "__main__":
    main()
