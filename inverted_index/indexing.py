from inverted_index.build_inverted_index import build_doc_id, get_tokens, get_terms, single_inverted_index, \
    get_biword_terms, biword_inverted_index
from inverted_index.documents_and_text import save_file

# Creating the inverted Index
# document_id = build_doc_id()
# save_file('p', 'document_id', document_id)
# print("Done with this")
# tokens_per_doc = get_tokens(document_id)
# save_file('p', 'tokens_per_doc', tokens_per_doc)
# save_file('j', 'tokens_per_doc', tokens_per_doc)
# print("Done with this")
# terms_per_doc = get_terms(tokens_per_doc)
# save_file('p', 'terms_per_doc', terms_per_doc)
# print("Done with this")
# invert_index = single_inverted_index(document_id, terms_per_doc)
# save_file('p', 'invert_index', invert_index)
# save_file('j', 'invert_index', invert_index)
# print("Done with this")

#
# def get_triword_terms(tokens_per_doc):
#     """Create a dict for biword terms per document\n
#     documents: dict"""
#     triword_terms = dict()
#     for doc in tokens_per_doc:
#         triword_list = list()
#         tokens = tokens_per_doc.get(doc)
#         n = len(tokens)
#         if n > 1:
#             for i in range(n - 2):
#                 triword_list.append(tokens[i] + ' ' + tokens[i + 1] + ' ' + tokens[i + 2])
#             triword_terms[doc] = set(triword_list)
#         else:
#             triword_terms[doc] = set(tokens)
#     return triword_terms


def get_4word_terms(tokens_per_doc):
    """Create a dict for biword terms per document\n
    documents: dict"""
    triword_terms = dict()
    for doc in tokens_per_doc:
        triword_list = list()
        tokens = tokens_per_doc.get(doc)
        n = len(tokens)
        if n > 1:
            for i in range(n - 3):
                triword_list.append(tokens[i] + ' ' + tokens[i + 1] + ' ' + tokens[i + 2] + ' ' + tokens[i + 3])
            triword_terms[doc] = set(triword_list)
        else:
            triword_terms[doc] = set(tokens)
    return triword_terms


tokens_per_doc = save_file('l', 'tokens_per_doc')
four_word_terms = get_4word_terms(tokens_per_doc)
save_file('p', 'four_word_terms', four_word_terms)

