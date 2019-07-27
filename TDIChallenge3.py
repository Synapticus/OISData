# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:07:54 2019

@author: Sean
"""


import csv
import numpy as np
import matplotlib as mpl

with open('ViceNews_FullOISData - Sheet1.csv', newline='', encoding='utf-8') as csvfile:
    SheetReader = csv.DictReader(csvfile)    
    ArmedAndAlive = 0
    ArmedAndKilled = 0
    UnarmedAndAlive = 0
    UnarmedAndKilled = 0
    KilledByYear = dict()
    NonfatallyShotByYear = dict()
    for row in SheetReader:
        #Figure 1: Are you likelier to be fatally shot if armed?
        if row['SubjectArmed'] == 'Y':
            if row['Fatal'] == 'F':
                ArmedAndKilled += 1
            else:
                ArmedAndAlive += 1
        if row['SubjectArmed'] == 'N':
            if row['Fatal'] == 'N':
                UnarmedAndKilled += 1
            else:
                UnarmedAndAlive += 1
                
        fullDate = row['Date']  
        fullDate.strip()
        if len(fullDate) == 4:
            year = int(fullDate)
        elif '/' in fullDate:               
            tempYear = fullDate[fullDate.rfind('/')+1:]
            if len(tempYear) == 2:
                year = int('20'+tempYear)
            else:
                year = int(tempYear)    
        elif '-' in fullDate:
            year = int(fullDate[0:4])
        else:
            continue
                                           
        if row['Fatal'] == 'F':
            if year in KilledByYear:
                KilledByYear[year] += 1
            else:
                KilledByYear[year] = 1    
        else:
           if year in NonfatallyShotByYear:
               NonfatallyShotByYear[year] += 1
           else:
               NonfatallyShotByYear[year] = 1
                
                
mpl_fig1 = mpl.pyplot.figure()
ax = mpl_fig1.add_subplot(111)                
label = ['Armed,Fatally shot','Armed,Alive','Unarmed,Fatally shot','Unarmed,Alive']                
p1 = ax.bar(np.arange(2),[ArmedAndKilled,UnarmedAndKilled],0.5,color=(0,0,0))
p2 = ax.bar(np.arange(2),[ArmedAndAlive,UnarmedAndAlive],0.5,color=(0.5,0.5,0.5),bottom=[ArmedAndKilled,UnarmedAndKilled])
ax.set_ylabel('Subjects')
ax.set_xlabel('Status')
ax.set_title('Unarmed subjects are likelier to be fatally shot')       
ax.set_xticks([0,1])
ax.set_xticklabels(('Armed','Unarmed'))   
ax.legend(['Fatally shot','Survived'])

mpl_fig2 = mpl.pyplot.figure()

x = np.zeros(7)
y1 = np.zeros(7)
y2 = np.zeros(7)
i = 0
for year in range(2010,2017):
    x[i] = int(year)
    y1[i] = KilledByYear[int(year)]
    y2[i] = NonfatallyShotByYear[int(year)]
    i = i+1
    
ax = mpl_fig2.add_subplot(111)
p1 = ax.plot(x,y1)
p2 = ax.plot(x,y2)  
ax.set_ylabel('Shootings')
ax.set_xlabel('Year')
ax.set_title('Survival of officer-involved shootings has declined annually')
ax.legend(['Fatally shot','Survived'])