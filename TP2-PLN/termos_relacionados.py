import spacy
import re
from collections import Counter
import sys
import json

file = open("Final.json", "r", encoding="utf-8")
db = file.read()
file.close()
file = open("Final.json", "r", encoding="utf-8")
dic = json.load(file)
file.close()

nlp = spacy.load('pt_core_news_lg')
nlp.max_length = 3000000
av = nlp(db)
# Get word vectors for a target word
target_doc = nlp(db)

# Iterate over words in the vocabulary

similar_words = []
# for i in dic.keys():
#     target_word = nlp(i)
target_word = nlp("abdomen")
for token in target_doc:
    if token.text != target_word:
        similarity = nlp(target_word).similarity(token)
        similar_words.append((token.text, similarity))
        print(token.text)

# Sort similar words based on similarity score
similar_words = sorted(similar_words, key=lambda x: x[1], reverse=True)

# Print the similar words
for word, similarity in similar_words:
    print(word, similarity)
