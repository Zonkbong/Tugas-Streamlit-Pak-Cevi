# streamlit_app.py

import pandas as pd
import streamlit as st

# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(allow_output_mutations=True)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])
st.subheader('Sebutkan nama - nama hero dari berbagai universe')

# Print results.
for row in df.itertuples():
    st.write(f"Hero has a : {row.Hero}")
    st.write(f"Skill has a : {row.Skill}")    
    st.write(f"Country has a : {row.Country}")
    st.write("#")