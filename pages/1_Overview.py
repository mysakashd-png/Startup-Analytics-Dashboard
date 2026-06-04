import streamlit as st
from utils.load_data import load_data

st.set_page_config(page_title="Overview", layout="wide")

df = load_data()

st.title("🚀 Startup Overview Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Startups",
        len(df)
    )

with col2:
    st.metric(
        "Total Funding",
        f"${df['Funding Amount (M USD)'].sum():,.0f} M"
    )

with col3:
    st.metric(
        "Total Revenue",
        f"${df['Revenue (M USD)'].sum():,.0f} M"
    )

with col4:
    st.metric(
        "Average Valuation",
        f"${df['Valuation (M USD)'].mean():,.0f} M"
    )

st.divider()

st.subheader("Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.subheader("Dataset Statistics")

st.dataframe(
    df.describe(),
    use_container_width=True
)
