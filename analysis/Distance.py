import BioLogic
import pandas as pd 
import numpy as np 
import glob
import os.path 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from numpy import matlib

'''
Uses the "Distance" method to find nucleation overpotential i.e. finds the point furthest away from a line drawn between the first and last points, equivalent to the "knee" point.
plotGraphCut() and barComparison() functions used to plot results, calculation code found below.
'''


# Created variables to store different paths for easy switching 
NewAcH = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis New\\AcH\\"
NewHCl = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis New\\HCl\\"
NewRef = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis New\\References\\"
Original = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis Original\\"
OriginalTime = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis Original Time\\"


'''Finds all files with file extension .mpr and appends them to a list called mpr_files. The sorted() function arranges them in alphabetical order.'''
mpr_files = sorted(glob.glob(NewHCl + '*.mpr')) 


def plotGraphCut():
    '''
    Plots graphs, cut to show only points of interest around the nucleation overpotential point. 
    The plots draw a vertical dotted red line at the x co-ordinate (time) of the identified point, to identify its position more clearly.
    Use the "Zoom to Rectangle" tool on the output plots to gain a closer look at the values and data points around the nucleation overpotential.
    '''
    fig = plt.figure()
    fig.set_size_inches(14, 6)

    ax = fig.add_subplot(1, 1, 1)   #1x1 grid, 1st subplot

    ax.scatter(np_data[:,3], np_data[:,1], color='black', marker='x', s=2)

    ax.set_xlabel('Time / min').set_style('italic') 
    ax.set_ylabel('$E_{we} / V$').set_style('italic')

    Title = os.path.basename(eChemFile)  
    plt.title(Title.strip('.mpr')).set_weight('bold')

    plt.grid(color=(.8, .8, .8))    #linestyle='-.', linewidth=0.7
    ax.spines['right'].set_color((.8, .8, .8))
    ax.spines['top'].set_color((.8, .8, .8))
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(axis='y', labelcolor='black')
    ax.axhline(y=0, color='black', linewidth=0.5)

    ax.axvline(x=np_data[:,3][idxOfBestPoint], color='red', linewidth=0.5, linestyle='--')

    plt.show()


def barComparison():
    '''
    Plots bar charts comparing the nucleation overpotentials of cells with HCl and AcH pre-treatments. Could probably find a way to automate this but did not have a large data pool to work from, so was easier at the time to manually input values. 
    '''
    fig = plt.figure()
    fig.set_size_inches(10, 6)

    '''Subplot for the HCl treated cells'''
    fig.add_subplot(2, 1, 1)

    plt.subplots_adjust(hspace = 0.4)

    threshold = 0.0
    # above_threshold = np.maximum(values - threshold, 0)
    # below_threshold = np.minimum(values, threshold)

    CuHCl_Voltages = [-0.1373777985572815, -0.4336039125919342, 0.5475689172744751, -0.4431435167789459]
    CuHCl_Treatments = ['2V (Erratic)', '0.1V 0.1mAh', '2V Plating', '2V Plating 2']
    CuHCl_y_pos = np.arange(len(CuHCl_Treatments))

    plt.bar(CuHCl_y_pos, CuHCl_Voltages, width = 0.4, align='center', alpha=0.8)
    plt.xticks(CuHCl_y_pos, CuHCl_Treatments)
    plt.ylabel('Voltage').set_style('italic')
    plt.xlabel('Treatment').set_style('italic')
    plt.title('HCl Treatment').set_weight('bold')
    plt.axhline(y=threshold,linewidth=1, color='black')


    '''Subplot for the AcH treated cells'''
    fig.add_subplot(2, 1, 2)
        
    CuAcH_Voltages = [0.2820037603378296, 0.08628690987825394, -0.05377234145998955, 0.05000302195549011, -0.40689000487327576, -0.3836333453655243]
    CuAcH_Treatments = ['2V 0.1mAh', '1.3V 0.1mAh', '2V 0.01mAh', '2V Plating', '2V 1mAh', '2V 1mAh Plating']
    CuAcH_y_pos = np.arange(len(CuAcH_Treatments))

    plt.bar(CuAcH_y_pos, CuAcH_Voltages, width = 0.4, align='center', alpha=0.8)
    plt.xticks(CuAcH_y_pos, CuAcH_Treatments)
    plt.ylabel('Voltage').set_style('italic')
    plt.xlabel('Treatment').set_style('italic')
    plt.title('AcH Treatment').set_weight('bold')
    plt.axhline(y=threshold,linewidth=1, color='black')

    plt.show()


'''MAIN'''
for i, eChemFile in enumerate(mpr_files):
    '''Read in .mpr files as pandas dataframes, then convert to numpy arrays'''
    mpr = BioLogic.MPRfile(eChemFile)
    df = pd.DataFrame(mpr.data)
    df = df.loc[:, df.columns.intersection(['time/s', 'Ewe/V'])]
    df['time/hr'] = df['time/s']/3600
    df['time/min'] = df['time/s']/60
    np_data = df.to_numpy()
    
    '''Identify point at which to 'cut' the graph, to 'zoom in' on points of interest, around nucleation overpotential.'''
    der_y = np.gradient(np_data[:,1], np_data[:,3])     
    
    for n in der_y:
        der_y = der_y[(der_y > -20)]

    cut = list(range(0, (len(np_data)-len(der_y)+1)))
    np_data_cut = np_data[(len(np_data)-len(der_y)):]

    ''' Calculate 'knee' point using the distance method.'''
    nPoints = len(np_data_cut[:,1])
    allCoord = np.vstack((range(nPoints), np_data_cut[:,1])).T
    np.array([range(nPoints), np_data_cut[:,1]])
    firstPoint = allCoord[0]
    lineVec = allCoord[-1] - allCoord[0]
    lineVecNorm = lineVec / np.sqrt(np.sum(lineVec**2))
    vecFromFirst = allCoord - firstPoint
    scalarProduct = np.sum(vecFromFirst * np.matlib.repmat(lineVecNorm, nPoints, 1), axis=1)
    vecFromFirstParallel = np.outer(scalarProduct, lineVecNorm)
    vecToLine = vecFromFirst - vecFromFirstParallel
    distToLine = np.sqrt(np.sum(vecToLine ** 2, axis=1))
    idxOfBestPoint = np.argmax(distToLine)  #Returns index of the nucleation overpotential point within the numpy array

    '''Print the time and potential at the nucleation overpotential point.'''
    print("\n \n" + os.path.basename(eChemFile))
    print("Time at nucleation overpotential:", np_data[:,0][idxOfBestPoint]/60, "min")
    print("Nucleation overpotential:", np_data[:,1][idxOfBestPoint], "V")

    '''Calls the plotting function. Comment this out to avoid viewing plots every time.'''
    plotGraphCut()

    '''Change number to restrict number file plots displayed when run.'''
    # if i + 1 == 10:
    #     break

'''Calls the bar comparison function. Comment this out to avoid viewing the comparison chart.'''
barComparison()