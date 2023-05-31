import spacy
import re
from collections import Counter
import sys
import json

file = open("teste1.json", "r", encoding="utf-8")
final = json.load(file)
file.close()

file = open("teste2.json", "r", encoding="utf-8")
mdsaude = json.load(file)
file.close()


dict = {}
nlp = spacy.load('pt_core_news_lg')
for i in final.keys():
    fi = nlp(i)
    text = ""
    for j in mdsaude.keys():
        md = nlp(j)
        score = fi.similarity(md)
        if score > 0.6:
            text += j+";"
    dict[i] = text

for i in final.keys():
    fi = nlp(i)
    if i in dict:
        text = dict[i]
    else:
        text = ""
    for j in final.keys():
        fi2 = nlp(j)
        score = fi.similarity(fi2)
        if score > 0.6:
            text += j+";"
    dict[i] = text

for i in mdsaude.keys():
    md = nlp(i)
    if i in dict:
        text = dict[i]
    else:
        text = ""
    for j in mdsaude.keys():
        md2 = nlp(j)
        score = md.similarity(md2)
        if score > 0.6:
            text += j+";"
    dict[i] = text
    
file = open("relacoes.json", "w", encoding="utf-8")
json.dump(dict,file, ensure_ascii=False, indent = 4)
file.close()



