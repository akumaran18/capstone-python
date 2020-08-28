#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Extract a list of weather stations and their coordinates for Illinois from nws.noaa.gov
# Program written by Maura and Amrutha and Emilio

from lxml import html
import requests
# Import library sys
import sys

page = requests.get('https://www.nws.noaa.gov/mdl/gfslamp/docs/stations_info.shtml')
extractedHTML = html.fromstring(page.content)


ilStations = extractedHTML.xpath('/html/body/table[4]/tr/td[3]/table[2]/tr[48]/td')
stationData = ilStations[0].text_content()
# Eliminate all print statements because they all get stored in sys.stdout which we don't want
#print (stationData)

# The following creates lists containing the name of the weather stations, and their coordinates
name=[]
lat=[]
long=[]
# Stands for total length
tlength=len(stationData)
# Eliminate all print statements because they all get stored in sys.stdout which we don't want
#print (tlength)
a=72
b=76
c=103 # USED TO BE 102
d=108
e=113
f=118


# Notice originally that a string with empty spaces used to be appended to the end of of the name, lat, and long arrays
# This new condition gets rid of the empty string at the end of the arrays
# As long as the station name doesn't return 4 blank spaces, this while loop will run
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
while x <= (len(name)-1): # Instead of using the integer 51, this version is fool-proof against new stations added to list
    # Increment x up by 1 before performing operations again
    lat[x]='+'+ lat[x]
    #lat[x]=lat[x].replace(' ','') This line of code is not needed
    long[x]='-'+ long[x]
    # Eliminate all prints statement because they all get stored in sys.stdout which we don't want
    #print(name[x],' ',long[x],' ',lat[x])
    x=x+1

# Write data to stations.txt file

x=0
#file=open('stations.txt','w+')
#for line in sys.stdout:
while x <= (len(name)-1): # Instead of using the integer 51, this version is fool-proof against new stations added to list
    sys.stdout.write(name[x])
    sys.stdout.write(' ')
    sys.stdout.write(long[x])
    sys.stdout.write(' ')
    sys.stdout.write(lat[x])
    sys.stdout.write('\n')
        
    #file.write(name[x])
    #file.write(' ')
    #file.write(long[x])
    #file.write(' ')
    #file.write(lat[x])
    #file.write('\n')
    x=x+1
#file.close()

# Eliminate all prints statement because they all get stored in sys.stdout which we don't want
#print(' ')
#print('The stations.txt file has been created for the state of Illinois from nws.noaa.gov')


# In[ ]:




