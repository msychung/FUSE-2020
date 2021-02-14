import pandas as pd
import numpy as np
import glob
import os.path

'''
Finds final recorded time for sample set, and returns the two nearest data points (time and current) to 64800 seconds.

(Unfortunately, I cannot remember why this length of time was chosen, and may have been arbritary, or a parameter to be changed)
'''

# analysisNew = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis New\\"
# analysisOriginal = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis Original\\"
analysisOriginalTime = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis Original Time\\"

mpr_files = sorted(glob.glob(analysisOriginalTime + '*.txt'))

for i, eChemFile in enumerate(mpr_files):
    df = pd.read_csv(eChemFile, sep='\t', skiprows=0, header=0)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]        #gets rid of the Unnamed column in the dataframe
    finaltime = df['time/s'].iloc[-1]   #finds final value in the time column 

    print("\n \n" + os.path.basename(eChemFile))
    print("Final time recorded is: ", finaltime, "s, or ", finaltime/3600, "hr")
    closest = df.iloc[(df['time/s']-64800).abs().argsort()[:2]]
    print("Closest measured time(s) to 64800s, with corresponding currents: ")
    print(closest)