from bidict import bidict
from nltk import word_tokenize
from documents_and_text import update_docs, update_inverted_index
from text_preprocessing import get_files, stem_and_lem, get_text


# ______________________________Build Essentials________________________________
# Build the Document ID map
def build_doc_id():
    """Building the unique document id invertible map"""
    files = get_files()
    document_id = bidict()
    for file in files:
        update_docs(file, document_id)
    return document_id


# Get the tokens
def get_tokens(documents):
    """Create a dict for tokens per document\n
    documents: dict, bidict"""
    tokens_per_doc = dict()
    for doc in documents:
        text = get_text(doc)
        tokens_per_doc[doc] = stem_and_lem(text)
    return tokens_per_doc


# Get the terms
def get_terms(tokens_per_doc):
    """Create a dict for terms per document\n
    documents: dict"""
    terms_per_doc = dict()
    for doc in tokens_per_doc:
        terms_per_doc[doc] = set(tokens_per_doc.get(doc))
    return terms_per_doc


# get the biword terms
def get_biword_terms(tokens_per_doc):
    """Create a dict for biword terms per document\n
    documents: dict"""
    biword_terms = dict()
    for doc in tokens_per_doc:
        biword_list = list()
        tokens = tokens_per_doc.get(doc)
        n = len(tokens)
        if n > 1:
            for i in range(n - 1):
                biword_list.append(tokens[i] + ' ' + tokens[i + 1])
            biword_terms[doc] = set(biword_list)
        else:
            biword_terms[doc] = set(tokens)
    return biword_terms


def number_in_dict(x):
    """Returns the total length of the values in a dict\n
    x: dict"""
    count = 0
    for token in x:
        count = count + len(x.get(token))
    return count


def unique_in_dict(x):
    """Returns the total number of the unique values in a dict\n
    x: dict"""
    unique = set()
    for token in x:
        for term in x.get(token):
            unique.add(term)
    return len(unique)


# build the inverted index
def single_inverted_index(documents, terms):
    """Building the single word inverted index\n
    documents: bidict of documents and ids\n
    terms: dict of terms per document"""
    inverted_index = dict()
    for doc in documents:
        words = terms.get(doc)
        for word in words:
            update_inverted_index(word, doc, inverted_index, documents)
    return inverted_index


# Build the biword index
def biword_inverted_index(documents, biword_terms):
    """Building the biword inverted index\n
    documents: bidict of documents and ids\n
    terms: dict of biword terms per document"""
    biword_index = dict()
    for doc in documents:
        biword_words = biword_terms.get(doc)
        for biword_word in biword_words:
            update_inverted_index(biword_word, doc, biword_index, documents)
    return biword_index
