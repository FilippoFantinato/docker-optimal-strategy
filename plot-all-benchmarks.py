import csv
import sys

import matplotlib.pyplot as plt 
import csv 

lines=20

x1 = [] 
y1 = []
  
with open("./results/both/both-first.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    i=0
    for row in plots:
        if i == lines: break;
        i = i + 1
        x1.append(float(row[0])) 
        y1.append(float(row[1])) 

x2 = [] 
y2 = []

with open("./results/both/both-second.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    i=0
    for row in plots:
        if i == lines: break;
        i = i + 1
        x2.append(float(row[0])) 
        y2.append(float(row[1])) 

x3 = [] 
y3 = []

with open("./results/both/both-third.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    i=0
    for row in plots:
        if i == lines: break;
        i = i + 1
        x3.append(float(row[0])) 
        y3.append(float(row[1])) 

x4 = [] 
y4 = []

with open("./results/co-safety/co-safety-first.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    i=0
    for row in plots:
        if i == lines: break;
        i = i + 1
        x4.append(float(row[0])) 
        y4.append(float(row[1])) 

x5 = [] 
y5 = []

with open("./results/co-safety/co-safety-second.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    i=0
    for row in plots:
        if i == lines: break;
        i = i + 1
        x5.append(float(row[0])) 
        y5.append(float(row[1])) 

x6 = [] 
y6 = []

with open("./results/co-safety/co-safety-third.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    i=0
    for row in plots:
        if i == lines: break;
        i = i + 1
        x6.append(float(row[0])) 
        y6.append(float(row[1])) 

x7 = [] 
y7 = []

with open("./results/driver/driver-finally.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    i=0
    for row in plots:
        if i == lines: break;
        i = i + 1
        x7.append(float(row[0])) 
        y7.append(float(row[1])) 

x8 = [] 
y8 = []

with open("./results/driver/driver-until.csv",'r') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
    next(plots, None)
    i=0
    for row in plots:
        if i == lines: break;
        i = i + 1
        x8.append(float(row[0])) 
        y8.append(float(row[1])) 

plt.plot(x7, y7, color = 'blue') 
plt.plot(x8, y8, color = 'green')
plt.plot(x1, y1, color = 'yellow') 
plt.plot(x2, y2, color = 'orange')
plt.plot(x3, y3, color = 'red')
plt.plot(x4, y4, color = 'pink') 
plt.plot(x5, y5, color = 'black')
plt.plot(x6, y6, color = 'violet')
plt.yscale('log')
plt.legend([
    '(3)', 
    '(4)', 
    '(5)', 
    '(6)', 
    '(7)', 
    '(8)', 
    '(9)', 
    '(10)'
])
plt.xlabel('n') 
plt.ylabel('Running time (ms)') 
plt.show()
