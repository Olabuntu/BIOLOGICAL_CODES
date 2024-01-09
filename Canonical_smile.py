#importing the libraries
import pubchempy as pb

file = open('compound_list.txt', 'rt')
with open('list.txt', 'w') as f:
    list = f.readlines()
    for i,x in enumerate(list):

        try:

            compounds = pb.get_compounds(x, 'name' )
            compound = compounds[0]  # for the first compound
                        
                        # Get the SMILES string
            smiles = compound.canonical_smiles
            with open('smiles.txt', 'a') as f:
                f.write(f'{smiles} \n')
            print(f'{i+1} is downloaded')

        except:
            print(f'{i+1} is not found')