import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objs as go
plt.style.use('ggplot')
# import folium
import json
import os
import geopandas
import streamlit as st

st.set_page_config(layout="wide")

data = pd.read_csv(r'../../data/pipeline-incidents-comprehensive-data.csv', encoding='latin-1')

incidents = data['Incident Types'].value_counts()

provinces = pd.DataFrame(data['Province'].value_counts())
# provinces['prov_name_en'] = provinces.index
provinces = provinces.reset_index()
provinces.rename(columns = {"count":"incident_counts", "Province":"prov_name_en"}, inplace=True)
# provinces.reindex(axis=0)

canada_data = geopandas.read_file("../../data/georef-canada-province@public.geojson")

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

df_map = data[['Incident Types', "LATITUDE", 'LONGITUDE']]
# print(df)
# print(data.head(5))
# st.map(combined_data)
# print(data.columns)

# st.write(data)
# st.map(data['Incident Types'],latitude=data["LATITUDE"], longitude=data["LONGITUDE"] )
st.map(df_map)

# Incident Types are:

st.markdown("# Incident Types")
df=  pd.DataFrame(data["Incident Types"].value_counts())
df = df.reset_index()
# df
fig = go.Figure(data=[go.Bar(
            x=df['Incident Types'], y=df['count'],
            text=df['count'],
            textposition='auto',
            marker_color = '#ff6983'
        )])

st.plotly_chart(fig, use_container_width=True)

# Companies

st.markdown("# Company Name")
df2 = data['Company'].value_counts()
df2 = df2.reset_index()
df2 = df2[df2["count"]>9]


fig_companies = go.Figure(data=[go.Bar(
            x=df['Incident Types'], y=df['count'],
            text=df['count'],
            textposition='auto',
            marker_color = '#f1c232'
        )])

st.plotly_chart(fig_companies, use_container_width=True)

# Significant Events

st.markdown("# Significant Events")
df3 = data['Significant'].value_counts()
df3 = df3.reset_index()
fig_significant = go.Figure(data=[go.Bar(
            x=df3['Significant'], y=df3['count'],
            text=df3['count'],
            textposition='auto',
            marker_color = '#a3c752'
        )])

st.plotly_chart(fig_significant, use_container_width=True)

# Year

st.markdown("# Year")
df4 = data['Year'].value_counts()
df4 = df4.reset_index()

fig_year = go.Figure(data=[go.Bar(
            x=df4['Year'], y=df4['count'],
            text=df4['count'],
            textposition='auto',
            marker_color = '#cd5c5c'
        )])
st.plotly_chart(fig_year, use_container_width=True)

# Emergency Level
st.markdown("# Emergency Level")

df5 = data['Emergency Level'].value_counts()
df5 = df5.reset_index()

fig_emergency_level = go.Figure(data=[go.Bar(
            x=df5['Emergency Level'], y=df5['count'],
            text=df5['count'],
            textposition='auto',
            marker_color = '#4a386f'
        )])
st.plotly_chart(fig_emergency_level, use_container_width=True)


# Repair Type
st.markdown("# Repair Type")

df6 = data['Repair type'].value_counts()
df6 = df6.reset_index()

fig_repair_type = go.Figure(data=[go.Bar(
            x=df6['Repair type'], y=df6['count'],
            text=df6['count'],
            textposition='auto',
            marker_color = '#4682b4'
        )])

st.plotly_chart(fig_repair_type, use_container_width=True)