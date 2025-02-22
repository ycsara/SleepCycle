import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Analysis of Sleep Cycle Productivity')
st.write('Filter the data below to see the ads by manufacturer')

sleep = pd.read_csv('sleep_cycle_productivity.csv', sep=',')

mood_choice = sleep['Mood Score'].unique()
st.selectbox('Select a Mood Score', mood_choice)