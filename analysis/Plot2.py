import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from numpy import matlib
import pandas as pd

'''
Plotting scatter graphs of nucleation overpotential vs. current at constant voltage hold end, grouped by time held at constant voltage. 
Passed in results manually due to small data pool.
'''

fig = plt.figure()
fig.set_size_inches(10, 6)
fig.add_subplot(1, 1, 1)

# plt.subplots_adjust(hspace = 0.4)

'''List results based on identified grouped trends (to allow easier colouring of groups)'''
Voltages1 = [-0.40689000487327500, -0.38363334536552400, -0.51062619686126700, -0.44314351677894500]
Currents1 = [-0.075, -0.116, -0.033, -0.060]
Time1 = [24.00559746, 9.616464154, 69.78085042, 13.26404527]

Voltages2 = [-0.57699948549270600, -0.993000000000000000, -0.67661249637603700]
Currents2 = [-0.126, -0.025, -0.077]
Time2 = [23.38176994, 77.98236238, 20.28648312]

Voltages3 = [-0.40689000487327500, -0.38363334536552400,  -0.44314351677894500, -0.57699948549270600, -0.67661249637603700]
Currents3 = [-0.075, -0.116, -0.060, -0.126, -0.077]
Time3 = [24.00559746, 9.616464154,  13.26404527, 23.38176994, 20.28648312]

Voltages4 = [-0.51062619686126700, -0.993000000000000000]
Currents4 = [-0.033, -0.025]
Time4= [69.78085042, 77.98236238]

'''Comment out one of these sets to view the other'''
plt.scatter(Voltages1, Currents1, s=12, c='#3BA9C6', marker='D')
plt.scatter(Voltages2, Currents2, s=12, c='#FDB515', marker='D')

plt.scatter(Voltages3, Currents3, s=18, c='#3BA9C6', marker='D')
plt.scatter(Voltages4, Currents4, s=18, c='#B41E8E', marker='D')

'''Draws straight line trendlines through the data - ended up not being very useful, since trends were more exponential than linear.'''
# data = {'Voltages': [-0.57699948549270600, -0.993000000000000000, -0.67661249637603700, -0.40689000487327500, -0.38363334536552400, -0.51062619686126700, -0.44314351677894500],
#         'Currents': [-0.126, -0.025, -0.077, -0.075, -0.116, -0.033, -0.060],
#         'Time': [23.38176994, 77.98236238, 20.28648312, 24.00559746, 9.616464154, 69.78085042, 13.26404527]}

# df = pd.DataFrame(data, columns = ['Voltages', 'Currents'])

# z = np.polyfit(x=df['Voltages'], y=df['Currents'], deg=1)
# p = np.poly1d(z)
# df['trendline'] = p(df['Voltages'])

# ax = df.plot.scatter(x='Voltages', y='Currents')
# df.set_index('Voltages', inplace=True)
# df.trendline.sort_index(ascending=False).plot(ax=ax)

plt.ylabel('Current at Constant Voltage End ($\mu$A)').set_style('italic')
plt.xlabel('Nucleation Overpotential (V)').set_style('italic')
plt.title('Current at CV End vs. Nucleation Overpotential').set_weight('bold')
plt.gca().invert_xaxis(), plt.gca().invert_yaxis()

plt.show()