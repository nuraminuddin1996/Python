import io
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Analyze Your Data',layout='wide',page_icon='🐼')
st.title("🧽 Analyze your Data")
st.write("Upload A **CSV** File and Explore Your Data")

# for uploading csv file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        # cvrt boolean col as str
        bool_cols = df.select_dtypes(include=['bool']).columns
        df[bool_cols] = df[bool_cols].astype(str)
    except Exception as e:
        st.error('Could not read the file. Please upload the csv file again')
        st.exception(e)
        st.stop()
    
    st.success('File Upload Successfully!')
    st.write('**Preview of Data**')
    st.dataframe(df.head())


    st.write('**Data Overview**')
    st.write('NUmber of Row :',df.shape[0])
    st.write("Number Of Columns :",df.shape[1])
    st.write("Number Of Missing Values :",df.isnull().sum().sum())
    st.write("Number Of Duplicate Records :",df.duplicated().sum())

    st.write('**Complete summary of Dataset**')
    buffer = io.StringIO()
    df.info(buf=buffer)
    info = buffer.getvalue()
    st.text(info)

    st.write("**Statistical Summary Of Dataset**")
    st.dataframe(df.describe())


    st.write("**Statistical Summary For Non Numerical Features**")
    st.dataframe(df.describe(include='object'))

    st.write("**Select Your Desired Columns**")
    column = st.multiselect("Choose Columns",df.columns.tolist())
    st.write("**Preview**")

    if column:
        st.dataframe(df[column].head())
    
    else:
        st.info("No Columns Selected. Showing Full Dataset")
        st.dataframe(df.head())

    st.write('**Data Visualization**')
    columns = df.columns.tolist()
    x_axis = st.selectbox('Select Columns For The X- Axis',options=columns)
    y_axis = st.selectbox('Select Columns For The Y- Axis',options=columns)

    # create buttons for chart types
    col1,col2 = st.columns(2)

    with col1:
        lin_btn = st.button('Click Here To Generate A Line Graph')
    with col2:
        bar_btn = st.button('Click Here To Generate A Bar Graph')

    # Plot Line Chart
    if lin_btn:
        st.write('Line Graph')
        fig, ax = plt.subplots()
        ax.plot(df[x_axis], df[y_axis], marker='o')
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"Line Graph of {y_axis} vs {x_axis}")
        st.pyplot(fig)

    if bar_btn:
        st.write('Bar Graph')
        fig, ax = plt.subplots()
        ax.bar(df[x_axis], df[y_axis], color='skyblue')
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"Bar Chart of {y_axis} vs {x_axis}")
        st.pyplot(fig)


