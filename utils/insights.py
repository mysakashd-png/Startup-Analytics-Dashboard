def generate_insights(df):

    insights = []

    highest_funding = (
        df.groupby("Industry")
        ["Funding Amount (M USD)"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"🏆 Highest funded industry: {highest_funding}"
    )

    highest_revenue = (
        df.groupby("Industry")
        ["Revenue (M USD)"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"💰 Highest revenue generating industry: {highest_revenue}"
    )

    highest_valuation = (
        df.groupby("Industry")
        ["Valuation (M USD)"]
        .mean()
        .idxmax()
    )

    insights.append(
        f"📈 Highest average valuation: {highest_valuation}"
    )

    profitable_pct = (
        df["Profitable"].mean() * 100
    )

    insights.append(
        f"✅ {profitable_pct:.2f}% startups are profitable"
    )

    top_region = (
        df.groupby("Region")
        ["Funding Amount (M USD)"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"🌍 Region receiving maximum funding: {top_region}"
    )

    avg_market_share = (
        df["Market Share (%)"]
        .mean()
    )

    insights.append(
        f"📊 Average market share: {avg_market_share:.2f}%"
    )

    return insights
