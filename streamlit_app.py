import plotly.graph_objects as go
import streamlit as st

st.write('Bellingcat Hackathon Apr 2023: Accessibility Tool')
st.write('# BOMBARDIER WATCH #####')

st.markdown("""---""") 

df = pd.read_csv('dfMERGE.csv')
st.dataframe(data=df)
