import pandas as pd
import plotly.graph_objects as go
import re
import geopy
import geopandas
import plotly.figure_factory as ff
import time

'''import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.scatter_geo(df, locations="iso_alpha",
                     size="pop", # size of markers, "pop" is one of the columns of gapminder
                     )
fig.show()
'''


#load
df = pd.read_csv('traffic_collisons.csv')

#clean
df['date_time']=pd.to_datetime(df['date_time'])

#if they have the same id number they were part of the same accident



df['report_id'] = df['report_id'].str.extract('(\d+)', expand=False)
df['report_id']=pd.to_numeric(df['report_id'])

ad = ['address_no_primary','address_road_primary']
df[ad] = df[ad].astype('str')
for i in list(ad):
    df[i] = df[i].str.strip()

df['address_full']=df[ad[0]] + " " + df[ad[1]]



len(df['address_full'].unique())
locator = geopy.Nominatim(user_agent= "myGeocoder",timeout=3)

lat = []
lon = []

start_time = time.time()
for i in list(df['address_full'][0:100]):
    loc_ = locator.geocode(i + ", San Diego, California")
    if loc_ is None:
        lat.append(0)
        lon.append(0)
    else:
        lat.append(loc_[1][0])
        lon.append(loc_[1][1])
print("--- %s seconds ---" % (time.time() - start_time))

df_ge=pd.DataFrame(data={'lat':lat,'lon':lon})



fig = go.Figure(data=go.Scattergeo(
    lat=df_ge['lat'],
    lon=df_ge['lon'],
    mode = 'markers',
        ))
fig.update_geos(fitbounds="locations",showsubunits=True, subunitcolor="Blue")
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

m=locator.geocode("0 CARMEL VALLEY, San Diego, California")



''' ['report_id', 'date_time', 'person_role', 
    'person_injury_lvl', 'person_veh_type', 'veh_type', 
    'veh_make', 'veh_model', 'police_beat', 
    'address_no_primary', 'address_pd_primary', 'address_road_primary', 
    'address_sfx_primary', 'address_pd_intersecting', 'address_name_intersecting', 
    'address_sfx_intersecting', 'violation_section', 'violation_type', 
    'charge_desc', 'injured', 'killed', 'hit_run_lvl']
'''

'''
Exploratory anlaysis
'''

#the amount of variable rows that are adaquate...
#date_time, address o

df['repo']=pd.to_numeric(df['report_id'])
for i in list(df):
    print(type(df['report_id']))

fig =go.Figure()
fig.add_histogram()

