#importing the necessary libraries
import pubchempy as pb


# Reading the list of compounds
with open('compound_list.txt', 'r') as file:
    files = file.readlines()
    for i,x in enumerate(files):
        try:
        # Downloading and saving the compound
            pb.download('SDF', f'SDF_FORMAT/{x}.sdf', (f'{x}'), 'name')
        # Checking if the compound is already downloaded
        except OSError:
            print('Already downloaded')
        except :
            print(f"{x} can't be found in the DATABASE")
        else:
            print(f'{x} is downloaded')

print("Conversion completed.")
