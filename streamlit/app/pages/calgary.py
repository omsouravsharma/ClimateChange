import pandas as pd
import numpy as np
import streamlit as st


data = pd.read_csv("../data/calgary.csv")
# df = data[['time','mean_temp']]
data['time'] = pd.to_datetime(data['time'])
# data['time']= pd.to_datetime(data['time'])
# print(data)
df = data[['time', 'mean_temp']]
df.index = data['time']
df = df.drop('time', axis=1)

print(df)
st.map(data)

st.line_chart(df)