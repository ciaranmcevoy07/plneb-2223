from bs4 import BeautifulSoup
import requests
import json

url = "https://www.atlasdasaude.pt/doencasAaZ"
html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

divs = soup.find_all("div", class_="views-row")
lista = []
for div in divs:
    title = div.div.h3.a.text
    desc = div.find("div", class_="field-content").text
    lista.append({title.strip():desc.strip()})
    
file = open("doencas.json", "w", encoding="utf-8")
json.dump(lista,file, ensure_ascii=False, indent = 4)
