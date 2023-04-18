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
text = re.sub(r'\n\s*\n', '\n', text)
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
'Retira primeiros paragrafos desnecessarios'        
for i in range(16):
    lista.pop(0)
json_file = open('CIH.json', 'w', encoding="utf-8")

'Serve para verificar fim de ligacao de palavras com traducao'
lista.append('')

lista_usados = []
dict = {}

'Liga as palavras com traducao correta'
for i in lista:
    string = ''
    if i in lista_usados or i == ':':
        print(1)
    else:
        pos = lista.index(i)
        if lista[pos+1] == '':
            break
        else:
            a = lista[pos+1]
            lista_usados.append(lista[pos+1])
            if lista[pos+2] == '':
                break
            else:
                match = re.search(r'(^[a-z])|^[\(\)]|^(Humana)|^(Salud)|^(Paciente)|^(Estreptococcica)|^(Adquirida)|^(Papanicolau)|^(Vaccine)', lista[pos+2])
                if match:
                    lista_usados.append(lista[pos+2])
                    if lista[pos+3] == '':
                        break
                    else:
                        match = re.search(r'(^[a-z])|^[\(\)]|^(Humana)|^(Salud)|^(Paciente)|^(Estreptococcica)|^(Adquirida)|^(Papanicolau)|^(Vaccine)', lista[pos+3])
                        if match:
                            lista_usados.append(lista[pos+3])
                            if lista[pos+4] == '':
                                break
                            else:
                                match = re.search(r'(^[a-z])|^[\(\)]|^(Humana)|^(Salud)|^(Paciente)|^(Estreptococcica)|^(Adquirida)|^(Papanicolau)|^(Vaccine)', lista[pos+4])
                                if match:
                                    lista_usados.append(lista[pos+3])
                                else:
                                    string = string + a + lista[pos+2] + lista[pos+3]
                                    dict[i] = string
                        else:
                            string = string +a + lista[pos+2]
                            dict[i] = string
                else:
                    string = string + a
                    dict[i] = string        

file4 = open('teste', 'w', encoding="utf-8")
for i in lista_usados:
    file4.write(i + "\n")
file4.close()

json.dump(dict, json_file, ensure_ascii=False, indent=4)
json_file.close()




        



