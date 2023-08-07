import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from plotly.offline import iplot
import cufflinks


st.set_page_config(layout="wide")
energy_source = pd.read_csv("../../data/primary-energy-source-bar-3.csv")
# energy_source['Year'] = 

# locations = data.location.unique().tolist()
counteries = energy_source.Entity.unique().tolist()

sidebar = st.sidebar
location_selector = sidebar.selectbox(
    "Select a Country",counteries
    )

st.markdown(f"## Country Selected {location_selector}\n")

country_energy_source = energy_source.loc[energy_source['Entity']== location_selector]




fig_can_line = st.line_chart(country_energy_source, x="Year", y =["Coal consumption - TWh",'Coal consumption - TWh',
       'Oil consumption - TWh', 'Gas consumption - TWh',
       'Nuclear consumption - TWh', 'Hydro consumption - TWh',
       'Wind consumption - TWh', 'Solar consumption - TWh',
       'Other renewables (including geothermal and biomass) - TWh'])

fig_can_area = st.area_chart(country_energy_source, x="Year", y =["Coal consumption - TWh",'Coal consumption - TWh',
       'Oil consumption - TWh', 'Gas consumption - TWh',
       'Nuclear consumption - TWh', 'Hydro consumption - TWh',
       'Wind consumption - TWh', 'Solar consumption - TWh',
       'Other renewables (including geothermal and biomass) - TWh'])

fig_plotly_line = px.line(country_energy_source, x="Year", y =["Coal consumption - TWh",'Coal consumption - TWh',
       'Oil consumption - TWh', 'Gas consumption - TWh',
       'Nuclear consumption - TWh', 'Hydro consumption - TWh',
       'Wind consumption - TWh', 'Solar consumption - TWh',
       'Other renewables (including geothermal and biomass) - TWh'])
st.plotly_chart(fig_plotly_line, use_container_width=True)


fig_plotly_area = px.area(country_energy_source, x="Year", y =["Coal consumption - TWh",'Coal consumption - TWh',
       'Oil consumption - TWh', 'Gas consumption - TWh',
       'Nuclear consumption - TWh', 'Hydro consumption - TWh',
       'Wind consumption - TWh', 'Solar consumption - TWh',
       'Other renewables (including geothermal and biomass) - TWh'])
st.plotly_chart(fig_plotly_area, use_container_width=True)


#checkbox
show_data = sidebar.checkbox("Show Data")

if show_data:
    st.dataframe(country_energy_source)
