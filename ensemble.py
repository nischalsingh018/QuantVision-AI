import numpy as np
import pandas as pd


def _clip(x):
    return float(np.clip(x, 0.0, 1.0))


def _normalize_var(x):
    """
    Converts forecast return into a probability-like score.
    """
    return _clip(0.5 + np.tanh(x / 2.0) / 2.0)


def ensemble_prediction(data):

    df = data.copy()

    ensemble_score = []
    uncertainty_budget = []
    final_confidence = []

    for _, row in df.iterrows():

        # -----------------------------
        # HMM
        # -----------------------------
        hmm = _clip(row.get("Confidence", 0.50))

        # -----------------------------
        # Bayesian Posterior
        # -----------------------------
        bayes = _clip(row.get("Posterior Confidence", 0.50))

        # -----------------------------
        # Particle Filter
        # -----------------------------
        particle = _clip(row.get("Particle Confidence", 0.50))

        # -----------------------------
        # Bayesian Deep Learning
        # -----------------------------
        dl_conf = _clip(row.get("DL Confidence", 0.50))

        # -----------------------------
        # VAR Forecast
        # -----------------------------
        var_score = _normalize_var(
            row.get("Forecast Return", 0.0)
        )

        # -----------------------------
        # Technical Score
        # -----------------------------
        rsi = row.get("RSI", 50)

        if rsi < 30:
            technical = 1.0
        elif rsi > 70:
            technical = 0.0
        else:
            technical = 0.50

        # ==================================================
        # Evidence Fusion
        # ==================================================

        score = (
            0.25 * hmm +
            0.20 * bayes +
            0.15 * particle +
            0.15 * dl_conf +
            0.15 * var_score +
            0.10 * technical
        )

        score = _clip(score)

        # ==================================================
        # Uncertainty Budget
        # ==================================================

        conformal = row.get("Conformal Width", 0.10)
        dl_uncertainty = row.get("DL Uncertainty", 0.10)

        uncertainty = (
            (1 - hmm) * 0.25 +
            (1 - bayes) * 0.20 +
            (1 - particle) * 0.15 +
            dl_uncertainty * 0.20 +
            conformal * 0.20
        )

        uncertainty = _clip(uncertainty)

        confidence = _clip(1 - uncertainty)

        ensemble_score.append(score)
        uncertainty_budget.append(uncertainty)
        final_confidence.append(confidence)

    df["Ensemble Score"] = ensemble_score
    df["Uncertainty Budget"] = uncertainty_budget
    df["Final Confidence"] = final_confidence

    return df