# importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pubchempy as p

driver = webdriver.Chrome()

list = []
Formula = []
Molecular_weight=[]
Num_heavy_atoms =[]
Num_arom_heavyatoms=[]
Fraction_Csp3 =[]
Num_rotatable_bonds = []
Num_Hbond_acceptors =[]
Num_Hbond_donors =[]
Molar_Refractivity =[]
TPSA = []
LogPo_wiLOGP = []
LogPo_wXLOGP3 = []
LogPo_wWLOGP = []
LogPo_wMLOGP = []
LogPo_wSILICOS_IT = []
Consensus_LogPow = []
LogS_ESOL =[]
Solubility = []
Class1 =[]
LogS_Ali = []
Solubility2 = []
Class2 =[]
LogS_SILICOS_IT =[]
Solubility3 =[]
Class3 =[]
GI_absorption= []
BBB_permeant =[]
Pgp_substrate = []
CYP1A2_inhibitor = []
CYP2C19_inhibitor = []
CYP2C9_inhibitor = []
CYP2D6_inhibitor = []
CYP3A4_inhibitor = []
LogKp_skin_permeation = []
Lipinski = []
Ghose = []
Veber = []
Egan = []
Muegge = []
Bioavailability_Score = []
PAINS = []
Brenk = []
Leadlikeness = []
Synthetic_accessibility = []

dict = {'compound Name': list,'Formula': Formula, 'Molecular weight' : Molecular_weight, 'Num. heavy atoms' : Num_heavy_atoms, 'Num. arom. heavy atoms': Num_arom_heavyatoms, 
        'Fraction Csp3':Fraction_Csp3, 'Num. rotatable bonds':Num_rotatable_bonds, 'Num. H-bond acceptors':Num_Hbond_acceptors, 'Num. H-bond donors':Num_Hbond_donors, 'Molar Refractivity':Molar_Refractivity, 'TPSA':TPSA, 'Log Po/w (iLOGP)':LogPo_wiLOGP,
        'Log Po/w (XLOGP3)':LogPo_wXLOGP3, 'Log Po/w (WLOGP)':LogPo_wWLOGP, 'Log Po/w (MLOGP)':LogPo_wMLOGP, 'Log Po/w (SILICOS-IT)':LogPo_wSILICOS_IT,'Consensus Log Po/w':Consensus_LogPow,'Log S (ESOL)':LogS_ESOL, 'Solubility':Solubility, 'Class':Class1,
        'Log S (Ali)':LogS_Ali, 'Solubility 2':Solubility2, 'Class 2':Class2, 'Log S (SILICOS-IT)':LogS_SILICOS_IT, 'Solubility 3':Solubility3, 'Class 3':Class3,  'GI absorption':GI_absorption, 'BBB permeant':BBB_permeant, 'P-gp substrate':Pgp_substrate,
        'CYP1A2 inhibitor':CYP1A2_inhibitor, 'CYP2C19 inhibitor':CYP2C19_inhibitor, 'CYP2C9 inhibitor':CYP2C9_inhibitor, 'CYP2D6 inhibitor':CYP2D6_inhibitor, 'CYP3A4 inhibitor':CYP3A4_inhibitor, 'Log Kp (skin permeation)':LogKp_skin_permeation,
        'Lipinski':Lipinski, 'Ghose':Ghose, 'Veber':Veber, 'Egan':Egan, 'Muegge':Muegge, 'Bioavailability Score':Bioavailability_Score,'PAINS':PAINS, 'Brenk':Brenk, 'Leadlikeness':Leadlikeness, 'Synthetic accessibility':Synthetic_accessibility}
