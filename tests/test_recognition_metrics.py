import unittest
from evaluation.metrics import evaluate_rows

class TestRecognitionMetrics(unittest.TestCase):
    def test_face_and_voice_counts(self):
        rows=[
            {"modality":"face","true_id":"A","predicted_id":"A"},
            {"modality":"face","true_id":"B","predicted_id":""},
            {"modality":"face","true_id":"","predicted_id":"A"},
            {"modality":"voice","true_id":"A","predicted_id":"B"},
        ]
        results=evaluate_rows(rows)
        self.assertEqual(results["face"]["correct_identity_accuracy"], .5)
        self.assertEqual(results["face"]["false_reject_rate"], .5)
        self.assertEqual(results["face"]["false_accept_rate"], 1.)
        self.assertIsNone(results["voice"]["false_accept_rate"])
        self.assertEqual(results["voice"]["wrong_identity_rate"],1.)

    def test_no_data(self):
        with self.assertRaises(ValueError):
            evaluate_rows([])

    def test_invalid_modality(self):
        with self.assertRaises(ValueError):
            evaluate_rows([{"modality":"other","true_id":"A","predicted_id":"A"}])

if __name__ == "__main__":
    unittest.main()
