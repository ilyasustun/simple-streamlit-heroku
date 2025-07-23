import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


@st.cache_data()
def load_data():
    # data = pd.read_csv('https://github.com/4GeeksAcademy/machine-learning-content/blob/master/assets/titanic_train.csv')

    data = pd.read_csv('https://raw.githubusercontent.com/4GeeksAcademy/machine-learning-content/refs/heads/master/assets/titanic_train.csv')
    return data

data = load_data()

# Data Viz
st.sidebar.title('Data Visualization')
st.sidebar.markdown('Select the type of plot you want to see')
plot_type = st.sidebar.selectbox('Plot Type', ['Bar Chart', 'Pie Chart',

'Histogram', 'Box Plot'])
if plot_type == 'Bar Chart':
    st.subheader('Bar Chart')
    x_axis = st.sidebar.selectbox('X-axis', data.columns)
    y_axis = st.sidebar.selectbox('Y-axis', data.columns)
    fig = px.bar(data, x=x_axis, y=y_axis, title=f'Bar Chart of {y_axis} vs {x_axis}')
    st.plotly_chart(fig)
elif plot_type == 'Pie Chart':  
    st.subheader('Pie Chart')
    column = st.sidebar.selectbox('Column', data.columns)
    fig = px.pie(data, names=column, title=f'Pie Chart of {column}')
    st.plotly_chart(fig)
elif plot_type == 'Histogram':
    st.subheader('Histogram')
    column = st.sidebar.selectbox('Column', data.columns)
    fig = px.histogram(data, x=column, title=f'Histogram of {column}')
    st.plotly_chart(fig)
elif plot_type == 'Box Plot':
    st.subheader('Box Plot')
    column = st.sidebar.selectbox('Column', data.columns)
    fig = px.box(data, y=column, title=f'Box Plot of {column}')
    st.plotly_chart(fig)


st.markdown('<style>description{color:blue;}</style>', unsafe_allow_html=True)
st.title('Titanic survival prediction')
st.markdown("<description>The sinking of the Titanic is one of the most infamous shipwrecks in history. " + 
"On April 15, 1912, during her maiden voyage, the widely considered “unsinkable” RMS Titanic sank after colliding " +
"with an iceberg. Unfortunately, there weren't enough lifeboats for everyone onboard, resulting in the death of " +
"1502 out of 2224 passengers and crew. While there was some element of luck involved in surviving, it seems some " +
"groups of people were more likely to survive than others. </description>", unsafe_allow_html=True)
st.sidebar.title('Select the parameters to analyze survival prediction')