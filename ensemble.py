import numpy as np


def ensemble_prediction(data):

    data = data.copy()

    scores = []

    for _, row in data.iterrows():

        hmm = row.get("Confidence", 0.0)
        bayes = row.get("Posterior Confidence", 0.0)
        particle = row.get("Particle Confidence", 0.0)

        # Technical score from RSI
        if row["RSI"] < 30:
            technical = 1.0
        elif row["RSI"] > 70:
            technical = 0.0
        else:
            technical = 0.5

        score = (
            0.35 * hmm +
            0.35 * bayes +
            0.20 * particle +
            0.10 * technical
        )

        scores.append(score)

    data["Ensemble Score"] = scores

    return data