import streamlit as st
from utils.load_data import load_data
from utils.charts import (
    funding_by_industry,
    valuation_vs_revenue,
    regional_distribution
)

# Page Configuration
st.set_page_config(
    page_title="🚀 Startup Analytics Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Data
df = load_data()

# Header
st.title("🚀 Startup Analytics Dashboard")
st.markdown(
    """
    Welcome to the Startup Intelligence Platform.
    
    Analyze startup funding, valuation, revenue,
    profitability, and regional trends using
    interactive visualizations.
    """
)

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.success(
    """
    Select a page from the sidebar:
    
    • Overview
    
    • Funding Analytics
    
    • Industry Insights
    
    • Regional Analysis
    
    • Startup Explorer
    """
)

# KPI Cards
st.subheader("📊 Executive Summary")

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

# Charts
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

st.info(
    """
    Use the pages menu on the left to explore:
    
    ✅ Funding Analytics
    
    ✅ Industry Insights
    
    ✅ Regional Analysis
    
    ✅ Startup Explorer
    """
)
