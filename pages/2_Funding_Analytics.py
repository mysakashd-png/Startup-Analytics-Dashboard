import streamlit as st
from utils.load_data import load_data
from utils.charts import *

st.set_page_config(page_title="Funding Analytics", layout="wide")

df = load_data()

st.title("💰 Funding Analytics")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        funding_by_industry(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        funding_rounds(df),
        use_container_width=True
    )

st.divider()

st.plotly_chart(
    market_share_analysis(df),
    use_container_width=True
)

st.divider()

top_funded = df.nlargest(
    10,
    "Funding Amount (M USD)"
)[
    [
        "Startup Name",
        "Industry",
        "Funding Amount (M USD)"
    ]
]

st.subheader("Top 10 Funded Startups")

st.dataframe(
    top_funded,
    use_container_width=True
)
