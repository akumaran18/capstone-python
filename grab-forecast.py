#!/usr/bin/env python
# coding: utf-8

# In[8]:


# The purpose of this program is to copy temperature data for all the weather stations in Illinois
# into a file from the NOAA website
# Program written by Maura and Amrutha and Emilio

#import data from website
import requests
# Import library sys
import sys

r=requests.get('http://nws.noaa.gov/mdl/gfslamp/bull/lavlamp.txt')
# print(r.text)

# Declare / assign variables
name=[]
lat=[]
long=[]
temp=[]
a=0
c=0
x=0
tlength=len(r.text)

# Eliminate all print statements because they all get stored in sys.stdout which we don't want
#print('c before the for loop:', c)

# Open stations.txt and read data into variables
#file=open('stations.txt','r')
for line in sys.stdin:
    elems = line.split()
    name.append(elems[0]) #station name
    long.append(elems[1])
    lat.append(elems[2])
    #c=c+1
#file.close()

# Eliminate all print statements because they all get stored in sys.stdout which we don't want
#print('Length of name array:', len(name))

#c=c-1

c=len(name)-1

# Find the temperature data for each weather station
while a <= c:
    x=r.text.find(name[a])
    t=r.text.find('TMP',x,tlength) 
    temp.append(r.text[t+5:t+8])
    # Eliminate all print statement because they all get stored in sys.stdout which we don't wan
    #print(name[a], ' ',long[a],' ',lat[a], ' ',temp[a])
    a=a+1

# Check for missing temperature data and delete station info if temperature is missing
a=0
while a <= c:
    if (temp[a] == '   '):
#        print ('Its a GREAT day!')
        del name[a]
        del long[a]
        del lat[a]
        del temp[a]
        c=c-1
    a=a+1
    
# Create the forecast.txt file
x=0
#file=open('forecast.txt','w+')
while x <= c:
    sys.stdout.write(name[x])
    sys.stdout.write(' ')
    sys.stdout.write(long[x])
    sys.stdout.write(' ')
    sys.stdout.write(lat[x])
    sys.stdout.write(' ')
    sys.stdout.write(temp[x])
    sys.stdout.write('\n')
    
    #file.write(name[x])
    #file.write(' ')
    #file.write(long[x])
    #file.write(' ')
    #file.write(lat[x])
    #file.write(' ')
    #file.write(temp[x])
    #file.write('\n')
    x=x+1
#file.close()

# Eliminate all print statements because they all get stored in sys.stdout which we don't want
#print(' ')
#print('The forecast.txt file has been created for the state of Illinois from nws.noaa.gov')

#print('END')


# In[ ]:




