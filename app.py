import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x:x.split()[0])

# create a text header above the dataframe
st.header('Data viewer') 
# display the dataframe with streamlit
st.dataframe(df)

# Create a header and display the dataframe
st.header('Vehicle Listings Data Viewer')
st.dataframe(df)

# Optional: Add some basic statistics
st.subheader('Quick Stats')
st.write(f"Total listings: {len(df)}")
st.write(f"Date range: {df['date_posted'].min()} to {df['date_posted'].max()}")
