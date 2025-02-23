import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.header('Analysis of Sleep Cycle Productivity')

sleep = pd.read_csv('sleep_cycle_productivity.csv', sep=',')

st.write('This graph will analyze how much the amount of sleep can affect productivity, mood, and stress.')

score = ['Productivity Score', 'Mood Score', 'Stress Level']
selected_type = st.selectbox('Split', score)
fig1 = px.histogram(sleep, x='Sleep Quality', color=selected_type)
fig1.update_layout(title='<b> Split of price by {}</b>'.format(selected_type))
st.plotly_chart(fig1)