import streamlit as st
import pandas as pd

from data_loader import load_market_data
from indicators import calculate_indicators
from regime_detector import detect_market_regime
from bayesian_engine import bayesian_update
from recommendation import generate_recommendation
from portfolio import simulate_portfolio
from particle_filter import particle_filter
from conformal import conformal_prediction
from ensemble import ensemble_prediction
from allocation import allocation_guidance
from report_generator import generate_pdf
from var_model import run_var_model

from charts import (
    price_chart,
    rsi_chart,
    volatility_chart,
    portfolio_chart
)

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="QuantVision AI",
    page_icon="📈",
    layout="wide"
)

st.title("📈 QuantVision AI")
st.subheader("Bayesian Regime Detection Engine for Indian Equity Markets")

st.markdown("---")

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

with st.spinner("Loading live market data..."):

    data = load_market_data("^NSEI")

    if data is None or len(data) < 100:
        st.error("Unable to download sufficient market data.")
        st.stop()

    # Technical Indicators
    data = calculate_indicators(data)
   

    # Remove rows with NaN values created by rolling indicators
    data = data.dropna().copy()

    # AI Pipeline
    data = detect_market_regime(data)

    # New Location
    var_forecast = run_var_model(data)
    
    data = bayesian_update(data)
    data = particle_filter(data)
    data = conformal_prediction(data)
    data = ensemble_prediction(data)
    data = allocation_guidance(data)
    data = generate_recommendation(data)

    # Portfolio Simulation
    data, portfolio_summary = simulate_portfolio(data)


#Latest rows
latest = data.iloc[-1]

st.write(data[[
    "Close",
    "Recommendation",
    "Portfolio_Value"
]].tail(20))

previous = data.iloc[-2]
# --------------------------------------------------
# MARKET OVERVIEW
# --------------------------------------------------

st.header("📊 Market Overview")

current_price = latest["Close"]
previous_price = previous["Close"]

daily_change = (
    (current_price - previous_price)
    / previous_price
) * 100

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Current NIFTY",
        f"{current_price:.2f}"
    )

with m2:
    st.metric(
        "Daily Change",
        f"{daily_change:.2f}%"
    )

with m3:
    st.metric(
        "Volume",
        f"{int(latest['Volume']):,}"
    )

st.markdown("---")

# --------------------------------------------------
# MARKET HEALTH
# --------------------------------------------------

st.header("🧠 Market Health")

latest_rsi = latest["RSI"]
latest_vol = latest["Volatility"]

trend = (
    "🟢 Bullish"
    if current_price > latest["MA20"]
    else "🔴 Bearish"
)

if latest_rsi > 70:
    momentum = "Overbought"
elif latest_rsi < 30:
    momentum = "Oversold"
else:
    momentum = "Neutral"

if latest_vol < 1:
    risk = "Low"
elif latest_vol < 2:
    risk = "Medium"
else:
    risk = "High"

h1, h2, h3 = st.columns(3)

with h1:
    st.metric("Trend", trend)

with h2:
    st.metric("Momentum", momentum)

with h3:
    st.metric("Risk", risk)

    st.subheader("📈 VAR Forecast")

if var_forecast is not None:
    st.dataframe(var_forecast)
else:
    st.info("Not enough historical data to generate a VAR forecast.")

st.markdown("---")

# --------------------------------------------------
# AI MARKET REGIME
# --------------------------------------------------

st.header("🤖 AI Market Regime")

regime = latest["Regime"]
confidence = float(latest["Confidence"])
posterior = float(latest["Posterior Confidence"])
uncertainty = float(latest["Uncertainty"])
particle = float(latest["Particle Confidence"])
ensemble = float(latest["Ensemble Score"])

recommendation = latest["Recommendation"]

r1, r2, r3, r4, r5, r6 = st.columns(6)

with r1:
    st.metric("Regime", regime)

with r2:
    st.metric("HMM", f"{confidence:.2%}")

with r3:
    st.metric("Bayesian", f"{posterior:.2%}")

with r4:
    st.metric("Particle", f"{particle:.2%}")

with r5:
    st.metric("Uncertainty", f"{uncertainty:.2%}")

with r6:
    st.metric(
        "Ensemble",
        f"{ensemble:.2%}"
    )    

lower = latest["Confidence Lower"]
upper = latest["Confidence Upper"]

