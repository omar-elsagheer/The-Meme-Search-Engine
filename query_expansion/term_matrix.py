import time

from inverted_index.documents_and_text import save_file
from query_expansion.thesaurus_based import term_doc_matrix, get_C, thesaurus_algorithm, tdi_vector

terms_per_doc = save_file('l', 'terms_per_doc')
all_terms = set()
for doc in terms_per_doc:
    all_terms = all_terms.union(terms_per_doc.get(doc))
save_file('p', 'all_terms', all_terms)
all_terms = save_file('l', 'all_terms')
terms_lst = list(all_terms)
save_file('p', 'terms_lst', terms_lst)

tdi_matrix = term_doc_matrix()
save_file('p', 'tdi_matrix', tdi_matrix)
save_file('l', 'tdi_matrix', tdi_matrix)
# print(len(tdi_matrix))
# print(len(tdi_matrix[0]))
# print(len(tdi_matrix[69]))

tdi_matrix = save_file('l', 'tdi_matrix')
C = get_C(tdi_matrix)
arr_C = C.toarray()
save_file('p', 'C', arr_C)

# thesaurus_algorithm()
# terms_lst = save_file('l', 'terms_lst')
# C = save_file("l", "C")
# start = time.time()
# print(thesaurus_algorithm('me and the', C, terms_lst))
# end = time.time()
# print(end - start)
# query = 'drake meme'
# tdi_vec = tdi_vector(query, C)
# # print(tdi_vec)
# get_top_n(query, tdi_vec)
