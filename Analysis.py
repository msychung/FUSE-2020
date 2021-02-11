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

mpr_files = sorted(glob.glob('C:\\Users\\User\\Documents\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis Original Time\\*.mpr')) 
#print('\n'.join(mpr_files))

def plotGraph():
    fig = plt.figure()
    fig.set_size_inches(14, 6)

    global ax
    ax = fig.add_subplot(1, 1, 1)   #1x1 grid, 1st subplot

    ax.scatter(np_data[:,3], np_data[:,1], color='black', marker='x', s=2)

    ax.set_xlabel('Time / min').set_style('italic')
    ax.set_ylabel('$E_{we} / V$').set_style('italic')

    Title = os.path.basename(eChemFile)        #or: Title = pathlib.PurePath (eChemFile)
    plt.title(Title.strip('.mpr')).set_weight('bold')

    plt.grid(color=(.8, .8, .8))    #linestyle='-.', linewdith=0.7
    ax.spines['right'].set_color((.8, .8, .8))
    ax.spines['top'].set_color((.8, .8, .8))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(axis='y', labelcolor='black')
    ax.axhline(y=0, color='red', linewidth=0.5)

    plotDer()
    plotDer2()

    #plt.show()

def plotDer():

    # der_y = diff(np_data[:,1]) / diff(np_data[:,3])   #has length n-1 since you can only start computing differences from 1st index
    # der_x = (np.data(np_data[:,3])[:-1] + np.data(np_data[:,3])[1:]) / 2

    global der_y, derp
    der_y = np.gradient(np_data[:,1], np_data[:,3])      #derivative will be computed using central differences and will have the same length as y, unlike numpy.diff, which uses forward differences and will return an (n-1) size vector.
    der_x = np_data[:,3]

    derp = ax.twinx()
    derp.scatter(der_x, der_y, color='blue', marker='^', s=2)
    derp.set_ylabel('Derivative').set_style('italic')
    derp.tick_params(axis='y', labelcolor='blue')

def plotDer2():

    # der_y2 = diff(der_y)/diff(der_x)
    # der_x2 = der_x[:-1]

    # myList = np_data[:,3].tolist()
    # der_y2 = [myList[n+1] + myList[n-1] - 2 * myList[n] for n in range(len(myList)-1)]
    # der_y2 = np.append(der_y2, [1])

    der_y2 = np.gradient(der_y, np_data[:,3])
    der_x2 = np_data[:,3]   # = der_x

    #derp2 = ax.twinx()
    derp.scatter(der_x2, der_y2, color='green', marker='d', s=2, alpha=0.4)

    #derp2.tick_params(axis='y', labelcolor='green')

    #Knee/Elbow point should be the point with max. absolute second derivative

for i, eChemFile in enumerate(mpr_files):   #for i, eChemFile in enumerate(mpr_files):  if too many files, then below an if i == x condition containing limited code
        global mpr
        global df
        mpr = BioLogic.MPRfile(eChemFile)
        df = pd.DataFrame(mpr.data)
        df = df.loc[:, df.columns.intersection(['time/s','Ewe/V'])] #gets rid of irrelevant data
        df['time/hr'] = df['time/s']/3600
        df['time/min'] = df['time/s']/60
        np_data = df.to_numpy()        # 0: time/s | 1: Ewe/V | 2: time/hr | 3: time/min

        print(os.path.basename(eChemFile))

        print(df['time/hr'].iloc[-1])

        #plotGraph()

        # if i+1 == 15:
        #     break




#=====================CLEANS UP COLUMNS APPARENTLY==========================
# def sanitize_labels(label):
#     return label.split('/')[0].lower().lstrip('-').translate(dict.fromkeys(map(ord, " ,|()-"),'_')).rstrip('_')

# df.columns = [sanitize_labels(label) for label in df.columns]
# df['redox'] = mpr.get_flag('ox/red')

#=============TO QUICKLY FIND ABSOLUTE MIN VOLTAGE(/TIME) VALUE==============
# print(df['Ewe/V'].min())  #'time/s'

#======================TO SET GRID STYLE USING SEABORN=======================
# sns.set_style("whitegrid")

#========================TO SEE SIZE OF NUMPY ARRAY==========================
# print(np_data.shape)

#==================TO MANUALLY SET TICKS RANGE AND SPACING===================
# x_start, x_end = ax.get_xlim()      #; ylims = ax.get_ylim()
# ax.xaxis.set_ticks(np.arange(x_start, x_end, (x_end-x_start)/10))

#======================TO SET POINT COLORS USING CMAP========================
## color is the length of each vector in `points`
#color = np.sqrt((points**2).sum(axis = 1))/np.sqrt(2.0)
#rgb = plt.get_cmap('jet')(color)

#=======================SET DECIMAL PLACES OF TICKERS========================
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

#==================TO ADD A CIRCLE AROUND A SPECIFIED POINT==================
# cir = plt.Circle((point_x, point_y), 0.07, color='r',fill=False)
# ax.set_aspect('equal', adjustable='datalim')
# ax.add_patch(cir)

#====================TO GET THE INDEX OF THE MINIMUM POINT====================
#ind=df.set_index('Ewe/V').index.get_loc(minimum_point)

#===========================TO PRINT FILE NAMES===============================
#print(os.path.basename(eChemFile))