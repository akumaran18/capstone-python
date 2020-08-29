#!/usr/bin/env python
# coding: utf-8

# In[7]:


# grab-stations.py extracts a list of weather stations and their coordinates for Illinois from nws.noaa.gov
# and outputs it to a file named stations.txt
# Program written by Amrutha and Maura

# Import library that allows DOM navigation
from lxml import html
# Import requests and sys libraries
import requests
import sys

page = requests.get('https://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml')
extractedHTML = html.fromstring(page.content)

# Pull context exclusively from html tag indicated
ilStations = extractedHTML.xpath('/html/body/table[4]/tr/td[3]/table[2]/tr[48]/td')
stationData = ilStations[0].text_content()


# The following creates lists containing the name of the weather stations, and their coordinates
name=[]
lat=[]
long=[]

# Stands for total length of the stationData text
tlength=len(stationData)

# These are the index numbers for the first station's name (72-76), latitude (103-108), and longitude (113-118)
a=72
b=76
c=103
d=108
e=113
f=118


# Originally, a string with empty spaces used to be appended to the end of of the name, lat, and long arrays
# This new condition gets rid of the empty string at the end of the arrays
# As long as the station name doesn't return 4 blank spaces, this while loop will run and append each name, lat, and long
# to their respective arrays
while stationData[a:b] != '    ': 
    name.append(stationData[a:b])
    lat.append(stationData[c:d])
    long.append(stationData[e:f])
    a=a+53
    b=b+53
    c=c+53
    d=d+53
    e=e+53
    f=f+53

# Eliminate all print statements because they all get stored in sys.stdout which we don't want
#print (name)
#print (lat)
#print (long)

# Add + / - to coordinates
x=0
while x <= (len(name)-1): # Instead of using the integer 51 for the 51 stations, this is adaptable to any amount of stations
    # Add the + and - to the lat and long strings
    lat[x]='+'+ lat[x]
    long[x]='-'+ long[x]
    # Increment x to perform same operation on every station's lat and long
    x=x+1

# Send data to standard output or stdout to write into stations.txt file
x=0
while x <= (len(name)-1): # Instead of using the integer 51 for the 51 stations, this is adaptable to any amount of stations
    # The print function or sys.stdout.write may be used to send this information to standard output
    # which will then be stored in the stations.txt file through the command-line in Git-Bash
    print(name[x],long[x],lat[x])
    x=x+1


# In[ ]:




