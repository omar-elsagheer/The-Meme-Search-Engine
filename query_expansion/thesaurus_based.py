import time

from nltk import word_tokenize

import numpy as np
from scipy.sparse import csr_matrix
from inverted_index.documents_and_text import save_file
from inverted_index.text_preprocessing import stem_and_lem
from ranking.scoring_corpus import tf_idf_query


# Generate the term document incidence matrix
def term_doc_matrix():
    inverted_index = save_file('l', 'invert_index')
    terms_lst = save_file('l', 'terms_lst')
    tdi_matrix = []
    for term in terms_lst:
        lst = [0] * 1608
        posting_list = inverted_index.get(term)[1]
        for i in posting_list:
            lst[i - 1] = 1
        tdi_matrix.append(lst)
    return tdi_matrix


# get the matrix C=A*A^T
def get_C(tdi_matrix):
    tdi_matrix = np.array(tdi_matrix)
    tdi_matrix_t = tdi_matrix.transpose()
    sparse_tdi = csr_matrix(tdi_matrix)
    sparse_tdi_t = csr_matrix(tdi_matrix_t)
    return sparse_tdi.dot(sparse_tdi_t)


# Sum the rows that corresponds to each word in the query to get the tdi vector of all the terms
def tdi_vector(query, C, terms_lst):
    query_terms = stem_and_lem(word_tokenize(query))
    if len(query_terms) == 0:
        return ''
    rows_of_query_terms = []
    for query_term in query_terms:
        if query_term in terms_lst:
            rows_of_query_terms.append(terms_lst.index(query_term))
    tdi_vec = []
    for index in rows_of_query_terms:
        tdi_vec.append(C[index])
    return list(np.array(tdi_vec).sum(0))


# Get the top n terms value
def get_n_value(tdi_vec, n=3):
    sorted_tdi = tdi_vec.copy()
    sorted_tdi.sort()
    top_n = []
    i = 1
    while True:
        if len(top_n) == n:
            break
        var = sorted_tdi[-i]
        if var not in top_n:
            top_n.append(var)
        i = i + 1
    return top_n


# Get the index of top n values
def get_n_index(top_n, tdi_vec):
    top_n_index = []
    for i in top_n:
        start = tdi_vec.index(i)
        top_n_index.append(start)
    return top_n_index


# Get the top n terms to add to the query
def get_top_n_terms(top_n_index, forbidden_values, terms_lst, n=2):
    top_n_terms = []
    for i in top_n_index:
        var = terms_lst[i]
        if var not in forbidden_values and var not in top_n_terms:
            top_n_terms.append(var)
        if len(top_n_terms) == n:
            break
    return ' '.join(top_n_terms)


# Putting everything together
def thesaurus_algorithm(query, C, terms_lst):
    tdi_vec = tdi_vector(query, C, terms_lst)
    if len(tdi_vec) == 0:
        return ''
    top_n = get_n_value(tdi_vec)
    top_n_index = get_n_index(top_n, tdi_vec)
    q = stem_and_lem(word_tokenize(query))
    top_n_terms = get_top_n_terms(top_n_index, q, terms_lst)
    alt = query + ' ' + top_n_terms
    return alt
