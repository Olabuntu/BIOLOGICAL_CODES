from rdkit import Chem
from rdkit.Chem import Descriptors
import pubchempy as pb
import pandas as pd


NAME = []
SMILE = []
MW = []
HBA = []
HBD = []
LogP = []
Violation_score = []
Drugability = []
synonyms =[]

A ={'COMPOUND NAME':NAME,'SYNONYM' :synonyms, 'CANONICAL SMILE':SMILE, 'MOLECULAR WEIGHT':MW, 'HYDROGEN BOUND ACCEPTOR':HBA, 'HYDROGEN BOUND DONOR':HBD,'LIPOHILICITY':LogP , 'VIOLATION SCORE':Violation_score, 'DRUGABILITY':Drugability}
file = open('a1.txt', 'rt')
for i,X in enumerate(file):
    F = X.strip()
    x = F.upper()

    compounds = pb.get_compounds(x, 'name' )
    compound = compounds[0]
    if compound.synonyms:
       synonyms1 = compound.synonyms[0]
        
    else:
        pass
            # Assuming you want the first compound in the search result
            
            # Get the SMILES string
    smiles = compound.canonical_smiles

    mol = Chem.MolFromSmiles( smiles)  

    # Ro5 descriptors
    MW1= Descriptors.MolWt(mol)
    HBA1 = Descriptors.NOCount(mol)
    HBD1 = Descriptors.NHOHCount(mol)
    LogP1 = Descriptors.MolLogP(mol)
    Violation_score1 = 0

    if MW1 > 500:
        Violation_score1 += 1
    if HBA1 > 10:
        Violation_score1 += 1
    if HBD1 > 5:
        Violation_score1 += 1
    if LogP1 > 5 :
        Violation_score1 += 1
    NAME.append(x)
    SMILE.append(smiles)
    MW.append(MW1)
    HBA.append(HBA1)
    HBD.append(HBD1)
    LogP.append(LogP1)
    synonyms.append(synonyms1)
    Violation_score.append(Violation_score1)
    if Violation_score1 > 1:
        Drugability1 = 'NOT DRUGABLE'
    else:
        Drugability1 = 'DRUGABLE'

    Drugability.append(Drugability1)    
Table = pd.DataFrame(A)
Table.to_csv('lipinski_Dr.csv', index=False)


