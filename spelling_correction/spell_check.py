import time

from inverted_index.documents_and_text import save_file
from spellchecker import SpellChecker


# spell = SpellChecker()
# print(spell.unknown(['you re', 'meme']))
# # find those words that may be misspelled
# misspelled = spell.unknown("Draek memee".split(' '))
# for word in misspelled:
#     # Get the one `most likely` answer
#     print(spell.correction(word))
#
#     # Get a list of `likely` options
#     print(spell.candidates(word))
#

def check_spelling(all_terms, query):
    q = ''
    spell = SpellChecker()
    lst = spell.split_words(query)
    for word in lst:
        misspelled = spell.unknown(word)
        if len(misspelled) != 0:
            pos = spell.correction(word)
            if pos in all_terms:
                q = q + pos + ' '
            else:
                cand = spell.candidates(word)
                i = 0
                for can in cand:
                    if can in all_terms:
                        q = q + can + ' '
                        break
                    i = i + 1
                if i == len(cand):
                    q = q + pos + ' '
        else:
            q = q + word + ' '
    return q.strip(' ')

#
# all_terms = save_file('l', 'all_terms')
# print(check_spelling(all_terms,'spiderman pointing at spiderman'))
