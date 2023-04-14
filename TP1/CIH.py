import json
import re

file = open('sdsds.xml', 'r', encoding="utf-8")
text = file.read().splitlines()
text2 = file.read()

filtered_file = open('New_CIH_Bilingual_Medical_Glossary_English_Spanish.xml', 'w', encoding="utf-8")
filtered_file.write(text2)
new_text = re.sub(r'<literallayout>(\n\s*(.*))*</literallayout>', ' ', text2)
filtered_file.write(new_text)
lista1 = []
lista2 = []
for i in text:
    match = re.search(r"<|>",i)
    if match == None:
        lista1.append(i)
for a in lista1:
    new = a.strip()
    lista2.append(new)
print(lista2)
    
file.close()
filtered_file.close()




'''lista1 =re.search(r"<entry>(\n\s*(.*))*</entry>",text)
print(lista1)
lista2 = re.findall(r"(?<=<para>\n)([^\n]+)", lista1)'''

'''json_CIH = open('json_CIH.json', 'w', encoding="utf-8")
json_CIH.close()'''