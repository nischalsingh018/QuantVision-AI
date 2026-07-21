import yfinance as yf
import pandas as pd

def load_market_data(symbol="^NSEI", period="1y"):
    """
    Downloads historical market data using Yahoo Finance.
    """

    data = yf.download(
        symbol,
        period=period,
        interval="1d",
        auto_adjust=False,
        progress=False
    )

    # Flatten MultiIndex columns if they exist
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data