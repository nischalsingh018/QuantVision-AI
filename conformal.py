import numpy as np


def conformal_prediction(data):

    data = data.copy()

    if "Posterior Confidence" not in data.columns:
        return data

    lower = []
    upper = []

    for _, row in data.iterrows():

        confidence = row["Posterior Confidence"]
        uncertainty = row.get("Uncertainty", 0.2)

        if np.isnan(confidence):
            lower.append(np.nan)
            upper.append(np.nan)
            continue

        # Adaptive margin
        margin = 0.03 + (0.20 * uncertainty)

        confidence_lower = max(0.0, confidence - margin)
        confidence_upper = min(1.0, confidence + margin)

        lower.append(confidence_lower)
        upper.append(confidence_upper)

    data["Confidence Lower"] = lower
    data["Confidence Upper"] = upper

    return data