import datetime
from geopy.geocoders import Nominatim
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from bs4 import BeautifulSoup

df = pd.read_csv('dfMERGE.csv')
display_df = df[['hex', 'r', 'RegisteredOwners', 'Manufacturer', 'Type', 'lat_rnd', 'lon_rnd']]

#### SUB FUNCTIONS #######################

def getSoup(url):
    
    from requests import get
    from bs4 import BeautifulSoup
    import requests

    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14'
    headers = {'User-Agent': user_agent,'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    return soup

def imageRetrieval(ICAOHEX):
    
    url = f'https://hexdb.io/hex-image?hex={ICAOHEX}'
    soup = getSoup(url)

    image_url = 'https:' +  soup.find('p').text
    
    return image_url

def getBYCOMPANY(chosen_company):

    dfCOORDS = df.loc[df['RegisteredOwners'] == chosen_company][['lat_rnd','lon_rnd']]    
    dfBYCOMPANY = df.merge(dfCOORDS)
    
    return dfBYCOMPANY

def getDisplayLocation(chosen_coords):
    
    locator = Nominatim(user_agent="myGeocoder")
    coordinates = f"{chosen_coords[0]}, {chosen_coords[1]}"
    
    location = locator.reverse(coordinates, timeout=None)
    location_raw = location.raw
    
    display_location = None
    city, state, country = '-','-','-'

    if 'address' in location_raw.keys():

        if 'city' in location_raw['address'].keys():
            city = location_raw['address']['city']

        elif 'town' in location_raw['address'].keys():
            city = location_raw['address']['town']

        if 'state' in location_raw['address'].keys():
            state = location_raw['address']['state']

        if 'country' in location_raw['address'].keys():
            country = location_raw['address']['country']

    display_location = f'{city}, {state}, {country}'    
        
    return display_location

########## STYLE #################################################

streamlit_style = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@100&display=swap');
    html, body, [class*="css"]  {
    font-family: 'Manrope', sans-serif;
    }
    .small-font {
        font-size: 10px !important;
    }
    </style>
"""
st.markdown(streamlit_style, unsafe_allow_html=True)

############################# RUN #############################

#### 
st.write('Bellingcat Hackathon Apr 2023: Accessibility Tool')

st.write('# BOMBARDIER WATCH #####')
st.write('A tool to monitor the movements of business jets around the world.')
st.write('')
st.write('by Jack Kerr (Group: Jackmaster)')
st.write('')
st.write('Unfiltered crowd-sourced flight-tracking service ADS-B Exchange offer an excellent view of air traffice movements. But finding out who is on board is another matter.')
st.write('This tool provides one solution to that: by showing which of these jets arrived or departed from the same location on the same day, it amy be possible to work out who met who.')
st.write('')
st.write('<p class="small-font">Notes: Data rouced from ADS-B Exchange. | This protype model uses data from one day, as recorded at the start of each minute. | Results filter to only include Bombardier, Gulfstream, Dassault and Embraer business jets that are show as "grounded".</p>', unsafe_allow_html=True)

st.markdown("""---""") 

d = st.date_input(
    "Date",
    datetime.date(2022, 5, 1), 
    disabled = True)

##### Visualisation

dfPLOT = df.copy()

dfPLOT['text'] = dfPLOT['lat_rnd'].astype(str) + ' | ' +  dfPLOT['lon_rnd'].astype(str)

x = dfPLOT['lon_rnd'] 
y = dfPLOT['lat_rnd'] 

fig = go.Figure(data=go.Scattergeo(
        lon = x,
        lat = y,
        text = dfPLOT['text'],
        hoverinfo="text",
        mode = 'markers',
        marker = dict(color='rgba(200,100,100,0.5)', size = 12),
        ))


# design
fig.update_layout(
    title_text = None,  
    showlegend = False,
    geo = dict(
        scope = 'world',
        projection = dict(
            type = 'orthographic',
            rotation = dict(
                lon = -40,
                lat = 30,
                roll = 0
            )
        ),
        showland = True, showocean = True, landcolor = 'rgb(243, 243, 243)', countrycolor = 'rgb(204, 204, 204)', oceancolor = '#E6F2F2',
        ),
    )

fig.update_layout(
    title = 'All locations where business jets were recorded on the ground',  width = 1000, height = 700,
)

st.plotly_chart(fig, use_container_width=True)

####

st.write('#### Check by coordinates')

cutoffs = st.slider('How many matching aircraft recorded per location', 1, 20, (2, 3))
st.write('<p class="small-font">This slider is useful for narrowing down the number of airports to only those where two meeting planes might really stick out.</p>', unsafe_allow_html=True)

dfMULTIS = df.groupby(by=['lat_rnd', 'lon_rnd']).count()['hex'].to_frame()
dfMULTIS = dfMULTIS[(dfMULTIS['hex'] >= cutoffs[0]) & (dfMULTIS['hex'] <= cutoffs[1])].sort_values(by='lat_rnd', ascending=False)

unqiue_coords = dfMULTIS.index
chosen_coords = st.selectbox(
    'Choose coordinates',
    unqiue_coords)

display_location = getDisplayLocation(chosen_coords)
st.write(display_location)

display_df_coords = display_df.loc[(display_df['lat_rnd'] == chosen_coords[0]) & (display_df['lon_rnd'] == chosen_coords[1])]

st.dataframe(data=display_df_coords)

st.markdown("""---""") 

show_pics = st.radio(
    "Show pictures of jets? (This can slow your searches)",
    ('N', 'Y'), 
    horizontal = True)

if show_pics == 'Y':
    for icao in display_df_coords['hex']:
        st.write(icao)

        image = imageRetrieval(icao)
        st.image(image)
    
####

st.markdown("""---""") 
st.write('#### Check by company')
st.write('See which other registered owners were at the same airport.')

unique_owners = display_df['RegisteredOwners'].unique()

chosen_company = st.selectbox(
    'Choose Company',
    unique_owners)

dfBYCOMPANY = getBYCOMPANY(chosen_company)
st.dataframe(data=dfBYCOMPANY[['hex', 'r', 'RegisteredOwners', 'Manufacturer', 'Type', 'lat_rnd', 'lon_rnd']])

st.markdown("""---""") 

