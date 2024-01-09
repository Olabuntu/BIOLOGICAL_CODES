import selenium as se
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

cids = []
Chemical_Classes = []   



website = 'https://pubchem.ncbi.nlm.nih.gov/'
driver = webdriver.Chrome()

with open('list.txt', 'r') as file: 
    files = file.readlines()
    for y in files:

        driver.get(website)
        time.sleep(4)


        driver.find_element(By.XPATH, '//div/form/div/div/input').send_keys(y)

        driver.find_element(By.CLASS_NAME, "main-search-submit").click()
        time.sleep(5)
        driver.find_element(By.XPATH, '//*[@id="featured-results"]/div/div[2]/div/div[1]/div[2]/div[1]/a').click()
        time.sleep(3)
        try:
            cid = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/div/section[1]/div/div/div/div[1]/div[2]").text
            clas = driver.find_element(By.XPATH, '//*[@id="Chemical-Classes"]/div[2]/div[1]').text
            with open('pubchem_info.csv', 'a') as f:
                f.write(f'{cid},{clas} \n')
        except :
            with open('pubchem_info.csv', 'a') as f:
                f.write(f'{cid}, no class \n')

