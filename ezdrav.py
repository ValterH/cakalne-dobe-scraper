import requests
from bs4 import BeautifulSoup
import re

class ezdrav:
    def scrape(pro, urg, reg):
        d = {'procedureId': pro, 'urgencyTypeIdp': urg, 'regionId': reg, 'btnProcedureSubmit': ''}
        req = requests.post("https://cakalnedobe.ezdrav.si/Home/ProcedureAppointmentSlots", data=d)
        
        html = req.text
        soup = BeautifulSoup(html,"html.parser")
        klinike = soup.find_all('div',{"class":"col-md-10 col-md-offset-1 well"})
        p = soup.find('h4')
        postopek = p.text
        c = 0
        ime = []
        cakalna_doba = []
        okvirni_termin = []
        email = []
        telefon = []
        for k in klinike:
            i = k.find('a').getText()
            ime.append(i)
    
            co1 = k.find_all('div',{"class":"row slotHeader"})
            co2 = k.find_all('div',{"class":"row slotData"})
            if (len(co1) > 1):
                ot = co1[0].text.strip() + ": " + co2[0].text.strip()
                cd = co1[1].text.strip() + ": " + co2[1].text.strip()
            else:
                ot = co1[0].text.strip()
                cd = co2[0].text.strip()
            okvirni_termin.append(ot.replace('\n',''))
            cakalna_doba.append(cd.replace('\n',''))

            teem = k.find_all('div',{"class":"col-md-6 propValue"})
            nt = True
            ne = True
            for te in teem:
                et = te.text.strip()
                if et.find("@") != -1:
                    ne = False
                    email.append(et)
                
                tel = re.findall(r'[\+\]?[1-9][0-9 .\-\(\)]{8,}[0-9]', et)
                if(len(tel)>0):
                    telefon.append(et)
                    nt = False
                    break
            if(nt): telefon.append("ni podan")
            if(ne): email.append("ni podan")
            c+=1
            
        err = ""
        if ime == []:
            err = soup.find('div',{"class":"col-md-12 error message-error"}).text.strip()
        
        return [postopek, ime,okvirni_termin,cakalna_doba,telefon,email,err]

    def firstfive(data):
        if(data[6] != ""):
            return [data[6]]
        else:
            return [data[0],data[1][:6],data[2][:6],data[3][:6],data[4][:6],data[5][:6]]
    def printdata(data):
        print(data[0])
        if(len(data)>1):
            for i, n in enumerate(data[1]):
                print(data[1][i])
                print(data[2][i])
                print(data[3][i])
                print(data[4][i])
                print(data[5][i])
        return
# TEST
data = ezdrav.scrape(847,7,9)
data = ezdrav.firstfive(data)
ezdrav.printdata(data)
