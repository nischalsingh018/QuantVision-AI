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

    # ==================================================
    # Candlestick Chart
    # ==================================================

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

    # ==================================================
    # Moving Averages
    # ==================================================

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MA20"],
            mode="lines",
            name="MA20",
            line=dict(
                color="#FFD54F",
                width=2
            )
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MA50"],
            mode="lines",
            name="MA50",
            line=dict(
                color="#40C4FF",
                width=2
            )
        ),
        row=1,
        col=1
    )

    # ==================================================
    # Latest Price
    # ==================================================

    fig.add_trace(
        go.Scatter(
            x=[data.index[-1]],
            y=[data["Close"].iloc[-1]],
            mode="markers+text",
            text=[f"{data['Close'].iloc[-1]:.2f}"],
            textposition="top center",
            marker=dict(
                size=12,
                color="cyan"
            ),
            name="Latest Price"
        ),
        row=1,
        col=1
    )

    # ==================================================
    # BUY Signals
    # ==================================================

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
                    size=13,
                    line=dict(
                        color="white",
                        width=1
                    )
                )
            ),
            row=1,
            col=1
        )

    # ==================================================
    # SELL Signals
    # ==================================================

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
                    size=13,
                    line=dict(
                        color="white",
                        width=1
                    )
                )
            ),
            row=1,
            col=1
        )

    # ==================================================
    # Volume
    # ==================================================

    fig.add_trace(
        go.Bar(
            x=data.index,
            y=data["Volume"],
            name="Volume",
            marker_color="#5DADE2"
        ),
        row=2,
        col=1
    )

    # ==================================================
    # Regime Background
    # ==================================================

    if "Regime" in data.columns:

        colors = {
            "Risk-On": "rgba(0,180,0,0.25)",
            "Late-Cycle": "rgba(100,255,100,0.20)",
            "Transitional": "rgba(255,255,0,0.15)",
            "Post-Shock": "rgba(255,140,0,0.20)",
            "Risk-Off": "rgba(255,0,0,0.25)"
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
                        opacity=0.35,
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
                opacity=0.35,
                layer="below",
                line_width=0,
                row=1,
                col=1
            )

    # ==================================================
    # Layout
    # ==================================================

    fig.update_layout(
        title="📈 NIFTY 50 Market Analysis",
        template="plotly_dark",
        height=760,
        hovermode="x unified",
        dragmode=False,
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

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.08)"
    )

    fig.update_xaxes(
        showgrid=False
    )

    return fig
def rsi_chart(data):

    fig = go.Figure()

    # RSI Line
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["RSI"],
            mode="lines",
            name="RSI",
            line=dict(
                color="#00E5FF",
                width=3
            )
        )
    )

    # Overbought
    fig.add_hline(
        y=70,
        line_dash="dash",
        line_color="red",
        annotation_text="Overbought (70)"
    )

    # Oversold
    fig.add_hline(
        y=30,
        line_dash="dash",
        line_color="green",
        annotation_text="Oversold (30)"
    )

    # Neutral
    fig.add_hline(
        y=50,
        line_dash="dot",
        line_color="gray",
        annotation_text="Neutral"
    )

    # Shade Overbought Zone
    fig.add_hrect(
        y0=70,
        y1=100,
        fillcolor="rgba(255,0,0,0.08)",
        line_width=0
    )

    # Shade Oversold Zone
    fig.add_hrect(
        y0=0,
        y1=30,
        fillcolor="rgba(0,255,0,0.08)",
        line_width=0
    )

    fig.update_layout(
        title="📊 Relative Strength Index (RSI)",
        template="plotly_dark",
        height=380,
        hovermode="x unified",
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font=dict(
            color="white",
            size=13
        ),
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    fig.update_yaxes(
        range=[0, 100],
        showgrid=True,
        gridcolor="rgba(255,255,255,0.08)"
    )

    fig.update_xaxes(
        showgrid=False
    )

    return fig
def volatility_chart(data):

    fig = go.Figure()

    # ==================================================
    # Volatility Line
    # ==================================================

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Volatility"],
            mode="lines",
            name="20-Day Volatility",
            line=dict(
                color="#FF9800",
                width=3
            ),
            fill="tozeroy",
            fillcolor="rgba(255,152,0,0.10)"
        )
    )

    # ==================================================
    # Average Volatility
    # ==================================================

    avg_volatility = data["Volatility"].mean()

    fig.add_hline(
        y=avg_volatility,
        line_dash="dash",
        line_color="cyan",
        annotation_text=f"Average ({avg_volatility:.2%})"
    )

    # ==================================================
    # Highest Volatility
    # ==================================================

    max_idx = data["Volatility"].idxmax()

    fig.add_trace(
        go.Scatter(
            x=[max_idx],
            y=[data.loc[max_idx, "Volatility"]],
            mode="markers+text",
            text=["Peak"],
            textposition="top center",
            marker=dict(
                size=12,
                color="red"
            ),
            name="Highest Volatility"
        )
    )

    # ==================================================
    # Latest Volatility
    # ==================================================

    latest_vol = data["Volatility"].iloc[-1]

    fig.add_annotation(
        x=data.index[-1],
        y=latest_vol,
        text=f"{latest_vol:.2%}",
        showarrow=True,
        arrowhead=2,
        bgcolor="rgba(0,0,0,0.7)",
        bordercolor="white",
        font=dict(color="white")
    )

    # ==================================================
    # Layout
    # ==================================================

    fig.update_layout(
        title="📉 20-Day Rolling Volatility",
        template="plotly_dark",
        height=380,
        hovermode="x unified",
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font=dict(
            color="white",
            size=13
        ),
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),
        legend=dict(
            orientation="h"
        )
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.08)"
    )

    fig.update_xaxes(
        showgrid=False
    )

    return fig
