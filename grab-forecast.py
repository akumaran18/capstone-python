#!/usr/bin/env python
# coding: utf-8

# In[55]:


# grab-forecast.py copies temperature data for all the weather stations in Illinois using input from stations.txt
# and outputs the temperature data to a file called forecast.txt
# Program written by Amrutha and Maura

# Import the requests and sys libraries
import requests
import sys

# Use requests to pull the text content from a text file on the remote website
r=requests.get('http://nws.noaa.gov/mdl/gfslamp/bull/lavlamp.txt')

# Declare/assign variables
name=[]
lat=[]
long=[]
temp=[]

# Stands for total length of the text found in lavlamp.txt on the NOAA site
tlength=len(r.text)

# grab-forecast.py will run with stations.txt as input in Git-Bash. Each line of input will be split up by white space as 
# indexed elements in an array named 'elems.' The for-loop appends each element to the right array before moving to the
# next line of input

file=open('stations.txt','r')
#for line in sys.stdin:
for line in file:
    elems = line.split()
    name.append(elems[0]) # appended to station name array
    long.append(elems[1]) # appended to station long array
    lat.append(elems[2]) # appended to station lat array
file.close()

c=len(name)-1 # c is the highest index number of the station name/lat/long arrays

a=0
# Find the temperature data for each weather station
while a <= c:
    x=r.text.find(name[a]) # Find index number of first char of station name within 'r.text' array
    t=r.text.find('TMP',x,tlength) # Find index num of first char of the first 'TMP' string found after station name 
    temp.append(r.text[t+5:t+8]) # Once t is known, counts upwards to grab most current temp
    a=a+1 # Increments up for next station
    
# Check for missing temperature data and delete station info if temperature is missing
a=0
while a <= c: # While a is <= the highest index number of the name/lat/long arrays
    if (temp[a] == '   '):
        del name[a]
        del long[a]
        del lat[a]
        del temp[a]
        c=c-1
    a=a+1
    
# Write data to forecast.txt file
a=0
while a <= (len(name)-1):
    # The print function or sys.stdout.write may be used to send this information to standard output
    # which will then be stored in the forecast.txt file through the command-line in Git-Bash
    print(name[a],long[a],lat[a],temp[a])
    a=a+1


# In[ ]:




