from bs4 import BeautifulSoup

with open('html/html-procedures.txt', 'r') as file:
    html=file.read().replace('\n', '')
    
soup = BeautifulSoup(html,"html.parser")
divs = soup.find_all('div',{"class":"option"})

options = []
for d in divs:
    ids = d.attrs
    val = d.text
    o = ids['data-value'] + " : " + val
    options.append(o)

f = open('procedures.txt','w')
for o in options:
    f.write(o + '\n')
f.close()
print("procedures done")

with open('html/html-regions.txt', 'r') as file:
    html=file.read().replace('\n', '')

soup = BeautifulSoup(html,"html.parser")
re = soup.find_all('option')

regions = []
i = 0
for r in re:
    regions.append(str(i) + " : " + r.text)
    i+=1
    
f = open('regions.txt','w')
for r in regions:
    f.write(r + '\n')
f.close()
print("regions done")
