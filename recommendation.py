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
        # Risk-On
        # -----------------------------
        if regime == "Risk-On":

            if confidence > 0.85:
                rec = "STRONG BUY"
                reason = "Very high bullish probability with strong confidence."
            else:
                rec = "BUY"
                reason = "Bullish market regime."

        # -----------------------------
        # Late-Cycle
        # -----------------------------
        elif regime == "Late-Cycle":

            rec = "BUY"
            reason = "Positive market trend."

        # -----------------------------
        # Transitional
        # -----------------------------
        elif regime == "Transitional":

            rec = "HOLD"
            reason = "Market is uncertain."

        # -----------------------------
        # Post-Shock
        # -----------------------------
        elif regime == "Post-Shock":

            rec = "SELL"
            reason = "Weak market conditions."

        # -----------------------------
        # Risk-Off
        # -----------------------------
        elif regime == "Risk-Off":

            if confidence > 0.85:
                rec = "STRONG SELL"
                reason = "Very high probability of continued weakness."
            else:
                rec = "SELL"
                reason = "Bearish market regime."

        # -----------------------------
        # Fallback
        # -----------------------------
        else:

            rec = "HOLD"
            reason = "Unknown market regime."

        # -----------------------------
        # High uncertainty adjustment
        # -----------------------------
        if uncertainty > 0.40:
            reason += " High uncertainty—trade cautiously."

        recommendations.append(rec)
        reasons.append(reason)

    data["Recommendation"] = recommendations
    data["Reason"] = reasons

    data["Buy_Signal"] = np.where(
        data["Recommendation"].isin(["BUY", "STRONG BUY"]),
        data["Close"],
        np.nan,
    )

    data["Sell_Signal"] = np.where(
        data["Recommendation"].isin(["SELL", "STRONG SELL"]),
        data["Close"],
        np.nan,
    )

    return data