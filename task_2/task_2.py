import numpy as np


def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


def calculate_aggregated_score(departments):
    total_weighted_score = 0
    total_importance = 0

    for department in departments:
        total_importance += department["importance"]

    for department in departments:
        avg_scores = np.mean(department["scores"])
        total_weighted_score += avg_scores * department["importance"]

    aggregated_score = total_weighted_score / total_importance
    return min(max(aggregated_score, 0), 90)
