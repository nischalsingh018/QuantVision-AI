import pandas as pd

def calculate_indicators(data):
    """
    Calculate technical indicators for market analysis.
    """

    # Moving Averages
    data["MA20"] = data["Close"].rolling(window=20).mean()
    data["MA50"] = data["Close"].rolling(window=50).mean()

    # Daily Returns
    data["Daily Return"] = data["Close"].pct_change() * 100

    # Rolling Volatility
    data["Volatility"] = data["Daily Return"].rolling(window=20).std()

    # RSI
    delta = data["Close"].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    data["RSI"] = 100 - (100 / (1 + rs))

    return data