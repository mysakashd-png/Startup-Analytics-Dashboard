import streamlit as st
import plotly.express as px
from utils.load_data import load_data
from utils.charts import regional_distribution

st.set_page_config(page_title="Regional Analysis", layout="wide")

df = load_data()

st.title("🌍 Regional Analysis")

st.plotly_chart(
    regional_distribution(df),
    use_container_width=True
)

region_funding = (
    df.groupby("Region")
    ["Funding Amount (M USD)"]
    .sum()
    .reset_index()
)

fig = px.bar(
    region_funding,
    x="Region",
    y="Funding Amount (M USD)",
    color="Region",
    title="Funding by Region"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

region_revenue = (
    df.groupby("Region")
    ["Revenue (M USD)"]
    .sum()
    .reset_index()
)

fig2 = px.line(
    region_revenue,
    x="Region",
    y="Revenue (M USD)",
    markers=True,
    title="Revenue by Region"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
