import BioLogic
import pandas as pd 
import numpy as np 
import glob
import os.path 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from numpy import matlib

mpr_files = sorted(glob.glob('C:\\Users\\User\\Documents\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis New\\HCl\\*.mpr')) 

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

    ax.axvline(x=np_data[:,3][minimum], color='red', linewidth=0.5, linestyle='--')

    plt.show()

def barComparison():

    fig = plt.figure()
    fig.set_size_inches(6, 6)
    fig.add_subplot(2, 1, 1)

    plt.subplots_adjust(hspace = 0.4)

    CuHCl_Voltages = [-0.813540518283844, -0.6889398694038391, -0.5106261968612671, -0.4431435167789459]
    CuHCl_Treatments = ['2V (Erratic)', '0.1V 0.1mAh', '2V Plating', '2V Plating 2']
    CuHCl_y_pos = np.arange(len(CuHCl_Treatments))

    plt.bar(CuHCl_y_pos, CuHCl_Voltages, width = 0.4, align='center', alpha=0.8)
    plt.xticks(CuHCl_y_pos, CuHCl_Treatments)
    plt.ylabel('Voltage').set_style('italic')
    plt.xlabel('Treatment').set_style('italic')
    plt.title('HCl Treatment').set_weight('bold')

    fig.add_subplot(2, 1, 2)
        
    CuAcH_Voltages = [-0.5769994854927063, -0.5840930938720703, -0.993, -0.6766124963760376, -0.40689000487327576, -0.3836333453655243]
    CuAcH_Treatments = ['2V 0.1mAh', '1.3V 0.1mAh', '2V 0.01mAh', '2V Plating', '2V 1mAh', '2V 1mAh Plating']
    CuAcH_y_pos = np.arange(len(CuAcH_Treatments))

    plt.bar(CuAcH_y_pos, CuAcH_Voltages, width = 0.4, align='center', alpha=0.8)
    plt.xticks(CuAcH_y_pos, CuAcH_Treatments)
    plt.ylabel('Voltage').set_style('italic')
    plt.xlabel('Treatment').set_style('italic')
    plt.title('AcH Treatment').set_weight('bold')

    plt.show()

for i, eChemFile in enumerate(mpr_files):
    mpr = BioLogic.MPRfile(eChemFile)
    df = pd.DataFrame(mpr.data)
    df = df.loc[:, df.columns.intersection(['time/s', 'Ewe/V'])]
    df['time/hr'] = df['time/s']/3600
    df['time/min'] = df['time/s']/60
    np_data = df.to_numpy()

    list = np_data[:,1].tolist()
    minimum = np.argmin(np_data[:,1])
    print(list[minimum])

    #plotGraph()

    if i+1 == 10:
        break

barComparison()
