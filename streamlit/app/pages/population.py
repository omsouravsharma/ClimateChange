import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(layout="wide")

filename = "../data/canada_population.csv"

data = pd.read_csv(filename)
print(data)

st.map(data)