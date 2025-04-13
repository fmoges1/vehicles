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

# Main header
st.header('Vehicle Types by Price Analysis')

# 1. Show average price by vehicle type
st.subheader('Average Price by Vehicle Type')
avg_price_by_type = df.groupby('type')['price'].mean().sort_values(ascending=False).round(2)
st.write(avg_price_by_type)

# 2. Show price distribution by type
st.subheader('Price Distribution by Type')
st.write("Minimum prices:")
min_prices = df.groupby('type')['price'].min().sort_values(ascending=False)
st.write(min_prices)

st.write("\nMaximum prices:")
max_prices = df.groupby('type')['price'].max().sort_values(ascending=False)
st.write(max_prices)

# 4. Optional visualization
st.subheader('Price Distribution Visualization')
st.bar_chart(df.groupby('type')['price'].mean())


