# 📈 QuantVision AI

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20With-Streamlit-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-success)]()
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://quantvision-bayesian-ns.streamlit.app/)

# Bayesian Regime Detection Engine for Indian Equity Markets

QuantVision AI is an AI-powered quantitative finance platform that combines probabilistic machine learning, Bayesian inference, and financial analytics to detect market regimes, estimate uncertainty, forecast market behaviour, simulate portfolio performance, and generate explainable investment recommendations.

The platform integrates multiple AI models into a unified decision-support system designed for quantitative research, equity analysis, and portfolio analytics.

---

# 🎯 Project Objective

The objective of QuantVision AI is to build an intelligent quantitative research platform capable of analysing Indian equity markets using modern statistical learning, Bayesian inference, probabilistic forecasting and portfolio analytics.

The system automatically:

- Downloads live market data
- Calculates technical indicators
- Detects hidden market regimes
- Estimates market uncertainty
- Forecasts market direction
- Generates investment recommendations
- Suggests portfolio allocation
- Simulates portfolio performance
- Produces professional PDF reports
- Provides an interactive analytics dashboard

---

# ⭐ Highlights

- Five-State Market Regime Detection
- Bayesian Probability Updating
- Particle Filtering
- Bayesian Deep Learning
- Foundation AI Layer
- Regime Switching VAR Forecasting
- Conformal Prediction
- Ensemble Learning
- Explainable AI Recommendations
- Portfolio Backtesting
- Buy & Hold Benchmark Comparison
- Interactive Streamlit Dashboard
- Professional PDF Reporting

---

# 📈 AI Architecture

```text
Yahoo Finance
      │
      ▼
Market Data Loader
      │
      ▼
Technical Indicators
      │
      ▼
Hidden Markov Model
      │
      ▼
Bayesian Updating
      │
      ▼
Particle Filter
      │
      ▼
Bayesian Deep Learning
      │
      ▼
Foundation Model
      │
      ▼
Regime Switching VAR
      │
      ▼
Conformal Prediction
      │
      ▼
Ensemble Learning
      │
      ▼
Allocation Engine
      │
      ▼
Recommendation Engine
      │
      ▼
Portfolio Simulator
      │
      ▼
Professional PDF Report
      │
      ▼
Interactive Streamlit Dashboard
```

---
# 🚀 Features

## 📊 Market Data

- Live NIFTY market data using Yahoo Finance
- Automatic historical data download
- Data preprocessing and cleaning
- Missing value handling
- Market statistics generation

---

## 📈 Technical Indicators

The system automatically computes:

- Relative Strength Index (RSI)
- Moving Average (20-Day)
- Moving Average (50-Day)
- Rolling Volatility
- Daily Returns
- Market Momentum
- Trend Detection

---

## 🤖 Artificial Intelligence Pipeline

### Hidden Markov Model (HMM)

- Five-State Market Regime Detection
- Hidden State Probability Estimation
- Regime Confidence Calculation
- Probabilistic State Transition

---

### Bayesian Updating

- Bayesian Posterior Estimation
- Probability Updating
- Confidence Refinement
- Dynamic Belief Adjustment

---

### Particle Filter

- Sequential Bayesian Filtering
- Confidence Smoothing
- Noise Reduction
- Robust State Estimation

---

### Bayesian Deep Learning

- Probabilistic Deep Learning
- Forecast Confidence Estimation
- Predictive Uncertainty Analysis

---

### Foundation AI Layer

- AI Forecast Enhancement
- Market Behaviour Modelling
- Additional Confidence Layer

---

### Regime Switching VAR

- Multi-variable Time Series Forecasting
- Regime Dependent Market Prediction
- Dynamic Market Behaviour Analysis

---

### Conformal Prediction

- Adaptive Confidence Intervals
- Prediction Reliability
- Uncertainty Quantification

---

### Ensemble Learning

The final prediction combines outputs from

- Hidden Markov Model
- Bayesian Updating
- Particle Filter
- Bayesian Deep Learning
- Foundation Model
- Regime Switching VAR
- Technical Indicators

to generate a robust investment decision.

---

# 💼 Investment Decision Engine

The AI generates

- BUY Recommendation
- SELL Recommendation
- HOLD Recommendation
- Portfolio Allocation Guidance
- Prediction Confidence
- Prediction Uncertainty
- Explainable Decision Summary
# 💼 Investment Decision Engine

QuantVision AI converts AI predictions into actionable investment insights.

