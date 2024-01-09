import selenium as se
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

pa3=[]
pi1=[]
line1=[]
name1=[]
tissue1=[]
type1=[]
smile =[]
names =[]




with open ('smiles.txt', 'r') as f, open('list.txt', 'r') as g:
    for x,j in zip(f,g):    

        try:

            site = 'https://www.way2drug.com/Cell-line/index.php'
            driver = webdriver.Chrome()
            driver.get(site)
            time.sleep(2)
            
            driver.find_element(By.XPATH, '//*[@id="myHeader3"]').click()
            driver.find_element(By.XPATH, '//*[@id="smi"]').send_keys(x)
            driver.find_element(By.XPATH, '//*[@id="myContent3"]/div/input[2]').click()
            time.sleep(4)



            driver.find_elements(By.TAG_NAME, "iframe")
            driver.switch_to.frame('upload_target')
            time.sleep(1)
            driver.switch_to.frame('protein')
        

 
            for i in range(2,9):
                Pa3= driver.find_element(By.XPATH, f'//*[@id="frm"]/table/tbody/tr[{i}]/td[1]').text
                Pi1= driver.find_element(By.XPATH, f'//*[@id="frm"]/table/tbody/tr[{i}]/td[2]').text
                Line1 = driver.find_element(By.XPATH, f'//*[@id="frm"]/table/tbody/tr[{i}]/td[3]/a').text
                Name1 = driver.find_element(By.XPATH, f'//*[@id="frm"]/table/tbody/tr[{i}]/td[4]').text
                Tissue1 = driver.find_element(By.XPATH, f'//*[@id="frm"]/table/tbody/tr[{i}]/td[5]').text
                Type1 = driver.find_element(By.XPATH, f'//*[@id="frm"]/table/tbody/tr[{i}]/td[6]').text
                type1.append(Type1)
                tissue1.append(Tissue1)
                name1.append(Name1)
                line1.append(Line1)
                pi1.append(Pi1)
                pa3.append(Pa3)
                smile.append(x)
                names.append(j)
            
        except:
            pass
Table = pd.DataFrame({'Compound Name':names,'SMILE':smile,'PA1':pa3,'PI1':pi1,'LINE':line1,'NAME':name1,'TISSUE':tissue1,'TYPE':type1}).to_csv('cell_line_info.csv', index=False)