def portfolio_chart(data):

    fig = go.Figure()

    # ==================================================
    # Portfolio Value
    # ==================================================

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Portfolio_Value"],
            mode="lines",
            name="QuantVision AI Portfolio",
            line=dict(
                color="#00E676",
                width=3
            ),
            fill="tozeroy",
            fillcolor="rgba(0,230,118,0.10)"
        )
    )

    # ==================================================
    # Buy & Hold Benchmark
    # ==================================================

    if "BuyHold_Value" in data.columns:

        fig.add_trace(
            go.Scatter(
                x=data.index,
                y=data["BuyHold_Value"],
                mode="lines",
                name="Buy & Hold",
                line=dict(
                    color="#40C4FF",
                    width=3,
                    dash="dash"
                )
            )
        )

    # ==================================================
    # Final Portfolio Value
    # ==================================================

    final_value = data["Portfolio_Value"].iloc[-1]

    fig.add_trace(
        go.Scatter(
            x=[data.index[-1]],
            y=[final_value],
            mode="markers+text",
            text=[f"₹{final_value:,.0f}"],
            textposition="top center",
            marker=dict(
                size=12,
                color="#00E676"
            ),
            name="Final Portfolio"
        )
    )

    # ==================================================
    # Final Benchmark Value
    # ==================================================

    if "BuyHold_Value" in data.columns:

        benchmark_value = data["BuyHold_Value"].iloc[-1]

        fig.add_trace(
            go.Scatter(
                x=[data.index[-1]],
                y=[benchmark_value],
                mode="markers+text",
                text=[f"₹{benchmark_value:,.0f}"],
                textposition="bottom center",
                marker=dict(
                    size=12,
                    color="#40C4FF"
                ),
                name="Final Buy & Hold"
            )
        )

        # Performance Difference

        difference = final_value - benchmark_value

        if difference >= 0:

            annotation = (
                f"<b>Outperformed</b><br>"
                f"₹{difference:,.0f}"
            )

            bgcolor = "rgba(0,180,0,0.30)"

        else:

            annotation = (
                f"<b>Underperformed</b><br>"
                f"₹{abs(difference):,.0f}"
            )

            bgcolor = "rgba(255,0,0,0.30)"

        fig.add_annotation(
            x=data.index[-1],
            y=max(final_value, benchmark_value),
            text=annotation,
            showarrow=True,
            arrowhead=2,
            bgcolor=bgcolor,
            bordercolor="white",
            font=dict(color="white")
        )

    # ==================================================
    # Layout
    # ==================================================

    fig.update_layout(
        title="💼 Portfolio Performance vs Buy & Hold",
        template="plotly_dark",
        height=430,
        hovermode="x unified",
        paper_bgcolor="#111111",
        plot_bgcolor="#111111",
        font=dict(
            color="white",
            size=13
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

    fig.update_yaxes(
        title="Portfolio Value (₹)",
        showgrid=True,
        gridcolor="rgba(255,255,255,0.08)"
    )

    fig.update_xaxes(
        title="Date",
        showgrid=False
    )

    return fig
