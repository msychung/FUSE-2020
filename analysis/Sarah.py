import BioLogic
import pandas as pd 
import numpy as np 
import glob
import os.path 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from numpy import matlib

mpr_files = sorted(glob.glob('C:\\Users\\User\\Documents\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\*.mpr')) 
    
def slicing(df):
    mini=min(df['Ewe/V'])
    ind=df.set_index('Ewe/V').index.get_loc(mini)
    points=[]
    maxi=df['Ewe/V'][0]
    diff=maxi-mini
    dfrange=(maxi-mini)/2

    if dfrange <0.1:
        for n in df['Ewe/V'][ind::-1]:
            if n > (mini+dfrange):
                upper=df.set_index('Ewe/V').index.get_loc(n)
                delta = ind-upper
                if delta<15:
                    delta=delta+10
                points.append(upper)
                points.append(delta+ind)
                return points

    else:
        for n in df['Ewe/V'][ind::-1]:
            if n >= (mini+0.2):
                upper=df.set_index('Ewe/V').index.get_loc(n)
                delta = ind-upper
                if delta<15:
                    delta=delta+10
                points.append(upper)
                points.append(delta+ind)
                return points

def derivative(df):
    mini = df.set_index('Ewe/V').index.get_loc(min(df['Ewe/V']))
    dvdt = np.gradient(df['Ewe/V'])
    #return dvdt[mini]
    return mini

def plotGraph():
    fig = plt.figure()
    fig.set_size_inches(14, 6)

    global ax
    ax = fig.add_subplot(1, 1, 1)   #1x1 grid, 1st subplot

    ax.scatter(np_data[:,3], np_data[:,1], color='black', marker='x', s=2)

    ax.set_xlabel('Time / min').set_style('italic')
    ax.set_ylabel('$E_{we} / V$').set_style('italic')

    Title = os.path.basename(eChemFile)        # or: Title = pathlib.PurePath (eChemFile)
    plt.title(Title.strip('.mpr')).set_weight('bold')

    plt.grid(color=(.8, .8, .8))    #linestyle='-.', linewdith=0.7
    ax.spines['right'].set_color((.8, .8, .8))
    ax.spines['top'].set_color((.8, .8, .8))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(axis='y', labelcolor='black')
    ax.axhline(y=0, color='red', linewidth=0.5)

    ax.axvline(x=np_data[:,3][slicing(df)[0]], color='red', linewidth=0.5, linestyle='--')
    #ax.axvline(x=np_data[:,3][derivative(df)], color='red', linewidth=0.5)

    plt.show()

for i, eChemFile in enumerate(mpr_files):
    mpr = BioLogic.MPRfile(eChemFile)
    df = pd.DataFrame(mpr.data)
    df = df.loc[:, df.columns.intersection(['time/s', 'Ewe/V'])]
    df['time/hr'] = df['time/s']/3600
    df['time/min'] = df['time/s']/60
    np_data = df.to_numpy()

    plotGraph()

    if i+1 == 4:
        break
