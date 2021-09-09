import itertools
import time
from nltk import word_tokenize

from inverted_index.documents_and_text import save_file
from inverted_index.text_preprocessing import stem_and_lem
from ranking.scoring_corpus import sort_dict


def edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """All edits that are two edits away from `word`."""
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))


def get_alt_spell(query, all_terms):
    """For each query, generate different spelling for each term\n
    query: string"""
    q1 = word_tokenize(query)
    alternatives = []
    for term in q1:
        alternatives.append(edits2(term))
    keepers = []
    i = 0
    for alts in alternatives:
        keepers.append([])
        for alt in alts:
            if alt in all_terms:
                keepers[i].append(alt)
        i = i + 1
    # for i in range(len(keepers)):
    #     keepers[i] = stem_and_lem(keepers[i])
    return keepers


def get_alt_queries(alt_spell):
    """Get alternative queries from the different word spellings
     alt_spell: list of lists, each list represents alternatives for a word"""
    results = list(itertools.product(*alt_spell))
    return set(" ".join(q) for q in results)


def set_intersect(p1, p2):
    """Intersection function for boolean query\n
    p1,p2: set, list"""
    if len(p1) >= len(p2):
        return set(p1).intersection(p2)
    else:
        return set(p2).intersection(p1)


def post_filter(query, result):
    """A function that checks if a query exist in a document the way it it\n
    query: String\n
    result: list of ids"""
    tokens_per_doc = save_file('l', 'tokens_per_doc')
    document_id = save_file('l', 'document_id')
    true_result = []
    for doc in result:
        lst = tokens_per_doc.get(document_id.inverse.get(doc))
        text = ' '.join(lst)
        if query in text:
            true_result.append(doc)
    return true_result


def top_alt_queries(alt_queries, inverted_index):
    """Get the top 3 queries from the alternative queries\n
    alt_queries: a set of alternative queries"""
    results = dict()
    top_3 = dict()
    for query in alt_queries:
        terms = []
        for word in query.split(" "):
            terms.append(inverted_index.get(word)[1])
        while len(terms) > 1:
            new_term = set_intersect(terms[0], terms[1])
            terms[1] = new_term
            terms = terms[1:]
            terms[0] = post_filter(query, terms[0])
        results[query] = len(terms[0])
    sorted_dict = sort_dict(results)
    i = 0
    for q in sorted_dict:
        if i == 3:
            break
        top_3[q] = sorted_dict.get(q)
        i = i + 1
    return top_3


def check_spell(query, all_terms, inverted_index):
    """Putting all the work together"""
    alts = get_alt_spell(query, all_terms)
    alt_queries = get_alt_queries(alts)
    return list(top_alt_queries(alt_queries, inverted_index))[0]
