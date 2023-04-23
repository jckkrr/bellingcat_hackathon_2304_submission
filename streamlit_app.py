import plotly.graph_objects as go
import streamlit as st

st.write('Bellingcat Hackathon Apr 2023: Accessibility Tool')
st.write('# BOMBARDIER WATCH #####')

st.markdown("""---""") 

DATA_URL = 'business_jet_type_codes.csv'
df = pd.read_csv(DATA_URL)
st.dataframe(data=df)

