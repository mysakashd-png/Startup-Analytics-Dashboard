
import streamlit as st
import plotly.express as px
from utils.load_data import load_data
from utils.insights import generate_insights

st.set_page_config(page_title="Industry Insights", layout="wide")

df = load_data()

st.title("🏭 Industry Insights")

industry_revenue = (
    df.groupby("Industry")
    ["Revenue (M USD)"]
    .sum()
    .reset_index()
)

fig = px.bar(
    industry_revenue,
    x="Industry",
    y="Revenue (M USD)",
    color="Industry",
    title="Industry Revenue Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

industry_valuation = (
    df.groupby("Industry")
    ["Valuation (M USD)"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    industry_valuation,
    x="Industry",
    y="Valuation (M USD)",
    color="Industry",
    title="Average Valuation by Industry"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.subheader("📈 AI Generated Insights")

insights = generate_insights(df)

for item in insights:
    st.info(item)
