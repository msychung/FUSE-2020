import glob
import os.path
import pandas as pd

current_mpr_files = sorted(glob.glob('C:\\Users\\User\\Documents\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Current Extraction\\HCl\\*.txt'))
#print('\n'.join(current_mpr_files))

for i, eChemFileCurrent in enumerate(current_mpr_files):
    df = pd.read_csv(eChemFileCurrent, sep='\t', skiprows=0, header=0)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]    #gets rid of the Unnamed column
    Currents = df['<I>/mA'].tolist()

    next((i for i, x in enumerate(Currents) if x), None)
    val = next((index for index,value in enumerate(Currents) if value != 0), None)  #uses next() to find the first value, or return None if there isn't one. enumerate() is used to make an iterator that iterates over index,value tuples so that we know the index that we're at

    # m = df.ne(0).idxmax()
    # PlatingCurrent = pd.DataFrame(dict(pos=m, val=df.lookup(m, m.index)))

    #print(os.path.basename(eChemFileCurrent))
    print(Currents[val+3])
  
