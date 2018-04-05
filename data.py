from bs4 import BeautifulSoup
import requests
import json

# urgencies, regions
url = "https://cakalnedobe.ezdrav.si/"
html = requests.get(url).text
soup = BeautifulSoup(html,'html.parser')
options = soup.find_all('option')

urg = options[0:3]
f = open('urgencies.txt','w')
for u in urg:
    f.write(u.text + " : " + str(u['value']) + '\n')
f.close()
print("urgencies done")

reg = options[3:len(options)-3]
f = open('regions.txt','w')
for r in reg:
    f.write(r.text + " : " + str(r['value']) + '\n')
f.close()
print("regions done")

# procedures
url = "https://cakalnedobe.ezdrav.si/Home/GetProcedures"
pro = json.loads(requests.get(url).text)
f = open('procedures.txt','w')
for p in pro:
    f.write(str(p['Id']) + " : " + str(p['Name']) + '\n')
f.close()
print("procedures done")
