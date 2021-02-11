# Plotting all initial results next to each other 

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from numpy import matlib

fig = plt.figure()
fig.set_size_inches(6, 6)
fig.add_subplot(1, 1, 1)

#plt.subplots_adjust(hspace = 0.4)

Voltages = [-0.813540518283844, -0.6889398694038391, -0.5106261968612671, -0.4431435167789459, -0.5769994854927063, -0.5840930938720703, -0.993, -0.6766124963760376, -0.40689000487327576, -0.3836333453655243, -0.0816, -0.0552, -0.0744]
Treatments = ['HCl 1', 'HCl 8', 'HCl 9', 'HCl 10', 'AcH 2', 'AcH 3', 'AcH 4', 'AcH 5', 'AcH 6', 'AcH 7', 'CuC 1', 'CuC 2', 'CuC 3']

for i in Treatments:
    if 'HCl' in Treatments[i]:
        plt.bar(y_pos, Voltages, width = 0.4, align='center', alpha=0.8, color='red')
    elif 'AcH' in Treatments[i]:
        plt.bar(y_pos, Voltages, width = 0.4, align='center', alpha=0.8)
    elif 'CuC' in Treatments[i]:
        plt.bar(y_pos, Voltages, width = 0.4, align='center', alpha=0.8, color='green')
    else:
        pass

y_pos = np.arange(len(Treatments))

#plt.bar(y_pos, Voltages, width = 0.4, align='center', alpha=0.8)
plt.xticks(y_pos, Treatments)
plt.ylabel('Voltage').set_style('italic')
plt.xlabel('Treatment').set_style('italic')
plt.title('All Treatments').set_weight('bold')

CuAcH_Treatments = ['2V 0.1mAh', '1.3V 0.1mAh', '2V 0.01mAh', '2V Plating', '2V 1mAh', '2V 1mAh Plating']

plt.show()
