import pandas as pd
import numpy as np


def generate_recommendation(data):

    data = data.copy()

    recommendations = []
    reasons = []

    for _, row in data.iterrows():

        regime = row["Regime"]

        confidence = row.get("Posterior Confidence", 0.0)
        uncertainty = row.get("Uncertainty", 1.0)

        if pd.isna(confidence):
            confidence = 0.0

        if pd.isna(uncertainty):
            uncertainty = 1.0

        # -----------------------------
        # Strong Bull
        # -----------------------------
        if regime == "Strong Bull":

            if confidence > 0.85:

                rec = "STRONG BUY"
                reason = "Very high bullish probability with strong confidence."

            else:

                rec = "BUY"
                reason = "Bullish regime detected."

        # -----------------------------
        # Bull
        # -----------------------------
        elif regime == "Bull":

            rec = "BUY"
            reason = "Positive market trend."

        # -----------------------------
        # Neutral
        # -----------------------------
        elif regime == "Neutral":

            rec = "HOLD"
            reason = "Market is uncertain."

        # -----------------------------
        # Bear
        # -----------------------------
        elif regime == "Bear":

            rec = "SELL"
            reason = "Bearish trend detected."

        # -----------------------------
        # Strong Bear
        # -----------------------------
        else:

            if confidence > 0.85:

                rec = "STRONG SELL"
                reason = "Very high probability of continued weakness."

            else:

                rec = "SELL"
                reason = "Bearish conditions."

        # -----------------------------
        # High uncertainty adjustment
        # -----------------------------
        if uncertainty > 0.40:

            reason += " High uncertainty—trade cautiously."

        recommendations.append(rec)
        reasons.append(reason)

    import numpy as np  # Add this at the top of recommendation.py if it's not already there

    data["Recommendation"] = recommendations
    data["Reason"] = reasons

     # Buy markers
    data["Buy_Signal"] = np.where(
    data["Recommendation"].isin(["BUY", "STRONG BUY"]),
    data["Close"],
    np.nan,
)

     # Sell markers
    data["Sell_Signal"] = np.where(
    data["Recommendation"].isin(["SELL", "STRONG SELL"]),
    data["Close"],
    np.nan,
)

    return data