import json
import re

file = open('sdsds.xml', 'r', encoding="utf-8")
text = file.read().splitlines()
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




'''lista1 =re.search(r"<entry>(\n\s*(.*))*</entry>",text)
print(lista1)
lista2 = re.findall(r"(?<=<para>\n)([^\n]+)", lista1)'''

'''json_CIH = open('json_CIH.json', 'w', encoding="utf-8")
json_CIH.close()'''