import os
import time
import numpy as np
from nltk import word_tokenize
from inverted_index.documents_and_text import save_file
from inverted_index.text_preprocessing import stem_and_lem


# get the tf and df for each term
def extract_df_tf(inverted_index, tokens):
    tf_df = dict()
    for term in inverted_index:
        lst = inverted_index.get(term)
        tf_df[term] = [lst[0]]
        tf_df.get(term).append(dict())
        for doc_id in lst[1]:
            count = 0
            for token in tokens.get(doc_id):
                if token == term:
                    count = count + 1
            tf_df.get(term)[1][doc_id] = count
    return tf_df


# Calculate the tf-idf scores
def get_tf_idf(tf_df):
    tf_idf = dict()
    for term in tf_df:
        tf_idf[term] = dict()
        lst = tf_df.get(term)
        df = lst[0]
        for doc_id in lst[1]:
            tf_idf.get(term)[doc_id] = ((1 + np.log10(lst[1].get(doc_id))) * np.log10(1600 / df))
        for i in range(1, 1601, 1):
            if i not in lst[1]:
                tf_idf.get(term)[i] = ((1 + 0) * np.log10(1600 / df))
    return tf_idf


# Calculate the score for a query
def get_query_scores(query, tf_idf):
    q1 = word_tokenize(query)
    lst = stem_and_lem(q1)
    doc_scores = dict()
    for term in lst:
        if term in tf_idf:
            docs = tf_idf.get(term)
            for doc in docs:
                if doc in doc_scores:
                    doc_scores[doc] += docs.get(doc)
                else:
                    doc_scores[doc] = docs.get(doc)
    return doc_scores


# Get the top 5 queries
def get_top_10(doc_scores, document_id):
    top_10 = []
    # count = 0
    for doc in doc_scores:
        # if count == 10:
        #     break
        # print(str(count + 1) + '.', document_id.inverse[doc])
        top_10.append(document_id.inverse[doc])
        # count = count + 1
    return top_10


def get_image_name(top_10):
    dir = r'C:\\Users\\Omar\\Desktop\\CMPS 391\\Project\\Code\\web_interface\\static\\images1'
    img_src = []
    for top in top_10:
        top = top[:-3]
        for img in os.listdir(dir):
            if img.startswith(top):
                img_src.append(img)
                continue
    return img_src


def get_name(tf_idf_scores, image_names):
    names = []
    for doc in tf_idf_scores:
        names.append(image_names.get(doc))
    return names


# Sorting the dictionary
def sort_dict(x):
    """Sort a dictionary by key value\n
    x: dict()"""
    return dict(sorted(x.items(), key=lambda item: item[1], reverse=True))


# process the query using tf-idf and get the top 10 results
def tf_idf_query(query, tf_idf, image_names):
    doc_scores = get_query_scores(query, tf_idf)
    if len(doc_scores) == 0:
        return get_name(image_names, image_names)
    sorted_scores = sort_dict(doc_scores)
    '''Consider Removing this to get all of them and not just 10 for Ihab'''

    return get_name(sorted_scores, image_names)
