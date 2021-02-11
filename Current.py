import BioLogic
import pandas as pd
import numpy as np
import seaborn as sns
import glob
import os.path
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
from numpy import diff


mpr_files = sorted(glob.glob('C:\\Users\\User\\Documents\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis Original Time\\*.txt'))

for i, eChemFile in enumerate(mpr_files):
    df = pd.read_csv(eChemFile, sep='\t', skiprows=0, header=0)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    print(os.path.basename(eChemFile))
    print(df['time/s'].iloc[-1])
    closest = df.iloc[(df['time/s']-64800).abs().argsort()[:2]]
    print(closest)