### Recommendations

- BUY
- STRONG BUY
- HOLD
- SELL
- STRONG SELL

### Decision Factors

Recommendations are generated using:

- Current Market Regime
- Bayesian Posterior Probability
- Hidden Markov Confidence
- Particle Filter Confidence
- Foundation Model Score
- Bayesian Deep Learning Forecast
- Regime Switching VAR Forecast
- Ensemble Confidence
- Prediction Uncertainty
- Technical Indicators

---

# 📊 Portfolio Analytics

The integrated portfolio simulator evaluates the effectiveness of AI-generated recommendations against a traditional Buy & Hold strategy.

### Portfolio Features

- AI Trading Strategy
- Buy & Hold Benchmark
- Portfolio Value Tracking
- Trade Execution History
- Cash Management
- Equity Curve

### Performance Metrics

- Initial Capital
- Final Portfolio Value
- Total Profit
- Total Return (%)
- CAGR
- Sharpe Ratio
- Sortino Ratio
- Calmar Ratio
- Maximum Drawdown
- Win Rate
- Profit Factor
- Number of Trades

---

# 📈 Interactive Dashboard

Built with **Streamlit** and **Plotly**, the dashboard provides an interactive research environment.

### Dashboard Sections

### Market Overview

- Live Market Price
- Daily Return
- Market Trend
- Volume Analysis

### AI Market Intelligence

- Current Market Regime
- Bayesian Confidence
- HMM Confidence
- Particle Filter Confidence
- Foundation Model Score
- Ensemble Confidence
- Prediction Uncertainty

### Visualizations

- Candlestick Chart
- MA20 & MA50
- Buy / Sell Signals
- Regime Background Visualization
- RSI Chart
- Rolling Volatility
- Portfolio Growth
- Buy & Hold Comparison

### Portfolio Analysis

- Portfolio Statistics
- Strategy Performance
- Trade History
- Allocation Guidance
- Recommendation Engine

---

# 📥 Export Features

QuantVision AI supports professional reporting.

### CSV Export

- Latest Market Data
- Portfolio Statistics
- Trade History

### PDF Report

Automatically generates a professional research report including:

- Executive Summary
- Market Summary
- Portfolio Analytics
- Risk Analysis
- AI Components
- Investment Recommendation
- Disclaimer

---

# 📈 Key Results

The completed system provides:

- Five-State Market Regime Detection
- Probabilistic Market Forecasting
- AI Confidence Estimation
- Bayesian Uncertainty Quantification
- Explainable Investment Recommendations
- Portfolio Backtesting
- Buy & Hold Benchmark Comparison
- Interactive Dashboard
- Professional PDF Report Generation

---
# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.12 |
| Dashboard | Streamlit |
| Data Analysis | Pandas, NumPy |
| Machine Learning | hmmlearn, Scikit-learn |
| Deep Learning | PyTorch |
| Statistical Models | Statsmodels |
| Financial Data | Yahoo Finance (yfinance) |
| Visualization | Plotly |
| Reporting | ReportLab |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
QuantVision-AI/

│
├── app.py
├── data_loader.py
├── indicators.py
├── regime_detector.py
├── bayesian_engine.py
├── particle_filter.py
├── bayesian_lstm.py
├── foundation_model.py
├── var_model.py
├── conformal.py
├── ensemble.py
├── allocation.py
├── recommendation.py
├── portfolio.py
├── charts.py
├── report_generator.py
├── requirements.txt
├── README.md
├── run.bat
├── LICENSE
├── .gitignore
│
├── screenshots/
│   ├── dashboard.jpeg
│   ├── portfolio.jpeg
│   ├── trade_history.jpeg
│   └── metrics.jpeg
│
└── assets/
```

---

# ⚙ Installation

## Clone the repository

```bash
git clone https://github.com/nischalsingh018/QuantVision-AI.git
```

Move into the project

```bash
cd QuantVision-AI
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv312
```

Activate it

```bash
venv312\Scripts\activate
```

---

### Linux / macOS

```bash
python3 -m venv venv312

source venv312/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Launch the Dashboard

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

# 📷 Dashboard Preview

## 🏠 Dashboard Overview

![Dashboard](screenshots/dashboard.jpeg)

---

## 📈 Portfolio Performance

![Portfolio](screenshots/portfolio.jpeg)

---

## 📑 Trade History

![Trade History](screenshots/trade_history.jpeg)

---

