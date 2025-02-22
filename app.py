import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title('Analysis of Sleep Cycle Productivity')

sleep = pd.read_csv('sleep_cycle_productivity.csv', sep=',')

st.write('This graph will analyze how much the amount of sleep can affect productivity, mood, and stress.')
fig1 = px.histogram(sleep, x='Total Sleep Hours')

st.title('Analysis of Sleep Cycle Productivity')