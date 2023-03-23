
import re
import json

file = open('novo_dicionario_medico.json', 'r', encoding="utf-8")
textjson = file.read()
json_obj = json.loads(textjson)
html = open('livro_anotado.html', 'r', encoding='utf8')
linhas = html.read().splitlines()
html_new = open('livro_anotado_new.html', 'w', encoding='utf8')
for line in linhas:
    for key in json_obj:
        a = re.search(r'\b' + key + r'\b', line, re.IGNORECASE)
        if a != None:
            line = line.lower()
            line = re.sub(r'\b' + key + r'\b', r'<b>' + key + r'</b>', line)
    html_new.write(line + "\n")
html_new.close


