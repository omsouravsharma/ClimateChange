import pandas as pd
import streamlit as st

climate_data_non_null_updated = pd.read_csv('../../data/climate_data_non_null.csv', encoding='latin')
df = climate_data_non_null_updated.copy()

drop_column_list = []
for i in range(0, df.shape[1]):
#     print(i)
    column = df.iloc[:,i]
    if column.isna().value_counts()[0]==100:
#         print(f"i value = {i}, {column.name} and count is {column.isna().value_counts()[0]}")
        continue
    elif column.isna().value_counts()[1]< 70:
#         print(f"Drop - i value = {i}, {column.name} and count is {column.isna().value_counts()[0]}")
        drop_column_list.append(column.name)
#         df.drop(column.name, axis='columns', inplace=True)
   
for col in drop_column_list:
#     print(col)
    df.drop(col,axis=1, inplace=True)

df_map = df[['REPORT_RECEIVED_DATE','LOCATION_LATITUDE', 'LOCATION_LONGITUDE']]
df_map.rename(columns={'LOCATION_LATITUDE':'LATITUDE', 'LOCATION_LONGITUDE':'LONGITUDE'}, inplace=True)
st.map(df_map)