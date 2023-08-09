import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import json

st.set_page_config(layout="wide")

data = pd.read_csv('../../data/canada_population.csv')
data.rename(columns={"provinces":"prov_name_en"}, inplace=True)
data.replace({"Newfoundland And Labrador":"Newfoundland and Labrador"}, inplace=True)
df = data[['prov_name_en','population']]


with open('../../data/canada.geojson') as response:
    canada_json = json.load(response)
# canada_json

fig_populaton = px.choropleth_mapbox(
    data_frame = df,            # Data frame with values
    geojson = canada_json,                      # Geojson with geometries
    featureidkey = 'properties.name', # Geojson key which relates the file with the data from the data frame
    locations = 'prov_name_en',               # Name of the column of the data frame that matches featureidkey
    color = 'population',                # Name of the column of the data frame with the data to be represented
    mapbox_style = 'open-street-map',
    color_continuous_scale="matter",
    center = dict(lat =49.892723, lon = -97.144234),
    zoom = 2,
    opacity = 0.5)

st.plotly_chart(fig_populaton, use_container_width=True)
