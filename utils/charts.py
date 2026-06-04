
import plotly.express as px
import plotly.graph_objects as go


def funding_by_industry(df):

    industry_funding = (
        df.groupby("Industry")["Funding Amount (M USD)"]
        .sum()
        .reset_index()
        .sort_values(
            by="Funding Amount (M USD)",
            ascending=False
        )
    )

    fig = px.bar(
        industry_funding,
        x="Industry",
        y="Funding Amount (M USD)",
        color="Industry",
        title="Funding by Industry"
    )

    return fig


def valuation_vs_revenue(df):

    fig = px.scatter(
        df,
        x="Revenue (M USD)",
        y="Valuation (M USD)",
        color="Industry",
        size="Funding Amount (M USD)",
        hover_name="Startup Name",
        title="Revenue vs Valuation"
    )

    return fig


def regional_distribution(df):

    region_df = (
        df.groupby("Region")
        .size()
        .reset_index(name="Count")
    )

    fig = px.pie(
        region_df,
        names="Region",
        values="Count",
        title="Startup Distribution by Region"
    )

    return fig


def market_share_analysis(df):

    fig = px.scatter(
        df,
        x="Funding Amount (M USD)",
        y="Market Share (%)",
        color="Region",
        size="Employees",
        hover_name="Startup Name",
        title="Funding vs Market Share"
    )

    return fig


def employee_distribution(df):

    fig = px.histogram(
        df,
        x="Employees",
        nbins=25,
        title="Employee Distribution"
    )

    return fig


def funding_rounds(df):

    round_df = (
        df.groupby("Funding Rounds")
        ["Funding Amount (M USD)"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        round_df,
        x="Funding Rounds",
        y="Funding Amount (M USD)",
        markers=True,
        title="Average Funding by Funding Rounds"
    )

    return fig
