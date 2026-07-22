import numpy as np
import pandas as pd

from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler


def bayesian_lstm_prediction(data):
    """
    Bayesian Deep Learning Approximation
    -----------------------------------
    Uses an ensemble of neural networks to estimate
    prediction uncertainty.

    Returns:
        DataFrame with:
            DL Prediction
            DL Uncertainty
    """

    df = data.copy()

    features = [
        "Daily Return",
        "RSI",
        "Volatility"
    ]

    df = df.dropna()

    if len(df) < 30:
        return df

    X = df[features].values
    y = df["Daily Return"].shift(-1)

    X = X[:-1]
    y = y[:-1]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    latest = X[-1].reshape(1, -1)

    predictions = []

    # Train multiple models with different random seeds
    # to estimate prediction uncertainty.
    for seed in range(30):

        model = MLPRegressor(
            hidden_layer_sizes=(64, 32),
            activation="relu",
            solver="adam",
            max_iter=500,
            random_state=seed
        )

        model.fit(X, y)

        pred = model.predict(latest)[0]
        predictions.append(pred)

    mean_prediction = float(np.mean(predictions))
    uncertainty = float(np.std(predictions))

    df.loc[df.index[-1], "DL Prediction"] = mean_prediction
    df.loc[df.index[-1], "DL Uncertainty"] = uncertainty

    return df