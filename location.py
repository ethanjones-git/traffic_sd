'''
Ethan Jones

This scripts puts a lattitude and longitude to given address.

This moves at a pace of appox 1 min per 100 rows.
'''

import pandas as pd
import plotly.graph_objects as go
import re
import geopy
import geopandas
import plotly.figure_factory as ff
import time
import plotly.graph_objects as go

#load
df = pd.read_csv('traffic_collisons.csv')

#clean street address strings
df['report_id'] = df['report_id'].str.extract('(\d+)', expand=False)
df['report_id']=pd.to_numeric(df['report_id'])
ad = ['address_no_primary','address_road_primary']
df[ad] = df[ad].astype('str')
for i in list(ad):
    df[i] = df[i].str.strip()

#create street addresses
df['address_full']=df[ad[0]] + " " + df[ad[1]]



#extracts the lattitude and longitude given address
locator = geopy.Nominatim(user_agent= "myGeocoder",timeout=5)

lat = []
lon = []
ad = []

len(df['address_full'].unique())

start_time = time.time()
for i in list(df['address_full'].unique()):
    ad.append(i)
    loc_ = locator.geocode(i + ", San Diego, California")
    if loc_ is None:
        lat.append(0)
        lon.append(0)
    else:
        lat.append(loc_[1][0])
        lon.append(loc_[1][1])

#create and save df
df_ge=pd.DataFrame(data={'lat':lat[0:10404],'lon':lon[0:10404],'ad':ad[0:10404]})
df_ge.to_csv('/Users/ethanjones/PycharmProjects/traffic_sd/lat_long_0_10404.csv')

'''
Try again
'''
for i in list(df['address_full'].unique()[10406:]):
    ad.append(i)
    loc_ = locator.geocode(i + ", San Diego, California")
    if loc_ is None:
        lat.append(0)
        lon.append(0)
    else:
        lat.append(loc_[1][0])
        lon.append(loc_[1][1])

df_ge
'''fig = go.Figure(data=go.Scattergeo(
    lat=df_ge['lat'],
    lon=df_ge['lon'],
    mode = 'markers',
        ))
fig.update_geos(fitbounds="locations",showsubunits=True, subunitcolor="Blue")
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()'''



len(df['address_full'].unique())