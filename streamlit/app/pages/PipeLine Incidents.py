import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
# import folium
import json
import os
import geopandas
import streamlit as st

data = pd.read_csv(r'../data/pipeline-incidents-comprehensive-data.csv', encoding='latin-1')

incidents = data['Incident Types'].value_counts()

provinces = pd.DataFrame(data['Province'].value_counts())
# provinces['prov_name_en'] = provinces.index
provinces = provinces.reset_index()
provinces.rename(columns = {"count":"incident_counts", "Province":"prov_name_en"}, inplace=True)
# provinces.reindex(axis=0)

canada_data = geopandas.read_file("../data/georef-canada-province@public.geojson")

canada_data['prov_name_en'] = ['Alberta',
 'Manitoba',
 'Yukon',
 'Saskatchewan',
 'Nova Scotia',
 'Northwest Territories',
 'Prince Edward Island',
 'Nunavut',
 'Quebec',
 'Ontario',
 'British Columbia',
 'Newfoundland and Labrador',
 'New Brunswick']

combined_data = pd.merge(canada_data, provinces, on="prov_name_en", how="left")
# print(combined_data)
data.rename(columns={'Latitude':'LATITUDE', 'Longitude':'LONGITUDE'}, inplace=True)

df = data[['Incident Types', "LATITUDE", 'LONGITUDE']]
print(df)
# print(data.head(5))
# st.map(combined_data)
# print(data.columns)

# st.write(data)
# st.map(data['Incident Types'],latitude=data["LATITUDE"], longitude=data["LONGITUDE"] )
st.map(df)