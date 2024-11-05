import unittest

from task_2.task_2 import calculate_aggregated_score, generate_random_data


class TestAggregatedThreatScore(unittest.TestCase):

    def test_no_outliers_similar_threat_scores(self):
        departments = [
            {"name": "Engineering", "importance": 3, "scores": generate_random_data(30, 5, 100)},
            {"name": "Marketing", "importance": 3, "scores": generate_random_data(31, 5, 100)},
            {"name": "Finance", "importance": 3, "scores": generate_random_data(29, 5, 100)},
            {"name": "HR", "importance": 3, "scores": generate_random_data(32, 5, 100)},
            {"name": "Science", "importance": 3, "scores": generate_random_data(30, 5, 100)}
        ]

        score = calculate_aggregated_score(departments)
        self.assertTrue(29 <= score <= 32)

    def test_all_departments_no_threats(self):
        departments = [
            {"name": "Engineering", "importance": 1, "scores": [0, 0, 0]},
            {"name": "Marketing", "importance": 1, "scores": [0, 0, 0]},
            {"name": "Finance", "importance": 1, "scores": [0, 0, 0]},
            {"name": "HR", "importance": 1, "scores": [0, 0, 0]},
            {"name": "Science", "importance": 1, "scores": [0, 0, 0]}
        ]
        score = calculate_aggregated_score(departments)
        self.assertEqual(score, 0)

    def test_all_departments_max_threats(self):
        departments = [
            {"name": "Engineering", "importance": 1, "scores": [90, 90, 90]},
            {"name": "Marketing", "importance": 1, "scores": [90, 90, 90]},
            {"name": "Finance", "importance": 1, "scores": [90, 90, 90]},
            {"name": "HR", "importance": 1, "scores": [90, 90, 90]},
            {"name": "Science", "importance": 1, "scores": [90, 90, 90]}
        ]
        score = calculate_aggregated_score(departments)
        self.assertEqual(score, 90)



if __name__ == '__main__':
    unittest.main()
