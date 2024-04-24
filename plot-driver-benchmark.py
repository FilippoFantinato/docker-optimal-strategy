import csv
import sys

import matplotlib.pyplot as plt 
import csv 
  
x1 = [] 
y1 = []
  
with open("./driver-finally.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    for row in plots: 
        x1.append(float(row[0])) 
        y1.append(float(row[1])) 

x2 = [] 
y2 = []

with open("./driver-until.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    for row in plots: 
        x2.append(float(row[0])) 
        y2.append(float(row[1])) 

plt.plot(x1, y1, color = 'b') 
plt.plot(x2, y2, color = 'g')
plt.yscale('log')

plt.legend(['First formula (finally)', 'Second formula (until)'])
plt.title("Driver example")
plt.xlabel('Number of states (n)') 
plt.ylabel('Running time(ms)') 
plt.show()
