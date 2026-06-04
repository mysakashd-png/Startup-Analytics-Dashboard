import os
import streamlit as st
from utils.load_data import load_data
from utils.charts import (
    funding_by_industry,
    valuation_vs_revenue,
    regional_distribution
)


# -----------------------------
# Configuration
# -----------------------------
st.set_page_config(
    page_title="Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
div[data-testid="metric-container"] {
    background-color: #262730;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #444;
}

h1 {
    color: #4CAF50;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load Data
# -----------------------------
df = load_data()

# -----------------------------
# Logo Handling
# -----------------------------
logo_path = "assets/vtulogo.png"

# Sidebar
if os.path.exists(logo_path):
    try:
        st.sidebar.image(logo_path, width=180)
    except Exception:
       # st.sidebar.markdown("### 🚀 Startup Analytics Dashboard")

# Sidebar Navigation
st.sidebar.title("Navigation")

st.sidebar.success("""
Select a page from the sidebar:

• Overview

• Funding Analytics

• Industry Insights

• Regional Analysis

• Startup Explorer
""")

st.sidebar.markdown("---")

st.sidebar.info("""
### About

🚀 Startup Analytics Dashboard

Built with:
- Python
- Pandas
- Plotly
- Streamlit

Developer: Akash D
""")

# -----------------------------
# Header Section
# -----------------------------
if os.path.exists(logo_path):
    try:
        col1, col2 = st.columns([1, 5])

        with col1:
            st.image(logo_path, width=120)

        with col2:
            st.title("🚀 Startup Analytics Dashboard")
            st.caption("Startup Intelligence Platform")

    except Exception:
        st.title("🚀 Startup Analytics Dashboard")
        st.caption("Startup Intelligence Platform")

else:
    st.title("🚀 Startup Analytics Dashboard")
    st.caption("Startup Intelligence Platform")

# -----------------------------
# Introduction
# -----------------------------
st.markdown("""
Welcome to the Startup Intelligence Platform.

Analyze startup funding, valuation, revenue,
profitability, and regional trends using
interactive visualizations.
""")

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------
st.subheader("📊 Executive Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Startups",
        f"{len(df):,}"
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

# -----------------------------
# Charts
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        funding_by_industry(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        regional_distribution(df),
        use_container_width=True
    )

st.divider()

st.plotly_chart(
    valuation_vs_revenue(df),
    use_container_width=True
)

st.divider()

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(10),
    use_container_width=True
)

# -----------------------------
# Download Dataset
# -----------------------------
csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Dataset",
    data=csv,
    file_name="startup_data.csv",
    mime="text/csv"
)

st.divider()

# -----------------------------
# Footer
# -----------------------------
st.info("""
Use the pages menu on the left to explore:

✅ Funding Analytics

✅ Industry Insights

✅ Regional Analysis

✅ Startup Explorer
""")
