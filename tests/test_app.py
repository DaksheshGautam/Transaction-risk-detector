import os
import tempfile
import unittest
from unittest.mock import patch

from app import app
from src.transaction.pipelines.prediction_pipeline import PredictionPipeline


SAMPLE = {
    "amt": "42.50", "age": "35", "gender": "F",
    "merchant": "demo_merchant", "category": "grocery_pos",
    "job": "Engineer", "state": "CA", "zip": "90210",
    "lat": "34.09", "long": "-118.41", "merch_lat": "34.10",
    "merch_long": "-118.42", "city_pop": "35000",
    "unix_time": "1704067200",
}


class AppSmokeTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_form_and_styles_load(self):
        self.assertEqual(self.client.get("/").status_code, 200)
        with self.client.get("/static/css/styles.css") as response:
            self.assertEqual(response.status_code, 200)

    def test_real_model_prediction(self):
        response = self.client.post("/", data=SAMPLE)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Fraud Probability:", response.data)
        self.assertNotIn(b"Prediction failed", response.data)

    def test_invalid_input_shows_form_error(self):
        response = self.client.post("/", data={**SAMPLE, "amt": "invalid"})
        self.assertIn(b"Prediction failed. Please check input values.", response.data)
        self.assertNotIn(b"Traceback", response.data)

    def test_health_checks_artifact_readiness(self):
        self.assertEqual(self.client.get("/healthz").json, {"status": "ok"})
        with patch("app.get_predictor", side_effect=FileNotFoundError):
            self.assertEqual(self.client.get("/healthz").status_code, 503)

    def test_artifact_paths_work_from_other_directory(self):
        previous = os.getcwd()
        with tempfile.TemporaryDirectory(dir=previous) as directory:
            try:
                os.chdir(directory)
                predictor = PredictionPipeline()
                self.assertEqual(predictor.model.n_features_in_, 1263)
            finally:
                os.chdir(previous)


if __name__ == "__main__":
    unittest.main()