## 📊 Performance Metrics

![Performance Metrics](screenshots/metrics.jpeg)

---

# 🌐 Live Demo

🚀 **Launch QuantVision AI**

https://quantvision-bayesian-ns.streamlit.app/

---

# 📦 Requirements

Major Python libraries used in this project:

- streamlit
- pandas
- numpy
- yfinance
- plotly
- matplotlib
- hmmlearn
- scikit-learn
- statsmodels
- torch
- transformers
- reportlab

---
# 💡 Skills Demonstrated

This project showcases practical applications of quantitative finance, machine learning, and software engineering.

### Programming

- Python
- Object-Oriented Programming
- Modular Software Design
- Data Processing

---

### Financial Analytics

- Quantitative Finance
- Equity Research
- Financial Modelling
- Portfolio Analytics
- Risk Analysis
- Market Regime Detection

---

### Artificial Intelligence & Machine Learning

- Hidden Markov Models
- Bayesian Statistics
- Bayesian Updating
- Particle Filtering
- Bayesian Deep Learning
- Foundation AI Models
- Regime Switching Models
- Ensemble Learning
- Conformal Prediction
- Time Series Analysis

---

### Data Science

- Data Cleaning
- Feature Engineering
- Statistical Analysis
- Financial Data Visualization
- Probabilistic Forecasting

---

### Software Development

- Streamlit Dashboard Development
- Interactive Data Visualization
- PDF Report Generation
- Git
- GitHub
- Version Control

---

# 🎯 Applications

QuantVision AI can be used for

- Equity Research
- Quantitative Finance
- Financial Analytics
- Portfolio Analysis
- Algorithmic Trading Research
- Market Regime Detection
- Risk Management
- Investment Decision Support
- Financial Data Science Projects

---

# 🔮 Future Roadmap

The following enhancements are planned for future versions:

### AI Enhancements

- Transformer-Based Foundation Models
- Large Language Model Integration
- Reinforcement Learning Portfolio Allocation
- Explainable AI (XAI)
- Multi-Horizon Forecasting

---

### Market Intelligence

- Real-Time Market Streaming
- Live News Sentiment Analysis
- Economic Indicator Integration
- Sector Rotation Analysis
- Multi-Asset Portfolio Support

---

### Portfolio Analytics

- Portfolio Optimization
- Monte Carlo Portfolio Simulation
- Value-at-Risk (VaR)
- Expected Shortfall
- Stress Testing

---

### Deployment

- Docker Deployment
- AWS Cloud Hosting
- REST API
- Mobile Dashboard
- Real-Time Alerts

---

# 📈 Project Highlights

✔ Five-State Market Regime Detection

✔ Bayesian Probability Updating

✔ Particle Filtering

✔ Bayesian Deep Learning

✔ Foundation AI Layer

✔ Regime Switching VAR

✔ Conformal Prediction

✔ Ensemble Learning

✔ Explainable Investment Recommendations

✔ Portfolio Backtesting

✔ Buy & Hold Benchmark Comparison

✔ Interactive Streamlit Dashboard

✔ Professional PDF Report Generation

---

# 👨‍💻 Author

## Nischal Singh

**B.Com (Accounting & Finance)**

Finance • Machine Learning • Quantitative Research • Financial Analytics

### Connect with Me

- GitHub: https://github.com/nischalsingh018
- LinkedIn: https://linkedin.com/in/nischal-singh-00548a38b

---

# 📄 License

This project is released under the **MIT License**.

It may be used for educational, research, internship, and portfolio purposes.

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the developers of:

- Streamlit
- Plotly
- Yahoo Finance
- Pandas
- NumPy
- hmmlearn
- Scikit-learn
- Statsmodels
- PyTorch
- ReportLab

whose libraries made this project possible.

---

# ⭐ Support

If you found this project interesting or useful:

⭐ Star this repository on GitHub

🍴 Fork the project

💡 Share your feedback or suggestions

🤝 Connect with me on LinkedIn

---

# 📌 Final Note

QuantVision AI was developed as a quantitative finance and machine learning project to demonstrate the integration of probabilistic AI models with financial market analysis.

The project showcases how Bayesian inference, Hidden Markov Models, ensemble learning, and portfolio analytics can be combined into a practical decision-support platform for Indian equity markets.

---

## 🚀 Live Application

**Streamlit App**

https://quantvision-bayesian-ns.streamlit.app/

---

**Thank you for visiting the QuantVision AI repository!**