import pandas as pd
from statsmodels.tsa.api import VAR


def run_var_model(data):

    """
    Regime Switching VAR

    One VAR model is trained
    for each Hidden Markov State.
    """

    features = [
        "Daily Return",
        "RSI",
        "Volatility",
        "State"
    ]

    df = data[features].dropna().copy()

    forecasts = {}

    # --------------------------
    # Train one VAR per regime
    # --------------------------

    for state in sorted(df["State"].unique()):

        regime_data = df[df["State"] == state]

        regime_data = regime_data.drop(columns="State")

        if len(regime_data) < 25:
            continue

        try:

            model = VAR(regime_data)

            results = model.fit(2)

            prediction = results.forecast(
                regime_data.values[-2:],
                steps=1
            )

            forecasts[int(state)] = prediction[0]

        except:

            continue

    # --------------------------
    # Current State
    # --------------------------

    current_state = int(df.iloc[-1]["State"])

    if current_state not in forecasts:
        return None

    prediction = forecasts[current_state]

    forecast_df = pd.DataFrame({

        "Current State":[current_state],

        "Forecast Return":[prediction[0]],

        "Forecast RSI":[prediction[1]],

        "Forecast Volatility":[prediction[2]]

    })

    return forecast_df