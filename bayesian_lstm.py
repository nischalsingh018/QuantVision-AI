import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import StandardScaler


def bayesian_lstm_prediction(data):

    """
    Bayesian Deep Learning Module
    Uses Monte Carlo Dropout for uncertainty estimation.
    """

    df = data.copy()

    features = [
        "Daily Return",
        "RSI",
        "Volatility"
    ]

    df = df.dropna()

    X = df[features].values

    y = df["Daily Return"].shift(-1)

    X = X[:-1]
    y = y[:-1]

    scaler = StandardScaler()

    X = scaler.fit_transform(X)

    model = Sequential([
        Dense(64, activation="relu"),
        Dropout(0.30),
        Dense(32, activation="relu"),
        Dropout(0.30),
        Dense(1)
    ])

    model.compile(
        optimizer="adam",
        loss="mse"
    )

    model.fit(
        X,
        y,
        epochs=20,
        verbose=0
    )

    latest = X[-1].reshape(1, -1)

    predictions = []

    # Monte Carlo Dropout
    for _ in range(100):
        pred = model(latest, training=True)
        predictions.append(pred.numpy()[0][0])

    mean_prediction = np.mean(predictions)
    uncertainty = np.std(predictions)

    df.loc[df.index[-1], "DL Prediction"] = mean_prediction
    df.loc[df.index[-1], "DL Uncertainty"] = uncertainty

    return df
