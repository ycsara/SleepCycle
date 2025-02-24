import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels

st.title('Sleep Health Data Analysis')

sh = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv', sep=',')

st.subheader('Difference in Lifestyle Factors')
st.write('The bar graph and scatterplot show health effects based on occupation and sleep disorders')
    
choose1 = ['Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 
          'Stress Level', 'Heart Rate', 'Daily Steps']
selected_type1 = st.selectbox('Choose a variable to visualize', choose1)
sleep_occ = sh.groupby('Occupation')[selected_type1].mean().reset_index()
fig1 = px.bar(sleep_occ, x='Occupation', y=selected_type1, color=selected_type1,
              color_continuous_scale='redor')
fig1.update_layout(title=f'<b> Average {selected_type1} by Occupation</b>')
st.plotly_chart(fig1)

choose2 = ['Sleep Duration', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']
selected_type2 = st.selectbox('Choose a variable to visualize', choose2)
sh['Sleep Disorder'].fillna('None', inplace=True)
fig2 = px.scatter(sh,x='Quality of Sleep', y=selected_type2, color='Sleep Disorder', 
                  size_max=13, trendline='ols')
fig2.update_layout(title=f'<b> Quality of Sleep vs {selected_type2} by Sleep Disorders </b>')
st.plotly_chart(fig2)

#choose3 = ['Sleep Duration', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']
#selected_type3 = st.selectbox('Choose a variable to visualize', choose3)
#fig2 = px.scatter(sh,x='Quality of Sleep', y=selected_type3 color='Sleep Disorder', 
#                  size_max=13, trendline='ols')
#fig2.update_layout(title=f'<b> Quality of Sleep vs {selected_type3} by Sleep Disorders </b>')
#st.plotly_chart(fig3)

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