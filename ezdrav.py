from selenium import webdriver
from bs4 import BeautifulSoup
import time

class ezdrav:
    def scrape(pro, urg, reg):
        driver = webdriver.Chrome()

        driver.get("https://cakalnedobe.ezdrav.si")
        js = "document.getElementById('procedureId').value = '" + str(pro) + "';"
        driver.execute_script(js)
   
        urgency = driver.find_element_by_id("urgencyTypeIdP")
        urgencies = urgency.find_elements_by_tag_name('option')
        urgencies[urg].click()
  
        region = driver.find_element_by_id("regionId")
        regions = region.find_elements_by_tag_name('option')
        regions[reg].click()
  
        driver.find_element_by_id("btnProcedureSubmit").click()

        time.sleep(1)
        
        html = driver.page_source
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
                if et.find("+386") != -1:
                    telefon.append(et)
                    nt = False
                    break
            if(nt): telefon.append("ni podan")
            if(ne): email.append("ni podan")
            c+=1
            
        driver.quit()
        err = ""
        if ime == []:
            err = soup.find('div',{"class":"col-md-12 error message-error"}).text.strip()
        driver.quit()
        return [postopek, ime,okvirni_termin,cakalna_doba,telefon,email,err]
    
data = ezdrav.scrape(1255,0,0)
print(data[0])
for i, n in enumerate(data[2]):
            print(data[1][i])
            print(data[2][i])
            print(data[3][i])
            print(data[4][i])
            print(data[5][i])
            print("")
print(data[6])