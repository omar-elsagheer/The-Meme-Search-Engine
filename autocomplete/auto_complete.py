from inverted_index.documents_and_text import save_file

from fast_autocomplete import AutoComplete


def auto_complete(words, word):
    auto = []
    autocomplete = AutoComplete(words=words)
    for phrase in autocomplete.search(word=word, max_cost=3, size=5):
        auto.append(phrase[0])
    return auto

# def build_words():
#     words = dict()
#     all_terms = save_file('l', 'all_terms')
#     biword_terms = save_file('l', 'biword_terms')
#     triword_terms = save_file('l', 'triword_terms')
#     four_word_terms = save_file('l', 'four_word_terms')
#     for term in all_terms:
#         words[term] = {}
#     for doc in biword_terms:
#         for biword in biword_terms.get(doc):
#             words[biword] = {}
#     for doc in triword_terms:
#         for triword in triword_terms.get(doc):
#             words[triword] = {}
#     for doc in four_word_terms:
#         for four_word in four_word_terms.get(doc):
#             words[four_word] = {}
#     return words
#
#
# words = build_words()
# save_file('p', 'words', words)
# save_file('j', 'words', words)


# words = save_file('l', 'words')
# word = 'rick and'
# print(auto_complete(words,word))
