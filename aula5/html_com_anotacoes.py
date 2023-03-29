import json, re
file = open('json_desc_pt_en.json', 'r', encoding="utf-8")
json_obj = json.load(file)

html = open('livro_anotado.html', 'r', encoding="utf-8")
linhas = html.read().splitlines()
html_new = open('livro_anotado_new.html', 'w', encoding='utf8')
blacklist = {"e", "de", "são"}

nova_lista = json_obj.keys() - blacklist
nova_lista.remove("L+")
nova_lista.add("L\+")

for line in linhas:
    for key in nova_lista:
        exp1 = r"\b" + key + r"\b"
        a = re.search(exp1, line, re.IGNORECASE)
        if a:
            line = line.lower()
            expression = f"<a href='' data-toggle='tooltip' title='{json_obj.get(key)}'>{key}</a>"
            exp2 = r"\b" + key + r"\b"
            line = re.sub(exp2, expression, line)
    html_new.write(line + "\n")
html.close()
html_new.close()
file.close()
file.close()


