import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.header('Analysis of Sleep Cycle Productivity')

sleep = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv', sep=',')

st.write('This graph will analyze how much sleep quality can affect productivity, mood, and stress.')

score = ['Productivity Score', 'Mood Score', 'Stress Level']
selected_type = st.selectbox('Choose a variable', score)
#sleep = sleep.sort_values(by='Sleep Quality')
fig1 = px.histogram(sleep, x='Sleep Quality', color=selected_type, nbins=20)
fig1.update_layout(title='<b> Distribution of Sleep Quality by {}</b>'.format(selected_type))
fig1.update_yaxes(categoryorder='category ascending')
st.plotly_chart(fig1)