time.sleep(2)
try:
       
        with open('compounds.txt', 'r') as file, open('comp.txt', 'r') as file1:

                for x,y in zip(file, file1):
                        list.append(y)

                        driver.get('http://www.swissadme.ch/index.php')
                
                        click = driver.find_element(By.NAME, 'smiles')
                        click.send_keys(x)
                        driver.find_element(By.ID, 'submitButton').click()
                                                                
                    

                        
                        b2 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[2]/td[2]').text
                        Formula.append(b2)
                        b3 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[3]/td[2]').text
                        Molecular_weight.append(b3)
                        b4 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[4]/td[2]').text
                        Num_heavy_atoms.append(b4)
                        b5 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[5]/td[2]').text
                        Num_arom_heavyatoms.append(b5)
                        b6 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[6]/td[2]').text
                        Fraction_Csp3.append(b6)
                        b7 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[7]/td[2]').text
                        Num_rotatable_bonds.append(b7)
                        b8 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[8]/td[2]').text
                        Num_Hbond_acceptors.append(b8)
                        b9 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[9]/td[2]').text
                        Num_Hbond_donors.append(b9)
                        b10 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[10]/td[2]').text
                        Molar_Refractivity.append(b10)
                        b11 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[11]/td[2]').text
                        TPSA.append(b11)
                        b13 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[13]/td[2]').text
                        LogPo_wiLOGP.append(b13)
                        b14 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[14]/td[2]').text
                        LogPo_wXLOGP3.append(b14)
                        b15 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[15]/td[2]').text
                        LogPo_wWLOGP.append(b15)
                        b16 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[16]/td[2]').text
                        LogPo_wMLOGP.append(b16)
                        b17 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[17]/td[2]').text
                        LogPo_wSILICOS_IT.append(b17)
                        b18 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[3]/table[2]/tbody/tr[18]/td[2]').text
                        Consensus_LogPow.append(b18)
                        a1 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[2]/td[2]').text
                        LogS_ESOL.append(a1)
                        a2 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[3]/td[2]').text
                        Solubility.append(a2)
                        a3 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[4]/td[2]').text
                        Class1.append(a3)
                        a4 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[5]/td[2]').text
                        LogS_Ali.append(a4)
                        a5 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[6]/td[2]').text
                        Solubility2.append(a5)
                        a6 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[7]/td[2]').text
                        Class2.append(a6)
                        a7 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[8]/td[2]').text
                        LogS_SILICOS_IT.append(a7)
                        a8 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[9]/td[2]').text
                        Solubility3.append(a8)
                        a9 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[10]/td[2]').text
                        Class3.append(a9)
                        a11 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[12]/td[2]').text
                        GI_absorption.append(a11)
                        a12 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[13]/td[2]').text
                        BBB_permeant.append(a12)
                        a13 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[14]/td[2]').text
                        Pgp_substrate.append(a13)
                        a14 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[15]/td[2]').text
                        CYP1A2_inhibitor.append(a14)
                        a15 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[16]/td[2]').text
                        CYP2C19_inhibitor.append(a15)
                        a16 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[17]/td[2]').text
                        CYP2C9_inhibitor.append(a16)
                        a17 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[18]/td[2]').text
                        CYP2D6_inhibitor.append(a17)
                        a18 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[19]/td[2]').text
                        CYP3A4_inhibitor.append(a18)
                        a19 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[20]/td[2]').text
                        LogKp_skin_permeation.append(a19)
                        a21 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[22]/td[2]').text
                        Lipinski.append(a21)
                        a22 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[23]/td[2]').text
                        Ghose.append(a22)
                        a23 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[24]/td[2]').text
                        Veber.append(a23)
                        a24 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[25]/td[2]').text
                        Egan.append(a24)
                        a25 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[26]/td[2]').text
                        Muegge.append(a25)
                        a26 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[27]/td[2]').text
                        Bioavailability_Score.append(a26)
                        a28 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[30]/td[2]').text
                        PAINS.append(a28)
                        a29 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[31]/td[2]').text
                        Brenk.append(a29)
                        a30 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[32]/td[2]').text
                        Leadlikeness.append(a30)
                        a31 = driver.find_element(By.XPATH, f'//*[@id="sib_body"]/div[11]/div[1]/div[4]/table/tbody/tr[33]/td[2]').text
                        Synthetic_accessibility.append(a31)

                        time.sleep(2)
except:
        pass



table = pd.DataFrame(dict)
table.to_csv('ADMET_Swiss.csv',index=False)
                        
                        
                        





