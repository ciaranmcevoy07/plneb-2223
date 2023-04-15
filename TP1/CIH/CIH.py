import json
import re

file = open('CIH Bilingual Medical Glossary English-Spanish.xml', 'r', encoding="utf-8")
text = file.read()
file.close()

filtered_file = open('New_CIH_Bilingual_Medical_Glossary_English_Spanish.xml', 'w', encoding="utf-8")
new_text = re.sub(r'<literallayout>(\n\s*(.*))*</literallayout>', ' ', text)
"new_text2 = re.sub(r'<title>((.*\n*))*</title>', ' ', new_text)"
print(new_text)
filtered_file.write(new_text)
filtered_file.close()


file2 = open('New_CIH_Bilingual_Medical_Glossary_English_Spanish.xml', 'r', encoding="utf-8")
text2 = file2.read().splitlines()
file2.close()

lista1 = []
lista2 = []
for i in text2:
    match = re.search(r"<|>",i)
    if match == None:
        lista1.append(i)
for a in lista1:
    new = a.strip()
    lista2.append(new)
print(lista2)




'''lista1 =re.search(r"<entry>(\n\s*(.*))*</entry>",text)
print(lista1)
lista2 = re.findall(r"(?<=<para>\n)([^\n]+)", lista1)'''

'''json_CIH = open('json_CIH.json', 'w', encoding="utf-8")
json_CIH.close()'''