st.info(
    f"📊 Confidence Interval: {lower:.1%} – {upper:.1%}"
)

st.subheader("💰 AI Allocation Guidance")

a1, a2 = st.columns(2)

with a1:
    st.metric(
        "Equity",
        f"{int(latest['Equity Allocation'])}%"
    )

with a2:
    st.metric(
        "Cash",
        f"{int(latest['Cash Allocation'])}%"
    )


st.progress(max(0.0, min(1.0, confidence)))

st.success(f"Recommendation: {recommendation}")

st.info(latest["Reason"])

st.markdown("---")
# --------------------------------------------------
# PORTFOLIO PERFORMANCE
# --------------------------------------------------

st.header("💼 Portfolio Performance")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Final Portfolio Value",
        f"₹{portfolio_summary['Final Portfolio Value']:,.2f}"
    )

with c2:
    st.metric(
        "Total Return",
        f"{portfolio_summary['Total Return (%)']:.2f}%"
    )

with c3:
    st.metric(
        "Sharpe Ratio",
        f"{portfolio_summary['Sharpe Ratio']:.2f}"
    )

c4, c5, c6 = st.columns(3)

with c4:
    st.metric(
        "Profit / Loss",
        f"₹{portfolio_summary['Profit/Loss']:,.2f}"
    )

with c5:
    st.metric(
        "Max Drawdown",
        f"{portfolio_summary['Max Drawdown (%)']:.2f}%"
    )

with c6:
    st.metric(
        "Trades",
        portfolio_summary["Number of Trades"]
    )
    st.markdown("### 📈 Advanced Performance Metrics")

    m1, m2, m3 = st.columns(3)

    with m1:
     st.metric(
        "CAGR",
        f"{portfolio_summary['CAGR (%)']:.2f}%"
    )

    with m2:
     st.metric(
        "Win Rate",
        f"{portfolio_summary['Win Rate (%)']:.2f}%"
    )

    with m3:
     profit_factor = portfolio_summary["Profit Factor"]

    if profit_factor == float("inf"):
        st.metric("Profit Factor", "∞")
    else:
        st.metric(
            "Profit Factor",
            f"{profit_factor:.2f}"
        )

    m4, m5 = st.columns(2)

    with m4:
     st.metric(
        "Sortino Ratio",
        f"{portfolio_summary['Sortino Ratio']:.2f}"
    )

    with m5:
     st.metric(
        "Calmar Ratio",
        f"{portfolio_summary['Calmar Ratio']:.2f}"
    )

    st.markdown("---")

# --------------------------------------------------
# CHARTS
# --------------------------------------------------

st.header("📈 Interactive Market Dashboard")

st.plotly_chart(
    price_chart(data),
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        rsi_chart(data),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        volatility_chart(data),
        use_container_width=True
    )

st.plotly_chart(
    portfolio_chart(data),
    use_container_width=True
)

# --------------------------------------------------
# TRADE HISTORY
# --------------------------------------------------

st.header("📋 Trade History")

trade_history = portfolio_summary["Trade History"]

if not trade_history.empty:
    st.dataframe(trade_history, use_container_width=True)
else:
    st.info("No trades executed.")

st.markdown("---")


# --------------------------------------------------
# EXPORT RESULTS
# --------------------------------------------------

st.header("📥 Export Results")

analysis_csv = data.to_csv(index=True).encode("utf-8")

st.download_button(
    label="⬇️ Download Full Analysis (CSV)",
    data=analysis_csv,
    file_name="QuantVision_AI_Analysis.csv",
    mime="text/csv",
)

trade_csv = trade_history.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Trade History (CSV)",
    data=trade_csv,
    file_name="Trade_History.csv",
    mime="text/csv",
)

st.markdown("---")

# --------------------------------------------------
# PDF REPORT
# --------------------------------------------------

st.header("📄 Performance Report")

pdf_file = generate_pdf(portfolio_summary)

with open(pdf_file, "rb") as file:
    st.download_button(
        label="📄 Download Performance Report (PDF)",
        data=file,
        file_name="QuantVision_Report.pdf",
        mime="application/pdf",
    )

st.markdown("---")


# --------------------------------------------------
# LATEST MARKET DATA
# --------------------------------------------------

st.header("📄 Latest Market Data")

st.dataframe(data.tail(20), use_container_width=True)