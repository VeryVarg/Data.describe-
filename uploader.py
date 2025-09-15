import streamlit as st
import pandas as pd 

st.header("Upload your CSV file and get its statistics instantly!")

file = st.file_uploader("Upload the file from here")

if file is not None:
    df = pd.read_csv(file)
    st.write("Here's a preview of your data:")
    st.dataframe(df)
    st.write("Here's some basic statistics about your data:")
    st.write(df.describe())
else:
    st.write("Please upload a CSV file to get started.")