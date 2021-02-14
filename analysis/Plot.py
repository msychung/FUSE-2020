import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from numpy import matlib

'''Plotting bar charts of all nucleation overpotential results for HCl, AcH and CuC treatments next to each other. Passed in results manually due to small data pool.'''

fig = plt.figure()
fig.set_size_inches(10, 6)
fig.add_subplot(1, 1, 1)

#plt.subplots_adjust(hspace = 0.4)

Voltages = [-0.813540518283844, -0.6889398694038391, -0.5106261968612671, -0.4431435167789459, -0.5769994854927063, -0.5840930938720703, -0.993, -0.6766124963760376, -0.40689000487327576, -0.3836333453655243, -0.0816, -0.0552, -0.0744]
Treatments = ['HCl 1', 'HCl 8', 'HCl 9', 'HCl 10', 'AcH 2', 'AcH 3', 'AcH 4', 'AcH 5', 'AcH 6', 'AcH 7', 'CuC 1', 'CuC 2', 'CuC 3']
CuAcH_Treatments = ['2V 0.1mAh', '1.3V 0.1mAh', '2V 0.01mAh', '2V Plating', '2V 1mAh', '2V 1mAh Plating']

y_pos = np.arange(len(Treatments))

colours = []
for i in Treatments:
    if 'HCl' in i:
        colours.append('red')
    elif 'AcH' in i:
        colours.append('green')
    elif 'CuC' in i:
        colours.append('blue')
    else:
        pass

plt.bar(y_pos, Voltages, width = 0.4, align='center', alpha=0.8, color = colours)

plt.xticks(y_pos, Treatments)
plt.ylabel('Voltage').set_style('italic')
plt.xlabel('Treatment').set_style('italic')
plt.title('All Treatments').set_weight('bold')

plt.show()