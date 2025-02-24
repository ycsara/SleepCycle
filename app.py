import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Sleep Health Data Analysis')

sh = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv', sep=',')

st.subheader('Difference in Lifestyle Factors')
st.write('The bar graph and scatterplot show health effects based on occupation and sleep disorders')
    
choose = ['Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 
          'Stress Level', 'Heart Rate', 'Daily Steps']
selected_type = st.selectbox('Choose a variable to visualize', choose)
sleep_occ = sh.groupby('Occupation')[selected_type].mean().reset_index()
fig1 = px.bar(sleep_occ, x='Occupation', y=selected_type, color=selected_type,
              color_continuous_scale='redor')
fig1.update_layout(title=f'<b> Average {selected_type} by Occupation</b>')
st.plotly_chart(fig1)

sh['Sleep Disorder'].fillna('None', inplace=True)
fig2 = px.scatter(sh,x='Quality of Sleep', y=selected_type, color='Sleep Disorder', 
                  size_max=13, trendline='ols')
fig2.update_layout(title=f'<b> Quality of Sleep vs {selected_type} by Sleep Disorders </b>')
st.plotly_chart(fig2)

st.subheader('Group by Gender')
st.write('The histogram displays the distribution grouped by gender.')

box = st.checkbox('Click to group by gender')
if box:
    fig3 = px.histogram(sh, x='Sleep Duration', nbins=20, color='Gender',
                        barmode='overlay', title='<b>Sleep Duration by Gender</b>',
                        labels={'Sleep Duration': 'Sleep Duration (hours)'})
else:
    fig3 = px.histogram(sh, x='Sleep Duration', title='<b>Sleep Duration</b>',
                       labels={'Sleep Duration': 'Sleep Duration (hours)'}, nbins=20)
st.plotly_chart(fig3)