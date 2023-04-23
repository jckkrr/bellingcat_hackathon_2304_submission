import datetime
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

st.write('Bellingcat Hackathon Apr 2023: Accessibility Tool')
st.write('# BOMBARDIER WATCH #####')

st.markdown("""---""") 

df = pd.read_csv('dfMERGE.csv')
st.dataframe(data=df)

d = st.date_input(
    "Date",
    datetime.date(2022, 5, 1), 
    disabled = True)
