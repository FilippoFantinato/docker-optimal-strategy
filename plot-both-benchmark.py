import csv
import sys

import matplotlib.pyplot as plt 
import csv 
  
x1 = [] 
y1 = []
  
with open("./both-first.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    for row in plots: 
        x1.append(float(row[0])) 
        y1.append(float(row[1])) 

x2 = [] 
y2 = []

with open("./both-second.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    for row in plots: 
        x2.append(float(row[0])) 
        y2.append(float(row[1])) 

x3 = [] 
y3 = []

with open("./both-third.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    for row in plots: 
        x3.append(float(row[0])) 
        y3.append(float(row[1])) 

plt.plot(x1, y1, color = 'b') 
plt.plot(x2, y2, color = 'g')
plt.plot(x3, y3, color = 'r')
plt.yscale('log')
plt.legend(['First formula', 'Second formula', 'Third formula'])
plt.title("First benchmark")
plt.xlabel('Number of states (n)') 
plt.ylabel('Running time(ms)') 
plt.show()
