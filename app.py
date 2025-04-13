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



# Create header
st.header('Vehicle Price Distribution Analysis')

# Create Plotly Express histogram
fig = px.histogram(df, 
                   x='price',
                   nbins=50,
                   title='Distribution of Vehicle Prices',
                   labels={'price': 'Price ($)'},
                   color_discrete_sequence=['#1f77b4'])

# Customize layout
fig.update_layout(
    bargap=0.1,
    xaxis_title='Vehicle Price ($)',
    yaxis_title='Number of Listings',
    hovermode='x unified'
)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Optional: Add interactive filters
st.subheader('Filter by Vehicle Type')
selected_type = st.selectbox(
    'Select vehicle type to analyze:',
    options=['All'] + sorted(df['type'].unique().tolist())
    
if selected_type != 'All':
    filtered_df = df[df['type'] == selected_type]
    fig2 = px.histogram(filtered_df, 
                       x='price',
                       nbins=30,
                       title=f'Price Distribution for {selected_type}',
                       labels={'price': 'Price ($)'},
                       color_discrete_sequence=['#ff7f0e'])
    st.plotly_chart(fig2, use_container_width=True)
