import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objs as go

st.set_page_config(layout="wide")

data = pd.read_csv("../../data/usa_incident_gas_distribution_jan2010_present.csv", encoding='latin')

df_map = data[['REPORT_NUMBER','LOCATION_LATITUDE', 'LOCATION_LONGITUDE']]
df_map.rename(columns={'LOCATION_LATITUDE':'LATITUDE', 'LOCATION_LONGITUDE':'LONGITUDE'}, inplace=True)
st.map(df_map)



# Year

st.markdown("# Year")
df_year = data['IYEAR'].value_counts()

df_year = df_year.reset_index()

fig_year = go.Figure(data=[go.Bar(
            x=df_year['IYEAR'], y=df_year['count'],
            text=df_year['count'],
            textposition='auto',
            marker_color = '#cd5c5c'
        )])
st.plotly_chart(fig_year, use_container_width=True)

# Companies

st.markdown("# Company Name")
df2 = data['NAME'].value_counts()
df2 = df2.reset_index()
df2 = df2[df2["count"]>9]


fig_companies = go.Figure(data=[go.Bar(
            x=df2['NAME'], y=df2['count'],
            text=df2['count'],
            textposition='auto',
            marker_color = '#f1c232'
        )])

st.plotly_chart(fig_companies, use_container_width=True)

# Cause

st.markdown("# Cause")
df_cause = data['CAUSE'].value_counts()
df_cause = df_cause.reset_index()
df_cause = df_cause[df_cause["count"]>9]


fig_cause = go.Figure(data=[go.Bar(
            x=df_cause['CAUSE'], y=df_cause['count'],
            text=df_cause['count'],
            textposition='auto',
            marker_color = '#f1c232'
        )])

st.plotly_chart(fig_cause, use_container_width=True)

# Cause = NATURAL FORCE DAMAGE
 

st.markdown("# Cause = NATURAL FORCE DAMAGE")
df_cause_nfd = data[data['CAUSE'] == 'NATURAL FORCE DAMAGE']['CAUSE_DETAILS'].value_counts()
df_cause_nfd = df_cause_nfd.reset_index()
df_cause_nfd = df_cause_nfd[df_cause_nfd["count"]>9]


fig_cause_nfd = go.Figure(data=[go.Bar(
            x=df_cause_nfd['CAUSE_DETAILS'], y=df_cause_nfd['count'],
            text=df_cause_nfd['count'],
            textposition='auto',
            marker_color = '#cd5c5c'
        )])

st.plotly_chart(fig_cause_nfd, use_container_width=True)