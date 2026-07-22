import yfinance as yf
import pandas as pd


def load_market_data(symbol="^NSEI", period="1y"):
    """
    Download market data with retry mechanism.
    """

    tickers = [
        symbol,
        "^NSEI",
        "NIFTYBEES.NS",
        "RELIANCE.NS"
    ]

    for ticker in tickers:

        try:

            data = yf.download(
                ticker,
                period=period,
                interval="1d",
                auto_adjust=False,
                progress=False,
                threads=False
            )

            if isinstance(data.columns, pd.MultiIndex):
                data.columns = data.columns.get_level_values(0)

            if not data.empty and len(data) > 100:
                return data

        except Exception:
            continue

    return pd.DataFrame()