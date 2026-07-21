import numpy as np


def particle_filter(data, n_particles=500):

    data = data.copy()

    if "Posterior Confidence" not in data.columns:
        return data

    particles = np.random.uniform(0.5, 1.0, n_particles)

    filtered = []

    for _, row in data.iterrows():

        confidence = row["Posterior Confidence"]

        if np.isnan(confidence):
            filtered.append(np.nan)
            continue

        # Prediction step
        particles += np.random.normal(0, 0.02, n_particles)

        # Update step
        weights = np.exp(-((particles - confidence) ** 2) / 0.01)
        weights /= weights.sum()

        # Resample
        indices = np.random.choice(
            np.arange(n_particles),
            size=n_particles,
            p=weights
        )

        particles = particles[indices]

        # Estimated confidence
        estimate = np.mean(particles)
        estimate = np.clip(estimate, 0.60, 0.95)

        filtered.append(estimate)

    data["Particle Confidence"] = filtered

    return data