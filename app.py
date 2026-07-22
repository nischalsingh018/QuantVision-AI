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
from bayesian_lstm import bayesian_lstm_prediction
from foundation_model import foundation_forecast

from charts import (
    price_chart,
    rsi_chart,
    volatility_chart,
    portfolio_chart,
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

    # Remove rolling NaN rows
    data = data.dropna().copy()

    # -----------------------------
    # AI Pipeline
    # -----------------------------

    data = detect_market_regime(data)

    var_forecast = run_var_model(data)

    data = bayesian_lstm_prediction(data)

    data = foundation_forecast(data)

    data = bayesian_update(data)

    data = particle_filter(data)

    data = conformal_prediction(data)

    data = ensemble_prediction(data)

    data = allocation_guidance(data)

    data = generate_recommendation(data)

    # Portfolio Backtest
    data, portfolio_summary = simulate_portfolio(data)

# Latest Market Row
latest = data.iloc[-1]
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
    st.dataframe(var_forecast, use_container_width=True)
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
foundation = float(latest["Foundation Score"])

recommendation = latest["Recommendation"]

r1, r2, r3, r4, r5, r6, r7 = st.columns(7)

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
    st.metric("Ensemble", f"{ensemble:.2%}")

with r7:
    st.metric("Foundation", f"{foundation:.2%}")

# --------------------------------------------------
# Confidence Interval
# --------------------------------------------------

lower = latest["Confidence Lower"]
upper = latest["Confidence Upper"]

st.info(
    f"📊 Confidence Interval: {lower:.1%} – {upper:.1%}"
)

# --------------------------------------------------
# Regime Probability Distribution
# --------------------------------------------------

st.subheader("📊 Regime Probability Distribution")

regime_probs = pd.DataFrame({
    "Market Regime": [
        "Risk-Off",
        "Post-Shock",
        "Transitional",
        "Late-Cycle",
        "Risk-On"
    ],
    "Probability": [
        latest["State_0_Prob"],
        latest["State_1_Prob"],
        latest["State_2_Prob"],
        latest["State_3_Prob"],
        latest["State_4_Prob"]
    ]
})

st.dataframe(
    regime_probs.style.format({"Probability": "{:.2%}"}),
    use_container_width=True
)

st.bar_chart(
    regime_probs.set_index("Market Regime")
)

# --------------------------------------------------
# AI Allocation Guidance
# --------------------------------------------------

st.subheader("💰 AI Allocation Guidance")

a1, a2 = st.columns(2)

with a1:
    st.metric(
        "Equity Allocation",
        f"{int(latest['Equity Allocation'])}%"
    )

with a2:
    st.metric(
        "Cash Allocation",
        f"{int(latest['Cash Allocation'])}%"
    )

# --------------------------------------------------
# Confidence Gauge
# --------------------------------------------------

st.progress(
    max(0.0, min(1.0, confidence))
)

# --------------------------------------------------
# Recommendation
# --------------------------------------------------

st.success(f"Recommendation: {recommendation}")

st.info(latest["Reason"])

st.markdown("---")
# --------------------------------------------------
# PORTFOLIO PERFORMANCE
# --------------------------------------------------

st.header("💼 Portfolio Performance")

# -----------------------------
# Primary Metrics
# -----------------------------

p1, p2, p3 = st.columns(3)

with p1:
    st.metric(
        "Final Portfolio Value",
        f"₹{portfolio_summary['Final Portfolio Value']:,.2f}"
    )

with p2:
    st.metric(
        "Total Return",
        f"{portfolio_summary['Total Return (%)']:.2f}%"
    )

with p3:
    st.metric(
        "Profit / Loss",
        f"₹{portfolio_summary['Profit/Loss']:,.2f}"
    )

st.markdown("---")

# -----------------------------
# Risk Metrics
# -----------------------------

r1, r2, r3 = st.columns(3)

with r1:
    st.metric(
        "Sharpe Ratio",
        f"{portfolio_summary['Sharpe Ratio']:.2f}"
    )

with r2:
    st.metric(
        "Sortino Ratio",
        f"{portfolio_summary['Sortino Ratio']:.2f}"
    )

with r3:
    st.metric(
        "Calmar Ratio",
        f"{portfolio_summary['Calmar Ratio']:.2f}"
    )

st.markdown("---")

# -----------------------------
# Strategy Metrics
# -----------------------------

s1, s2, s3 = st.columns(3)

with s1:
    st.metric(
        "CAGR",
        f"{portfolio_summary['CAGR (%)']:.2f}%"
    )

with s2:
    st.metric(
        "Win Rate",
        f"{portfolio_summary['Win Rate (%)']:.2f}%"
    )

with s3:

    profit_factor = portfolio_summary["Profit Factor"]

    if profit_factor == float("inf"):
        st.metric("Profit Factor", "∞")
    else:
        st.metric(
            "Profit Factor",
            f"{profit_factor:.2f}"
        )

st.markdown("---")

# -----------------------------
# Portfolio Statistics
# -----------------------------

t1, t2 = st.columns(2)

with t1:
    st.metric(
        "Max Drawdown",
        f"{portfolio_summary['Max Drawdown (%)']:.2f}%"
    )

with t2:
    st.metric(
        "Number of Trades",
        portfolio_summary["Number of Trades"]
    )

st.markdown("---")
# --------------------------------------------------
# CHARTS
# --------------------------------------------------

st.header("📈 Interactive Market Dashboard")

# Price Chart
st.subheader("📊 NIFTY Price")

st.plotly_chart(
    price_chart(data),
    use_container_width=True
)

# RSI & Volatility
c1, c2 = st.columns(2)

with c1:
    st.subheader("📉 RSI")
    st.plotly_chart(
        rsi_chart(data),
        use_container_width=True
    )

with c2:
    st.subheader("📊 Volatility")
    st.plotly_chart(
        volatility_chart(data),
        use_container_width=True
    )

# Portfolio Performance
st.subheader("💼 Portfolio Growth")

st.plotly_chart(
    portfolio_chart(data),
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# TRADE HISTORY
# --------------------------------------------------

st.header("📋 Trade History")

trade_history = portfolio_summary["Trade History"]

if len(trade_history) > 0:

    st.success(
        f"Total Executed Trades: {len(trade_history)}"
    )

    st.dataframe(
        trade_history,
        use_container_width=True
    )

else:

    st.warning(
        "No trades executed during the backtest."
    )

st.markdown("---")
# --------------------------------------------------
# EXPORT RESULTS
# --------------------------------------------------

st.header("📥 Export Results")

col1, col2 = st.columns(2)

analysis_csv = data.to_csv(index=True).encode("utf-8")

with col1:
    st.download_button(
        label="⬇️ Download Full Analysis (CSV)",
        data=analysis_csv,
        file_name="QuantVision_AI_Analysis.csv",
        mime="text/csv",
    )

trade_history = portfolio_summary["Trade History"]

trade_csv = trade_history.to_csv(index=False).encode("utf-8")

with col2:
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

st.header("📄 AI Performance Report")

pdf_file = generate_pdf(portfolio_summary)

with open(pdf_file, "rb") as file:

    st.download_button(
        label="📄 Download PDF Report",
        data=file,
        file_name="QuantVision_AI_Report.pdf",
        mime="application/pdf",
    )

st.markdown("---")

# --------------------------------------------------
# LATEST MARKET DATA
# --------------------------------------------------

st.header("📊 Latest Market Data")

display_columns = [
    "Close",
    "Daily Return",
    "RSI",
    "Volatility",
    "Regime",
    "Recommendation",
    "Portfolio_Value"
]

available_columns = [
    col for col in display_columns if col in data.columns
]

st.dataframe(
    data[available_columns].tail(20),
    use_container_width=True
)

st.markdown("---")

# --------------------------------------------------
# PROJECT SUMMARY
# --------------------------------------------------

st.header("📌 AI Model Summary")

summary = pd.DataFrame({
    "Component": [
        "Hidden Markov Model",
        "Bayesian Update",
        "Particle Filter",
        "Bayesian Deep Learning",
        "Foundation Model",
        "Regime Switching VAR",
        "Conformal Prediction",
        "Ensemble Engine",
        "Portfolio Simulator"
    ],
    "Status": [
        "✅ Active",
        "✅ Active",
        "✅ Active",
        "✅ Active",
        "✅ Active",
        "✅ Active",
        "✅ Active",
        "✅ Active",
        "✅ Active"
    ]
})

st.dataframe(
    summary,
    use_container_width=True
)

st.success("✅ QuantVision AI Pipeline Executed Successfully")        