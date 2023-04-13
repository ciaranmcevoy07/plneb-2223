import json
import re

file = open('CIH Bilingual Medical Glossary English-Spanish.xml', 'r', encoding="utf-8")
text = file.read()

lista1 =re.findall(r"<entry>(\n\s*(.*))*</entry>",text)

for i in lista1:
    print(i)
'lista2 = re.findall(r"(?<=<para>\n)([^\n]+)", lista1)'

'''json_CIH = open('json_CIH.json', 'w', encoding="utf-8")
json_CIH.close()'''
file.close()