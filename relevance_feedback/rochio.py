import re
import time

from nltk import word_tokenize
import numpy as np

from inverted_index.text_preprocessing import stem_and_lem
from ranking.scoring_corpus import tf_idf_query


# Get the unique terms and vectors from query and list of documents
def unique_terms_and_vectors(f):
    terms = []
    vectors = []
    for term in f:
        words = stem_and_lem(word_tokenize(re.sub("[^a-zA-Z0-9]+", " ", term)))
        vectors.append(words)
        for word in words:
            if word.lower() not in terms:
                terms.append(word.lower())
    return terms, vectors


# Vectorization of the vectors and giving weights to terms
def creat_vectors(terms, vectors):
    vec = []
    n = len(terms)
    for vector in vectors:
        d = [0] * n
        for term in vector:
            count = 0
            for word in terms:
                if word == term:
                    d[count] = 1
                count = count + 1
        vec.append(d)
    return vec


# Getting the modified query vector qm
def get_qm(vec):
    q0 = vec[0]
    vec = vec[1:]
    return list(np.array(q0) + (1 / len(vec)) * np.array(vec).sum(0))


# Get the alternative query based on qm
def alt_query(qm, terms):
    alt = []
    for i in range(len(qm)):
        if qm[i] > 0:
            alt.append(terms[i])
    return " ".join(alt)


# # Putting everything together
def rochio_algorithm(rf):
    terms, vectors = unique_terms_and_vectors(rf)
    vec = creat_vectors(terms, vectors)
    qm = get_qm(vec)
    return alt_query(qm, terms)

