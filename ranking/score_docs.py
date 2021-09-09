import os
import time

from inverted_index.documents_and_text import save_file
from ranking.scoring_corpus import get_tf_idf, extract_df_tf, sort_dict, tf_idf_query, get_query_scores, get_image_name

# invert_index = save_file('l', 'invert_index')
# tokens_per_doc = save_file('l', 'tokens_per_doc')
# document_id = save_file('l', 'document_id')
# tokens_per_doc2 = dict()
# for token in tokens_per_doc:
#     doc_id = document_id.get(token)
#     print(token, doc_id)
#     tokens_per_doc2[doc_id] = tokens_per_doc.get(token)
# save_file('p', 'tokens_per_doc2', tokens_per_doc2)
# save_file('j', 'tokens_per_doc2', tokens_per_doc2)
#
# # get the tf_df count
# tf_df = extract_df_tf(invert_index, tokens_per_doc2)
# save_file('p', 'tf_df', tf_df)
# save_file('j', 'tf_df', tf_df)
#
# # get the tf_idf scores
# tf_df = save_file('l', 'tf_df')
# print(len(tf_df))
# tf_idf = get_tf_idf(tf_df)
# save_file('p', 'tf_idf', tf_idf)
# save_file('j', 'tf_idf', tf_idf)
# tf_idf = save_file('l', 'tf_idf')
# sorted_tf_idf = dict()
# for term in tf_idf:
#     sorted_tf_idf[term] = sort_dict(tf_idf.get(term))
# save_file('p', 'sorted_tf_idf', sorted_tf_idf)
# save_file('j', 'sorted_tf_idf', sorted_tf_idf)
image_names = save_file('l', 'image_names')
sorted_tf_idf = save_file('l', 'sorted_tf_idf')
start = time.time()
print(tf_idf_query("drake", sorted_tf_idf, image_names))
end = time.time()
print(end-start)
# image_names = dict()
# start = time.time()
# for doc in document_id:
#     # if len(get_image_name([doc])) == 0:
#     print(doc)
#     print(document_id.get(doc))
#     image_names[document_id.get(doc)] = get_image_name([doc])[0]
# save_file('p', 'image_names', image_names)
# save_file('j', 'image_names', image_names)
# end = time.time()
# print(end - start)
