import json
import re

file = open('CIH_Bilingual_Medical_Glossary_English_Spanish.xml', 'r', encoding="utf-8")
text = file.read()
file.close()
file1 = open('CIH_Editado.xml', 'w', encoding="utf-8")

'Remove linhas que nao tem fonte="4 ou 5"'
text = re.sub(r'(.*)(font="[0-3|6-9]")(.*)', '', text, flags=re.MULTILINE)
text = re.sub(r'(.*)(font="10")(.*)', '', text, flags=re.MULTILINE)

'Retira linhas que nao tem nada entre > <'
text = re.sub(r'^<text\s.*?>(\s)</text>$', '', text, flags=re.MULTILINE)

'Retira linhas sem nada entre<b> e </b>'
text = re.sub(r'(.*)<b>\s*</b>(.*)', '', text, flags=re.MULTILINE)

'Retira paragrafos desnecessarios'
text = re.sub(r'(.*)(fontspec)(.*)', '', text, flags=re.MULTILINE)
text = re.sub(r'(.*)(page)(.*)', '', text, flags=re.MULTILINE)
text = re.sub(r'(.*)(pdf2xml)(.*)', '', text, flags=re.MULTILINE)
text = re.sub(r'(.*)(xml)(.*)', '', text, flags=re.MULTILINE)
text = re.sub(r'(.*)(<i>)(.*)', '', text, flags=re.MULTILINE)
text = re.sub(r'^\s*$', '*', text, flags=re.MULTILINE)
text = re.sub(r'\*{2}', '*', text, flags=re.MULTILINE)
file1.write(text)
file1.close()
file2 = open('CIH_Editado.xml', 'r', encoding="utf-8")
text2 = file2.read().splitlines()
file2.close()

lista = []
'Limpar lista'
for i in text2:
    match = re.search(r"(.*)", i)
    if "*" in i:
        lista.append(i)
    else:
        if match:
            new_i = match.group()
            new_i = re.sub(r'<b>|</b>', '', new_i)
            newmatch = re.search(r'(?<=>)(.*)(?=<)', new_i)
            if newmatch:
                new_i = newmatch.group()
                new_i = new_i.strip()
                lista.append(new_i)
        
for i in range(20):
    lista.pop(0)
print(lista)
json_file = open('CIH.json', 'w', encoding="utf-8")

string = ''
lista_usados = []
dict = {}
for i in lista:
    if i in lista_usados:
        print(1)
    else:
        pos = lista.index(i)
        a = lista[pos+1]
        match1 = re.search(r'(\*){1}', a)
        if match1:
            a = lista[pos+2]
            dict[i] = a
            lista_usados.append(a)
        else:
            match2 = re.search(r'(\*){1}', lista[pos+1])
            if match2 == None:
                a = lista[pos+1]
                lista_usados.append(a)
                match3 = re.search(r'(^[a-z])|^[\(]|Humana|Salud|Paciente|Estreptococcica|Adquirida|Papanicolau|Vaccine', lista[pos+2])
                if match3:
                    match4 = re.search(r'(^[a-z])|^[\(]|Humana|Salud|Paciente|Estreptococcica|Adquirida|Papanicolau|Vaccine', lista[pos+3])
                    lista_usados.append(lista[pos+2])
                    if match4:
                        match5 = re.search(r'(^[a-z])|^[\(]|Humana|Salud|Paciente|Estreptococcica|Adquirida|Papanicolau|Vaccine', lista[pos+4])
                        lista_usados.append(lista[pos+3])
                    else:
                        string = lista[pos+1] + lista[pos+2] + lista[pos+3]
                        dict[i] = string
                else:
                    string = lista[pos+1] + lista[pos+2]
                    dict[i] = string
            else:
                dict[i] = lista[pos+1]
                
                

json.dump(dict, json_file, ensure_ascii=False, indent=4)
json_file.close()




        



