import plotly.graph_objects as go
from plotly.subplots import make_subplots


def price_chart(data):

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_heights=[0.75, 0.25]
    )

    # Candlestick Chart
    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            name="NIFTY",
            increasing_line_color="#00E676",
            increasing_fillcolor="#00E676",
            decreasing_line_color="#FF5252",
            decreasing_fillcolor="#FF5252"
        ),
        row=1,
        col=1
    )

    # MA20
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MA20"],
            mode="lines",
            name="MA20",
            line=dict(color="#FFD54F", width=2)
        ),
        row=1,
        col=1
    )

    # MA50
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MA50"],
            mode="lines",
            name="MA50",
            line=dict(color="#40C4FF", width=2)
        ),
        row=1,
        col=1
    )

    # BUY Signals
    if "Buy_Signal" in data.columns:
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["Buy_Signal"],
                mode="markers",
                name="BUY",
                marker=dict(
                    symbol="triangle-up",
                    color="lime",
                    size=12
                )
            ),
            row=1,
            col=1
        )

    # SELL Signals
    if "Sell_Signal" in data.columns:
        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["Sell_Signal"],
                mode="markers",
                name="SELL",
                marker=dict(
                    symbol="triangle-down",
                    color="red",
                    size=12
                )
            ),
            row=1,
            col=1
        )

    # Volume
    fig.add_trace(
        go.Bar(
            x=data.index,
            y=data["Volume"],
            name="Volume",
            marker_color="#5DADE2"
        ),
        row=2,
        col=1
    )    # ---------------------------------------
    # Regime Background Shading
    # ---------------------------------------

    if "Regime" in data.columns:

        colors = {
            "Strong Bull": "rgba(0,180,0,0.25)",
            "Bull": "rgba(100,255,100,0.20)",
            "Neutral": "rgba(255,255,0,0.15)",
            "Bear": "rgba(255,140,0,0.20)",
            "Strong Bear": "rgba(255,0,0,0.25)"
        }

        regime_data = data.dropna(subset=["Regime"])

        if not regime_data.empty:

            previous_regime = regime_data.iloc[0]["Regime"]
            start_date = regime_data.index[0]

            for date, row in regime_data.iloc[1:].iterrows():

                current_regime = row["Regime"]

                if current_regime != previous_regime:

                    fig.add_vrect(
                        x0=start_date,
                        x1=date,
                        fillcolor=colors.get(
                            previous_regime,
                            "rgba(150,150,150,0.15)"
                        ),
                        opacity=0.4,
                        layer="below",
                        line_width=0,
                        row=1,
                        col=1
                    )

                    previous_regime = current_regime
                    start_date = date

            fig.add_vrect(
                x0=start_date,
                x1=regime_data.index[-1],
                fillcolor=colors.get(
                    previous_regime,
                    "rgba(150,150,150,0.15)"
                ),
                opacity=0.4,
                layer="below",
                line_width=0,
                row=1,
                col=1
            )

    fig.update_layout(
        title="📈 NIFTY 50 Market Analysis",
        template="plotly_dark",
        height=750,
       hovermode="x unified",
       dragmode=False,
       xaxis=dict(
       fixedrange=True
),
       yaxis=dict(
       fixedrange=True
),
        xaxis_rangeslider_visible=False,
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font=dict(
            color="white",
            size=14
        ),
        legend=dict(
            orientation="h",
            y=1.02,
            x=0
        ),
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    return fig


def rsi_chart(data):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["RSI"],
            mode="lines",
            name="RSI",
            line=dict(
                color="#00E5FF",
                width=2
            )
        )
    )

    fig.add_hline(y=70, line_dash="dash", line_color="red")
    fig.add_hline(y=30, line_dash="dash", line_color="green")

    fig.update_layout(
        title="Relative Strength Index (RSI)",
        template="plotly_dark",
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig


def volatility_chart(data):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Volatility"],
            mode="lines",
            name="Volatility",
            line=dict(
                color="#FF9800",
                width=2
            )
        )
    )

    fig.update_layout(
        title="20-Day Rolling Volatility",
        template="plotly_dark",
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig 


def portfolio_chart(data):
    import plotly.graph_objects as go

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Portfolio_Value"],
            mode="lines",
            name="Portfolio Value",
            line=dict(width=3)
        )
    )

    fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["BuyHold_Value"],
        mode="lines",
        name="Buy & Hold",
        line=dict(width=3, dash="dash")
    )
)

    fig.update_layout(
        title="Portfolio Growth",
        xaxis_title="Date",
        yaxis_title="Portfolio Value (₹)",
        template="plotly_dark",
        height=400
    )

    return fig