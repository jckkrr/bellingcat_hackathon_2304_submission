import datetime
from geopy.geocoders import Nominatim
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv('dfMERGE.csv')
display_df = df[['hex', 'r', 'RegisteredOwners', 'Manufacturer', 'Type', 'lat_rnd', 'lon_rnd']]


