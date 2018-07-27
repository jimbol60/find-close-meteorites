# -*- coding: utf-8 -*-
"""
Nasa data

Created on Fri Jun 15 14:17:09 2018

@author: Jim
"""

import requests
import math

# https://nasasearch.nasa.gov/search?query=meteors&affilliate=nasa&utf8=check

meteor_resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
#print(meteor_resp.status_code)
#print(meteor_resp.text)
print(meteor_resp.json())
"""
Returns dictionary with imbeded string
in the following columns
name   	
id   	
nametype   	
recclass   	
mass (g)   	
fall   	
year   	
reclat   	
reclong   	
GeoLocation

The dictionary keys are
fall:, geolocation:, id:, mass:, name:, nametype:, recclass:,
reclat:, reclong:, year:
    
"""
meteor_data = meteor_resp.json()
#print(type(meteor_data))  = a list

for meteor in meteor_data: 
    print(type(meteor))

#haversine.py formula
def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat1 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    h = math.sin( (lat2 - lat1) / 2)**2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin( (lon2 - lon1) / 2)**2
      
    return 6372.8 * 2 * math.asin(math.sqrt(h))

#calc_dist(50.775000, 6.083330, 40.114955, -111.654923)
    
my_loc = (40.233845, -111.658531)

#float(meteor_data[0]['reclat'])

for meteor in meteor_data:
#    print(meteor)
    if not ('reclat' in meteor and 'reclong' in meteor): continue
    meteor['distance'] = calc_dist(float(meteor['reclat']), float(meteor['reclong']), my_loc[0], my_loc[1])

# sort the dictionary by distance 1st get the distance if no distance place at end of list
        
def get_dist(meteor):
    return meteor.get('distance', math.inf)

meteor_data.sort(key=get_dist)

# Metors at the end of the list
print(meteor_data[-1:-11:-1])

#print("Meteors in list ", len(meteor_data))

#meteors without distance 
len([m for m in meteor_data if 'distance' not in m])





