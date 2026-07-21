import numpy as np


def bayesian_update(data):

    data = data.copy()

    # Uniform prior
    prior = np.ones(5) / 5

    posterior_list = []
    uncertainty_list = []

    for _, row in data.iterrows():

        likelihood = np.array([
            row.get("State_0_Prob", 0.0),
            row.get("State_1_Prob", 0.0),
            row.get("State_2_Prob", 0.0),
            row.get("State_3_Prob", 0.0),
            row.get("State_4_Prob", 0.0)
        ], dtype=float)

        # Avoid exact zeros
        likelihood = np.clip(likelihood, 1e-6, 1.0)

        # Bayesian update
        posterior = likelihood * prior
        posterior /= posterior.sum()

        # Smooth posterior (80% posterior + 20% prior)
        posterior = 0.8 * posterior + 0.2 * prior
        posterior /= posterior.sum()

        posterior_list.append(posterior)

        # Shannon entropy
        entropy = -np.sum(posterior * np.log(posterior))
        max_entropy = np.log(len(posterior))

        uncertainty = entropy / max_entropy
        uncertainty_list.append(uncertainty)

    posterior_array = np.array(posterior_list)

    # Save posterior probabilities
    for i in range(5):
        data[f"Posterior_{i}"] = posterior_array[:, i]

    # Smoothed Bayesian confidence
    raw_confidence = posterior_array.max(axis=1)

    confidence = 0.60 + (raw_confidence * 0.35)
    confidence = np.clip(confidence, 0.60, 0.95)

    data["Posterior Confidence"] = confidence

    data["Uncertainty"] = uncertainty_list

    return data