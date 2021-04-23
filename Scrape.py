import csv
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pandas as pd
import numpy as nm
import flask

url="https://charusat.edu.in:912/Uniexamresult/"

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument(f'user-agent={user_agent}')
# options.add_argument("--window-size=1920,1080")
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--allow-running-insecure-content')
# options.add_argument("--disable-extensions")
# options.add_argument("--proxy-server='direct://'")
# options.add_argument("--proxy-bypass-list=*")
# options.add_argument("--start-maximized")
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')
# r = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

r=webdriver.Chrome()

a=ActionChains(r)

id_no=[]
name=[]
sgpa=[]
# sgpa_2=[]
# sgpa_3=[]
# sgpa_4=[]
# sgpa_5=[]
# month_pre=["3911","4085","4385","4733","4917"]
s='18DCS'

results={}

r.get(url)

for i in range(1,136):
    try:
        d1=Select(r.find_element_by_id("ddlInst"))
        d1.select_by_value("21")

        d2=Select(r.find_element_by_id("ddlDegree"))
        d2.select_by_value("134")
                
        d3=Select(r.find_element_by_id("ddlSem"))
        d3.select_by_value("5")

        d4=Select(r.find_element_by_id("ddlScheduleExam"))
        d4.select_by_value("4917")
        
        # print(str(j)+' '+month_pre[j-1])
        
        s='18DCS'
        if(i>=1 and i<=9):
            s+='00'
            s+=str(i)
        elif(i>=10 and i<=99):
            s+='0'
            s+=str(i)
        elif(i>=136 and i<=164):
            s='D19DCS'
            s+=str(i)
        else:
            s+=str(i)

        r.find_element_by_id("txtEnrNo").send_keys(s)

        a.send_keys(Keys.RETURN).perform()

        d6=r.find_element_by_id("uclGrd1_lblExamNo")
        id_no.append(d6.text)

        d5=r.find_element_by_id("uclGrd1_lblStudentName")
        name.append(d5.text)

        # if(j==1):    
        d7=r.find_element_by_id("uclGrd1_lblSGPA")
        sgpa.append(d7.text)
            
        # elif(j==2):
        #     d8=r.find_element_by_id("uclGrd1_lblSGPA")
        #     sgpa_2.append(d8.text)
        
        # elif(j==3):
        #     d9=r.find_element_by_id("uclGrd1_lblSGPA")
        #     sgpa_3.append(d9.text)

        # elif(j==4):
        #     d10=r.find_element_by_id("uclGrd1_lblSGPA")
        #     sgpa_4.append(d10.text)

        # elif(j==5):
        #     d11=r.find_element_by_id("uclGrd1_lblSGPA")
        #     sgpa_5.append(d11.text)

        r.find_element_by_id('btnBack1').click()
    except:
        pass
# print(s)

r.quit()

results['ID']=id_no
results['NAME']=name
results['SGPA']=sgpa
# results['SGPA2']=sgpa_2
# results['SGPA3']=sgpa_3
# results['SGPA4']=sgpa_4
# results['SGPA5']=sgpa_5

# print(d5.text,sgpa,sgpa_2,sgpa_3,sgpa_4,sgpa_5)


# try:
d=pd.DataFrame(results)
print(d)
# except:
#     pass
d.to_csv('Sem-5.csv')

# print(results)
