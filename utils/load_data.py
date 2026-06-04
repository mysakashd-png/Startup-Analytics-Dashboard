import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path="data/startup_data.csv"):
    df = pd.read_csv(path)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df.fillna(0, inplace=True)

    return df
