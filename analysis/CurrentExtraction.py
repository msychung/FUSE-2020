import glob
import os.path
import pandas as pd

'''
Finds the plating current for each cell, in mA.
'''

# Created variables to store different paths for easy switching 
CEAcH = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Current Extraction\\AcH\\"
CEHCl = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Current Extraction\\HCl\\"

current_mpr_files = sorted(glob.glob(CEHCl + '*.txt'))
# print('\n'.join(current_mpr_files))

for i, eChemFileCurrent in enumerate(current_mpr_files):
    df = pd.read_csv(eChemFileCurrent, sep='\t', skiprows=0, header=0)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]    #gets rid of the Unnamed column in the dataframe
    Currents = df['<I>/mA'].tolist()

    '''
    Using next() to find the first value, or return None if there isn't one. enumerate() is used to make an iterator that iterates over (index,value) tuples so that we know the index that we are at. This takes the form `next((i for i, x in enumerate(Currents) if x), None)`
    '''
    
    val = next((index for index, value in enumerate(Currents) if value != 0), None)  

    # m = df.ne(0).idxmax()
    # PlatingCurrent = pd.DataFrame(dict(pos=m, val=df.lookup(m, m.index)))

    print('\n', os.path.basename(eChemFileCurrent))
    print(Currents[val+3])  # Not 100% sure why I added 3 to the index...sorry!