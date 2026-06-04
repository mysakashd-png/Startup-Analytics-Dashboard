
import streamlit as st
import plotly.express as px
from utils.load_data import load_data

st.set_page_config(page_title="Startup Explorer", layout="wide")

df = load_data()

st.title("🔍 Startup Explorer")

startup = st.selectbox(
    "Select Startup",
    sorted(df["Startup Name"].unique())
)

selected = df[
    df["Startup Name"] == startup
]

st.subheader("Startup Details")

st.dataframe(
    selected,
    use_container_width=True
)

st.divider()

if len(selected) > 0:

    startup_data = selected.iloc[0]

    metrics = {
        "Funding":
            startup_data["Funding Amount (M USD)"],
        "Revenue":
            startup_data["Revenue (M USD)"],
        "Valuation":
            startup_data["Valuation (M USD)"],
        "Market Share":
            startup_data["Market Share (%)"]
    }

    metric_df = {
        "Metric": list(metrics.keys()),
        "Value": list(metrics.values())
    }

    fig = px.bar(
        metric_df,
        x="Metric",
        y="Value",
        title=f"{startup} Performance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.divider()

st.subheader("Search Startups")

keyword = st.text_input(
    "Enter Startup Name"
)

if keyword:

    result = df[
        df["Startup Name"]
        .str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

    st.dataframe(
        result,
        use_container_width=True
    )
