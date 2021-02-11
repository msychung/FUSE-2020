import BioLogic
import pandas as pd 
import numpy as np 
import glob
import os.path 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter
from kneed import KneeLocator

mpr_files = sorted(glob.glob('C:\\Users\\User\\Documents\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis Original\\*.mpr')) 

def plotGraph():
    fig = plt.figure()
    fig.set_size_inches(14, 6)

    global ax
    ax = fig.add_subplot(1, 1, 1)   #1x1 grid, 1st subplot

    ax.scatter(np_data_cut[:,3], np_data_cut[:,1], color='black', marker='x', s=2)

    ax.set_xlabel('Time / min').set_style('italic')
    ax.set_ylabel('$E_{we} / V$').set_style('italic')

    Title = os.path.basename(eChemFile)        # or: Title = pathlib.PurePath (eChemFile)
    plt.title(Title.strip('.mpr')).set_weight('bold')
    #print(Title.strip('.mpr'))

    plt.grid(color=(.8, .8, .8))    #linestyle='-.', linewdith=0.7
    ax.spines['right'].set_color((.8, .8, .8))
    ax.spines['top'].set_color((.8, .8, .8))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(axis='y', labelcolor='black')
    ax.axhline(y=0, color='red', linewidth=0.5)

    ax.axvline(x = kneedle.knee, color='red', linewidth=0.5, linestyle='--')

    #y[x.index(kn.knee)]   to get y coordinates of knee

    plt.show()

def barComparison():

    # fig = plt.figure()
    # fig.set_size_inches(6, 6)
    # fig.add_subplot(2, 1, 1)

    # plt.subplots_adjust(hspace = 0.4)

    # CuHCl_Voltages = [-0.15988153219223022, -0.17048443853855133, -0.4431435167789459]
    # CuHCl_Treatments = ['2V (Erratic)', '2V Plating', '2V Plating 2']
    # CuHCl_y_pos = np.arange(len(CuHCl_Treatments))

    # plt.bar(CuHCl_y_pos, CuHCl_Voltages, width = 0.4, align='center', alpha=0.8)
    # plt.xticks(CuHCl_y_pos, CuHCl_Treatments)
    # plt.ylabel('Voltage').set_style('italic')
    # plt.xlabel('Treatment').set_style('italic')
    # plt.title('HCl Treatment').set_weight('bold')

    # fig.add_subplot(2, 1, 2)
        
    # CuAcH_Voltages = [-0.11868062615394592, -0.35521629452705383, -0.9868888258934021, -0.6756008863449097, -0.40689000487327576, -0.3836333453655243]
    # CuAcH_Treatments = ['2V 0.1mAh', '1.3V 0.1mAh', '2V 0.01mAh', '2V Plating', '2V 1mAh', '2V 1mAh Plating']
    # CuAcH_y_pos = np.arange(len(CuAcH_Treatments))

    # plt.bar(CuAcH_y_pos, CuAcH_Voltages, width = 0.4, align='center', alpha=0.8)
    # plt.xticks(CuAcH_y_pos, CuAcH_Treatments)
    # plt.ylabel('Voltage').set_style('italic')
    # plt.xlabel('Treatment').set_style('italic')
    # plt.title('AcH Treatment').set_weight('bold')

    fig = plt.figure()
    fig.set_size_inches(6, 6)
    ax = fig.add_subplot(1, 1, 1)

    Voltages = [-0.088241403, -0.242107034, -0.06751815, -0.0971542, -0.376451677]
    Treatments = ['N2', 'O2', 'Ar-O2', 'Mesh', 'O2N2']
    y_pos = np.arange(len(Treatments))

    plt.bar(y_pos, Voltages, width = 0.4, align='center', alpha=0.8)
    plt.xticks(y_pos, Treatments)
    plt.ylabel('Voltage').set_style('italic')
    plt.xlabel('Treatment').set_style('italic')
    plt.title('Overpotential under different gas atmospheres (AVERAGES)').set_weight('bold')
    ax.invert_yaxis()

    plt.show()

for i, eChemFile in enumerate(mpr_files):

    # if i+1 != 12:
    #     continue

    # if i+1 == 10:
    #     break

    mpr = BioLogic.MPRfile(eChemFile)
    df = pd.DataFrame(mpr.data)
    df = df.loc[:, df.columns.intersection(['time/s', 'Ewe/V'])]
    df['time/hr'] = df['time/s']/3600
    df['time/min'] = df['time/s']/60
    np_data = df.to_numpy()

    #print(os.path.basename(eChemFile))

    # der_y = np.gradient(np_data[:,1], np_data[:,3])     
    # #print(der_y[500:650])

    # for n in der_y:
    #     der_y = der_y[(der_y > -100)]

    # cut = list(range(0, (len(np_data)-len(der_y)+1)))
    # np_data_cut = np_data[(len(np_data)-len(der_y)):]

    np_data_cut = np_data[(np_data[:,1] < 0.1)]

    kneedle = KneeLocator(np_data_cut[:,3], np_data_cut[:,1], S=100, curve='convex', direction='increasing', interp_method='interp1d',)

    Voltage = np_data[:,1].tolist()
    Time = np_data[:,3].tolist()

    VertIndex = Time.index(kneedle.knee)
    #print(Voltage[VertIndex])

    plotGraph()
    
#barComparison()
