#!/bin/python3
#import built-in modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#assign variable to read excel files
gpr16 = pd.read_excel("2016_GPR.xlsx")
gpr18 = pd.read_excel("2018_GPR.xlsx")
gpr20 = pd.read_excel("2020_GPR.xlsx")

#convert excel files into DataFrame
df16 = pd.DataFrame(gpr16)
df18 = pd.DataFrame(gpr18)
df20 = pd.DataFrame(gpr20)

#Drop all columns not related to OVERTIME
cln1 = df16.drop(columns=['GRADE', 'ANNUAL1', 'HOURLY1', 'ANNUAL2', 'HOURLY2', 'ANNUAL3', 'HOURLY3', 'ANNUAL4', 'HOURLY4', 'ANNUAL5', 'HOURLY5', 'ANNUAL6', 'HOURLY6', 'ANNUAL7', 'HOURLY7', 'ANNUAL8', 'HOURLY8', 'ANNUAL9', 'HOURLY9', 'ANNUAL10', 'HOURLY10'])
cln2 = df18.drop(columns=['GRADE', 'ANNUAL1', 'HOURLY1', 'ANNUAL2', 'HOURLY2', 'ANNUAL3', 'HOURLY3', 'ANNUAL4', 'HOURLY4', 'ANNUAL5', 'HOURLY5', 'ANNUAL6', 'HOURLY6', 'ANNUAL7', 'HOURLY7', 'ANNUAL8', 'HOURLY8', 'ANNUAL9', 'HOURLY9', 'ANNUAL10', 'HOURLY10'])
cln3 = df20.drop(columns=['GRADE', 'ANNUAL1', 'HOURLY1', 'ANNUAL2', 'HOURLY2', 'ANNUAL3', 'HOURLY3', 'ANNUAL4', 'HOURLY4', 'ANNUAL5', 'HOURLY5', 'ANNUAL6', 'HOURLY6', 'ANNUAL7', 'HOURLY7', 'ANNUAL8', 'HOURLY8', 'ANNUAL9', 'HOURLY9', 'ANNUAL10', 'HOURLY10'])

#Get the cumulative sum of OVERTIME columns#
otsum1 = cln1[['OVERTIME1','OVERTIME2','OVERTIME3','OVERTIME4','OVERTIME5','OVERTIME6','OVERTIME7','OVERTIME8','OVERTIME9','OVERTIME10']].cumsum()
otsum2 = cln2[['OVERTIME1','OVERTIME2','OVERTIME3','OVERTIME4','OVERTIME5','OVERTIME6','OVERTIME7','OVERTIME8','OVERTIME9','OVERTIME10']].cumsum()
otsum3 = cln3[['OVERTIME1','OVERTIME2','OVERTIME3','OVERTIME4','OVERTIME5','OVERTIME6','OVERTIME7','OVERTIME8','OVERTIME9','OVERTIME10']].cumsum()

#Get the maximum value from each overtime column
otmax1 = otsum1.max()
otmax2 = otsum2.max()
otmax3 = otsum3.max()

#Get the sum of all maximum values of overtime columns
otmaxsum1 = otmax1.sum()
otmaxsum2 = otmax2.sum()
otmaxsum3 = otmax3.sum()

OT16 = otmax1.astype(int)
OT18 = otmax2.astype(int)
OT20 = otmax3.astype(int)
#2016 = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#2018 = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#2020 = ['Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#np2016 = np.array(2016)
#np2018 = np.array(2018)
#np2020 = np.array(2020)

x = np.linspace(23000, 32000, 10)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.

ax.plot(x, OT16, label='2016')  # Plot more data on the axes...
ax.plot(x, OT18, label='2018')  # ... and some more.
ax.plot(x, OT20, label='2020')  # ... and some more.

ax.set_xlabel('Years')  # Add an x-label to the axes.
ax.set_ylabel('Total Gov Overtime 2016-2020')  # Add a y-label to the axes.
ax.set_title("GPR Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.

plt.hist(OT16, bins = 10)
plt.show()

#Print out only the maximum values for the years 2016, 2018, 2020
#ot2016 = otmaxsum1.astype(int)
#ot2018 = otmaxsum2.astype(int)
#ot2020 = otmaxsum3.astype(int)

#print('\n')
#print(ot2016 + ot2018 + ot2020)

