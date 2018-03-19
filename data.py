from bs4 import BeautifulSoup

with open('html/html-procedures.txt', 'r') as file:
    html=file.read().replace('\n', '')
    
soup = BeautifulSoup(html,"html.parser")
divs = soup.find_all('div',{"class":"option"})

procedures = {}
for d in divs:
    ids = d.attrs
    val = d.text
    n = int(ids['data-value'])
    procedures[val] = n
    
f = open('procedures.txt','w')
for p in procedures:
    f.write(p + " : " + str(procedures[p]) +'\n')
f.close()
print("procedures done")

with open('html/html-regions.txt', 'r') as file:
    html=file.read().replace('\n', '')

soup = BeautifulSoup(html,"html.parser")
re = soup.find_all('option')

regions = {}
i = 0
for r in re:
    regions[r.text] = i
    i+=1
    
f = open('regions.txt','w')
for r in regions:
    f.write(r + " : " + str(regions[r]) + '\n')
f.close()
print("regions done")
