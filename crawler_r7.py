from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# Acessando a URL
URL = 'https://jovempan.com.br/noticias'
html = urlopen(URL)

# Fazendo a Sopa
bs = BeautifulSoup(html, 'lxml')
print(bs.title)

# Criando Arquivo CSV
f = open('noticias_r7.csv','w', newline='', encoding="UTF-8")
w = csv.writer(f, dialect='excel',delimiter=';')

for i in bs.find_all("h2"):
    w.writerow([i.text])
    print(i.text)
f.close()
