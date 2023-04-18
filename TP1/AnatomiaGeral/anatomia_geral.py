import json
import re

file = open('anatomia_geral.xml', 'r', encoding="utf-8")
text = file.read()
file.close()
text1 = re.sub(r'(.*)(font="1"|font="4"|font="9"|font="7")(.*)', '', text)
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

file = open('anatomia_geral.xml', 'r', encoding="utf-8")
new_file = open('anatomia_geral_editado.xml', 'w', encoding="utf-8")
new_frases = file.read().splitlines()
elementos_juntos = []
for i in clean_list2:
        a = re.search(r'^.*-\s*$', i)
        count = clean_list2.index(i)
        new_elem = ''
        if a:
            b = re.sub(r'-$', '', i)
            new_elem = b + clean_list[count+1]
            elementos_juntos.append(new_elem)
        else:
            a = re.search(r'^.*-\s*$', clean_list2[count-1])
            if a == None:
                elementos_juntos.append(i)

for i in new_frases:
    match1 = re.search(r'(?<=<b>)(.*?)(?=</b>)|(?<=<i>)(.*?)(?=</i>)', i)
    count = new_frases.index(i)
    if match1:
        linha1 = match1.group()
        a = re.search(r'^.*-\s*$', linha1)
        if a:
            filtered_linha1 = re.sub(r'-$', '', linha1)
            match2 = re.search(r'(?<=<b>)(.*?)(?=</b>)|(?<=<i>)(.*?)(?=</i>)', new_frases[count+1])
            linha2 = match2.group()
            new_elem = ''
            new_elem = filtered_linha1 + linha2
            new_i = re.sub(r'(?<=<b>)(.*?)(?=</b>)|(?<=<i>)(.*?)(?=</i>)', new_elem, i)
            c = re.sub('ﬁ', 'fi', new_i)
            c = re.sub("ﬂ", "fl", c)
            c = re.sub(r"[\*\.]", '', c)
            c = re.sub('\[', '', c)
            c = re.sub('\]', '', c)
            new_file.write(c + '\n')
        else:
            match3 = re.search(r'(?<=<b>)(.*?)(?=</b>)|(?<=<i>)(.*?)(?=</i>)', new_frases[count-1])
            if match3:
                linha3 = match3.group()
                traco_match = re.search(r'^.*-\s*$', linha3)
                if traco_match ==None:
                    c = re.sub('ﬁ', 'fi', i)
                    c = re.sub("ﬂ", "fl", c)
                    c = re.sub(r"[\*\.]", '', c)
                    c = re.sub('\[', '', c)
                    c = re.sub('\]', '', c)
                    new_file.write(c + '\n')
            else:
                c = re.sub('ﬁ', 'fi', i)
                c = re.sub("ﬂ", "fl", c)
                c = re.sub(r"[\*\.]", '', c)
                c = re.sub('\[', '', c)
                c = re.sub('\]', '', c)
                new_file.write(c + '\n')
    else:
        c = re.sub('ﬁ', 'fi', i)
        c = re.sub("ﬂ", "fl", c)
        c = re.sub(r"[\*\.]", '', c)
        c = re.sub('\[', '', c)
        c = re.sub('\]', '', c)
        new_file.write(c + '\n')
new_file.close()
file.close()

file2 = open('anatomia_geral_editado.xml', 'r', encoding="utf-8")
frases = file2.read().splitlines()
file2.close()
clean_list3 = []
for i in elementos_juntos:
        c = re.sub('ﬁ', 'fi', i)
        c = re.sub("ﬂ", "fl", c)
        new_i = re.sub(r"[^a-zA-Z\s\(\)üáàâãçéèêíìîóòôõúùûÁÀÂÄÃÉÈÍÌÎÓÒÔÕÚÙ\-\<\>\"]", '', c)
        clean_list3.append(new_i)
print(clean_list3)

file4 = open('primeiroteste', 'w', encoding="utf-8")
for i in clean_list3:
    file4.write(i + "\n")
file4.close()

json_file = open('anatomia_geral.json', 'w', encoding="utf-8")
string = ''
dict = {}
for i in clean_list3:
    for a in frases:
        '''match2 = re.search(r"(<i>|<b>)(\s*)" + i +r"(\s*)(</i>|</b>)", a)'''
        match2 = re.search(r'<b>|</b>|<i>|</i>', a)
        if match2:
            if i in a:
                pos = frases.index(a)
                pos = pos +1
                frase2 = re.search(r'(?<=>)(.*?)(?=<)', frases[pos])
                if frase2:
                    frase_2 = frase2.group()
                    clean_frase_2 = frase_2.strip()
                    match = re.match(r'[0-9]+', clean_frase_2)
                    if match:
                        print('1')
                        dict[i] = ''
                    else:
                        n = pos
                        match = re.match(r'[0-9]+', clean_frase_2)
                        secondmatch = re.match(r'</page>', frases[n])
                        while match is None and secondmatch is None:
                            traco = re.search(r'^.*-\s*$', clean_frase_2)
                            if traco:
                                new_clean_frase_2 = re.sub(r'-$', ' ', clean_frase_2)
                                string = string + new_clean_frase_2
                            else:
                                string = string + clean_frase_2 + ' '
                            n = n + 1
                            frase2 = re.search(r'(?<=>)(.*?)(?=<)', frases[n])
                            if frase2 is not None:
                                frase_2 = frase2.group()
                                clean_frase_2 = frase_2.strip()
                                match = re.match(r'[0-9]+', clean_frase_2)
                                secondmatch = re.match(r'</page>', frases[n])
                                if match and secondmatch:
                                    break
                        string = re.sub(r"[^a-zA-Z\s\(\)áàâãçéèêíìîóòôõúùûÁÀÂÄÃÉÈÍÌÎÓÒÔÕÚÙ\-\.]", '', string)
                        dict[i] = string
                        string = ''
json.dump(dict, json_file, ensure_ascii=False, indent=4)
json_file.close()














