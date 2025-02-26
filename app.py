import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Sleep Health Data Analysis')

sh = pd.read_csv('sleep_health_lifestyle.csv', sep=',')
sh = sh.rename(columns={'Blood Pressure (systolic/diastolic)':'Blood Pressure', 'Heart Rate (bpm)':'Heart Rate'})

st.subheader('Occupational Lifestyle Differences')
st.write('This bar graph will show you the average differences in lifestyle by occupation.')
    
choose1 = ['Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 
          'Stress Level', 'Heart Rate', 'Daily Steps']
selected_type1 = st.selectbox('Choose a lifestyle variable to visualize', choose1, 
                              key='occupation')
box1 = st.checkbox('Click to group by gender')
if box1:
    sleep_occ_gender = sh.groupby(['Occupation', 'Gender'])[selected_type1].mean().reset_index()
    fig1 = px.bar(sleep_occ_gender, x='Occupation', y=selected_type1, color='Gender', 
                  barmode='group', color_continuous_scale='redor', labels={selected_type1: selected_type1},  
                  title=f'<b> Average {selected_type1} by Occupation by Gender</b>')
else:
    sleep_occ = sh.groupby('Occupation')[selected_type1].mean().reset_index()
    fig1 = px.bar(sleep_occ, x='Occupation', y=selected_type1, color=selected_type1,
                  color_continuous_scale='redor', title=f'<b> Average {selected_type1} by Occupation</b>')
st.plotly_chart(fig1)

st.subheader('Lifestyle Differences with Sleep Disorders')
st.write('This scatterplot will show you the correlation between sleep disorders and lifestyle habits.')

choose2 = ['Sleep Duration', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps']
selected_type2 = st.selectbox('Choose a lifestyle variable to visualize', choose2,
                              key='sleep_disorders')
sh['Sleep Disorder'].fillna('None', inplace=True)
fig2 = px.scatter(sh,x='Quality of Sleep', y=selected_type2, color='Sleep Disorder', 
                  size_max=10, trendline='ols')
fig2.update_layout(title=f'<b> Quality of Sleep vs {selected_type2} by Sleep Disorders </b>')
st.plotly_chart(fig2)

st.subheader('Different Lifestyles Based on BMI')
st.write('The histogram will show you the distribution of lifestyle habits grouped by BMI categories and gender.')

bmi = sh['BMI Category'].unique()
choose3 = ['Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 
          'Stress Level', 'Heart Rate', 'Daily Steps']
bmi_choose = st.selectbox('Choose a BMI category to visualize', bmi)
selected_type3 = st.selectbox('Choose a lifestyle variable to visualize', choose3,
                              key='BMI_category')
filtered = sh[sh['BMI Category'] == bmi_choose]
fig3 = px.histogram(filtered, x=selected_type3, color='Gender', nbins=10, barmode='overlay', 
    title=f'<b>{selected_type3} for {bmi_choose} BMI Category</b>', labels={selected_type3: selected_type3})
st.plotly_chart(fig3)