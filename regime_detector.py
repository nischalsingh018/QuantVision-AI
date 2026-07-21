import numpy as np
import pandas as pd

from hmmlearn.hmm import GaussianHMM
from sklearn.preprocessing import StandardScaler


def detect_market_regime(data):

    # -----------------------------
    # Feature Selection
    # -----------------------------
    features = data[
        [
            "Daily Return",
            "Volatility",
            "RSI"
        ]
    ].dropna()

    # Keep index aligned
    valid_index = features.index

    # -----------------------------
    # Feature Scaling
    # -----------------------------
    scaler = StandardScaler()
    X = scaler.fit_transform(features)

    # -----------------------------
    # Hidden Markov Model
    # -----------------------------
    model = GaussianHMM(
        n_components=5,
        covariance_type="full",
        n_iter=500,
        random_state=42
    )

    model.fit(X)

    hidden_states = model.predict(X)
    probabilities = model.predict_proba(X)

    # -----------------------------
    # Attach Results
    # -----------------------------
    result = data.copy()

    result.loc[valid_index, "State"] = hidden_states

    # Raw confidence
    raw_confidence = probabilities.max(axis=1)

    # Smooth confidence
    smoothed_confidence = 0.60 + (raw_confidence * 0.35)

    # Limit between 60% and 95%
    smoothed_confidence = np.clip(
        smoothed_confidence,
        0.60,
        0.95
    )

    result.loc[
        valid_index,
        "Confidence"
    ] = smoothed_confidence

    # Save state probabilities
    for i in range(5):
        result.loc[
            valid_index,
            f"State_{i}_Prob"
        ] = probabilities[:, i]

    # -----------------------------
    # Determine Market Regimes
    # -----------------------------
    state_returns = {}

    for state in range(5):

        idx = hidden_states == state

        if idx.sum() == 0:
            state_returns[state] = -999
        else:
            state_returns[state] = features.loc[idx, "Daily Return"].mean()

    ordered = sorted(
        state_returns,
        key=state_returns.get
    )

    mapping = {
        ordered[0]: "Strong Bear",
        ordered[1]: "Bear",
        ordered[2]: "Neutral",
        ordered[3]: "Bull",
        ordered[4]: "Strong Bull",
    }

    result["Regime"] = result["State"].map(mapping)

    return result