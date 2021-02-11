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

class Analysis():
    '''
    This class contains the constructor, and 3 functions to plot Voltage vs Time, along with its first and second derivatives.

    Note that the second derivative is usually masked by the first derivative plot, so is not seen when all 3 are plotted together.

    der_y note: derivative will be computed using central differences and will have the same length as y, unlike numpy.diff, which uses forward differences and will return an (n-1) size vector.
    '''

    def __init__(self, name, data_array):
        '''
        Initialises fig, ax and derp to produce plots
        Initialises der_y and der_x to set x and y derivatives 
        Takes in name and data_array as arguments, belonging to each object (representing a file)
        '''
        self.name = name
        self.data_array = data_array
        self.fig = plt.figure()
        self.ax = ax = self.fig.add_subplot(1, 1, 1)    #1x1 grid, 1st subplot
        self.derp = self.ax.twinx()
        self.der_y = np.gradient(self.data_array[:,1], self.data_array[:,3])      
        self.der_x = self.data_array[:,3]


    def plotGraph(self):
        '''
        Plots voltage against time.
        '''
        self.fig.set_size_inches(14, 6) 

        self.ax.scatter(self.data_array[:,3], self.data_array[:,1], color='black', marker='x', s=2)

        self.ax.set_xlabel('Time / min').set_style('italic')
        self.ax.set_ylabel('$E_{we} / V$').set_style('italic')

        plt.title(self.name.strip('.mpr')).set_weight('bold')

        plt.grid(color=(.8, .8, .8))    #linestyle='-.', linewidth=0.7
        self.ax.spines['right'].set_color((.8, .8, .8))
        self.ax.spines['top'].set_color((.8, .8, .8))
        self.ax.xaxis.set_ticks_position('bottom')
        self.ax.yaxis.set_ticks_position('left')
        self.ax.tick_params(axis='y', labelcolor='black')
        self.ax.axhline(y=0, color='red', linewidth=0.5)

        '''Plots first and second derivatives on same plot as original V-t graph.'''
        self.plotDer()      #Comment this out to see second derivative plot more clearly
        self.plotDer2()

        plt.show()


    def plotDer(self):
        '''
        Plots the first derivative of voltage against time.
        '''

        # self.der_y = diff(np_data[:,1]) / diff(np_data[:,3])   #has length n-1 since you can only start computing differences from 1st index
        # self.der_x = (np.data(np_data[:,3])[:-1] + np.data(np_data[:,3])[1:]) / 2

        self.derp.scatter(self.der_x, self.der_y, color='blue', marker='^', s=1)
        self.derp.set_ylabel('Derivative').set_style('italic')
        self.derp.tick_params(axis='y', labelcolor='blue')

        plt.show()


    def plotDer2(self):
        '''
        Plots the second derivative of voltage against time.
        '''
        # der_y2 = diff(self.der_y)/diff(self.der_x)
        # der_x2 = self.der_x[:-1]

        # myList = np_data[:,3].tolist()
        # der_y2 = [myList[n+1] + myList[n-1] - 2 * myList[n] for n in range(len(myList)-1)]
        # der_y2 = np.append(der_y2, [1])

        der_y2 = np.gradient(self.der_y, self.data_array[:,3])
        der_x2 = self.data_array[:,3]   # = self.der_x

        #derp2 = ax.twinx()
        self.derp.scatter(der_x2, der_y2, color='green', marker='d', s=2, alpha=0.4)

        plt.show()

        #derp2.tick_params(axis='y', labelcolor='green')

        #Knee/Elbow point should be the point with max. absolute second derivative


analysisNew = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis New\\"
analysisOriginal = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis Original\\"
analysisOriginalTime = "C:\\Users\\Melissa\\OneDrive - Lancaster University\\Jobs & Internships\\FUSE 2020\\Data Analysis\\Analysis\\Analysis Original Time\\"

'''Finds all files with file extension .mpr and appends them to a list called mpr_files. The sorted() function arranges them in alphabetical order.'''
mpr_files = sorted(glob.glob(analysisOriginal + '*.mpr')) 
#print('\n'.join(mpr_files))


def main(fileObject):
    '''
    main(fileObject) does the following:
    - loops through each file in the list of files (mpr_files)
    - converts the relevant data to a numpy array
    - creates an object for the file, with name and data atrributes

    `for i, eChemFile in enumerate(mpr_files):`  if too many files, then below there is an `if i == x` condition to limit number of output results
    '''
    
    for i, eChemFile in enumerate(mpr_files):   
        
        mpr = BioLogic.MPRfile(eChemFile)
        df = pd.DataFrame(mpr.data)
        df = df.loc[:, df.columns.intersection(['time/s','Ewe/V'])]     # gets rid of irrelevant data
        df['time/hr'] = df['time/s']/3600
        df['time/min'] = df['time/s']/60
        np_data = df.to_numpy()         # 0: time/s | 1: Ewe/V | 2: time/hr | 3: time/min

        # print(df['time/hr'].iloc[-1])

        file_name = os.path.basename(eChemFile)   

        fileObject.append(Analysis(file_name, np_data))     # append an object containing file name and file data to the fileObject[] list
        
        '''Calls the plotGraph() function for each object. Produces a single plot containing original, first and second derivatives.'''
        fileObject[i].plotGraph()
        
        '''Limits the number of output results if folder contains too many files (I forgot CTRL+C exists...)'''
        # if i+1 == 15:
        #     break


fileObject = []    # contains a list of all file objects (representing the mpr files)
main(fileObject)    # runs main()


'''prints the first 2 attributes of the first file Object.'''
# print(fileObject[0].name, fileObject[0].data_array)





'''=====================CLEANS UP COLUMNS APPARENTLY=========================='''
# def sanitize_labels(label):
#     return label.split('/')[0].lower().lstrip('-').translate(dict.fromkeys(map(ord, " ,|()-"),'_')).rstrip('_')

# df.columns = [sanitize_labels(label) for label in df.columns]
# df['redox'] = mpr.get_flag('ox/red')

'''=============TO QUICKLY FIND ABSOLUTE MIN VOLTAGE(/TIME) VALUE=============='''
# print(df['Ewe/V'].min())  #'time/s'

'''======================TO SET GRID STYLE USING SEABORN======================='''
# sns.set_style("whitegrid")

'''========================TO SEE SIZE OF NUMPY ARRAY=========================='''
# print(np_data.shape)

'''==================TO MANUALLY SET TICKS RANGE AND SPACING==================='''
# x_start, x_end = ax.get_xlim()      #; ylims = ax.get_ylim()
# ax.xaxis.set_ticks(np.arange(x_start, x_end, (x_end-x_start)/10))

'''======================TO SET POINT COLORS USING CMAP========================'''
## color is the length of each vector in `points`
#color = np.sqrt((points**2).sum(axis = 1))/np.sqrt(2.0)
#rgb = plt.get_cmap('jet')(color)

'''=======================SET DECIMAL PLACES OF TICKERS========================'''
#ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.2f'))

'''==================TO ADD A CIRCLE AROUND A SPECIFIED POINT=================='''
# cir = plt.Circle((point_x, point_y), 0.07, color='r',fill=False)
# ax.set_aspect('equal', adjustable='datalim')
# ax.add_patch(cir)

'''====================TO GET THE INDEX OF THE MINIMUM POINT===================='''
#ind=df.set_index('Ewe/V').index.get_loc(minimum_point)

'''===========================TO PRINT FILE NAMES==============================='''
#print(os.path.basename(eChemFile))