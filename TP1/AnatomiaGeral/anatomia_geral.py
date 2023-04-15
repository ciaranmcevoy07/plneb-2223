import json
import re

file = open('anatomia_geral.xml', 'r', encoding="utf-8")
text = file.read()
file.close()

text1 = re.sub(r'(.*)(font="1"|font="4")(.*)', '', text)
terms = re.findall(r'(?<=<b>)(.*?)(?=</b>)|(?<=<i>)(.*?)(?=</i>)', text1)

clean_list = []
new_list = [item for tup in terms for item in tup]
for i in new_list:
    if i != '':
        match = re.search(r'<b>|</b>|<i>|</i>', i)
        if match == None:
            clean_list.append(i)
clean_list2 = []
for i in clean_list:
    if len(i) != 1:
        a = i.strip()
        b = re.sub(r'\.', '', a)
        clean_list2.append(b)

file2 = open('anatomia_geral.xml', 'r', encoding="utf-8")
frases = file2.read().splitlines()
file2.close()
clean_list3 = []
for i in clean_list2:
        new_i = re.sub(r"[^a-zA-Z\s\(\)]", '', i)
        clean_list3.append(new_i)

file3 = open('new', 'w', encoding="utf-8")

for i in clean_list3:
    file3.write(i + "\n")
file3.close()


json_file = open('anatomia_geral.json', 'w', encoding="utf-8")
string = ''
dict = {}
for i in clean_list3:
    for a in frases:
        match2 = re.search(r"(<i>|<b>)(\s)" + i +r"\.(</i>|</b>)", a)
        if match2:
            pos = frases.index(a)
            pos = pos +1
            frase2 = re.search(r'(?<=>)(.*?)(?=<)', frases[pos])
            if frase2:
                frase_2 = frase2.group()
                clean_frase_2 = frase_2.strip()
                match = re.match(r'[0-9]+', clean_frase_2)
                if match:
                    print('1')
                else:
                    n = pos
                    match = re.match(r'[0-9]+', clean_frase_2)
                    while match is None:
                        string = string + clean_frase_2
                        n = n + 1
                        frase2 = re.search(r'(?<=>)(.*?)(?=<)', frases[n])
                        if frase2 is not None:
                            frase_2 = frase2.group()
                            clean_frase_2 = frase_2.strip()
                            match = re.match(r'[0-9]+', clean_frase_2)
                            if match:
                                dict[i] = {
                                    "desc":string
                                }
                                json.dump(dict, json_file, ensure_ascii=False, indent=4)
                                string = ''
                                dict = {}
                                break
json_file.close()














