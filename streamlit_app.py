import plotly.graph_objects as go
import streamlit as st

st.write('Bellingcat Hackathon Apr 2023: Accessibility Tool')
st.write('# BOMBARDIER WATCH #####')

st.markdown("""---""") 

DATA_URL = 'dfMERGE.csv'
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data
df = load_data()
st.dataframe(data=df)

