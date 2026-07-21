import pandas as pd
import numpy as np


def simulate_portfolio(data, initial_investment=100000):

    data = data.copy()

    cash = float(initial_investment)
    shares = 0.0
    trades = 0

    portfolio_values = []
    trade_history = []

    # ------------------------
    # Portfolio Simulation
    # ------------------------
    for _, row in data.iterrows():

        price = row["Close"]

        if pd.isna(price) or price <= 0:
            portfolio_values.append(cash)
            continue

        recommendation = str(row["Recommendation"]).strip().upper()

        # BUY
        if recommendation in ["BUY", "STRONG BUY"] and cash > 0:

            shares = cash / price
            cash = 0.0
            trades += 1

            trade_history.append({
                "Date": row.name,
                "Action": "BUY",
                "Price": round(price, 2),
                "Shares": round(shares, 4)
            })

        # SELL
        elif recommendation in ["SELL", "STRONG SELL"] and shares > 0:

            cash = shares * price

            trade_history.append({
                "Date": row.name,
                "Action": "SELL",
                "Price": round(price, 2),
                "Shares": round(shares, 4)
            })

            shares = 0.0
            trades += 1

        portfolio_value = cash + (shares * price)
        portfolio_values.append(portfolio_value)

    # ------------------------
    # Portfolio Series
    # ------------------------
    portfolio_series = pd.Series(
        portfolio_values,
        index=data.index
    )

    data["Portfolio_Value"] = portfolio_series

    # ------------------------
    # Buy & Hold Benchmark
    # ------------------------
    buy_hold_shares = initial_investment / data["Close"].iloc[0]
    data["BuyHold_Value"] = buy_hold_shares * data["Close"]

    # ------------------------
    # Performance Metrics
    # ------------------------
    final_value = float(portfolio_series.iloc[-1])

    profit = final_value - initial_investment

    total_return = (
        profit / initial_investment
    ) * 100

    daily_returns = portfolio_series.pct_change().dropna()

    if len(daily_returns) > 1 and daily_returns.std() > 0:
        sharpe_ratio = (
            daily_returns.mean()
            / daily_returns.std()
        ) * np.sqrt(252)
    else:
        sharpe_ratio = 0.0

    rolling_max = portfolio_series.cummax()

    drawdown = (
        portfolio_series - rolling_max
    ) / rolling_max

    max_drawdown = float(drawdown.min() * 100)

    # ------------------------
    # Advanced Metrics
    # ------------------------
    years = len(portfolio_series) / 252

    if years > 0:
        cagr = (
            (final_value / initial_investment) ** (1 / years) - 1
        ) * 100
    else:
        cagr = 0.0

    downside_returns = daily_returns[daily_returns < 0]

    if len(downside_returns) > 1 and downside_returns.std() > 0:
        sortino_ratio = (
            daily_returns.mean()
            / downside_returns.std()
        ) * np.sqrt(252)
    else:
        sortino_ratio = 0.0

    if max_drawdown != 0:
        calmar_ratio = cagr / abs(max_drawdown)
    else:
        calmar_ratio = 0.0

    # ------------------------
    # Trade Statistics
    # ------------------------
    sell_prices = [
        t["Price"]
        for t in trade_history
        if t["Action"] == "SELL"
    ]

    buy_prices = [
        t["Price"]
        for t in trade_history
        if t["Action"] == "BUY"
    ]

    completed_trades = min(
        len(buy_prices),
        len(sell_prices)
    )

    wins = 0
    gross_profit = 0.0
    gross_loss = 0.0

    for i in range(completed_trades):

        pnl = sell_prices[i] - buy_prices[i]

        if pnl > 0:
            wins += 1
            gross_profit += pnl
        else:
            gross_loss += abs(pnl)

    if completed_trades > 0:
        win_rate = (wins / completed_trades) * 100
    else:
        win_rate = 0.0

    if gross_loss > 0:
        profit_factor = gross_profit / gross_loss
    else:
        profit_factor = float("inf")

    # ------------------------
    # Summary
    # ------------------------
    summary = {
        "Initial Investment": initial_investment,
        "Final Portfolio Value": final_value,
        "Profit/Loss": profit,
        "Total Return (%)": total_return,
        "CAGR (%)": cagr,
        "Win Rate (%)": win_rate,
        "Profit Factor": profit_factor,
        "Sortino Ratio": sortino_ratio,
        "Calmar Ratio": calmar_ratio,
        "Sharpe Ratio": sharpe_ratio,
        "Max Drawdown (%)": max_drawdown,
        "Number of Trades": trades,
        "Trade History": pd.DataFrame(trade_history)
    }

    return data, summary