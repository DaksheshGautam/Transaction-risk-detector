import os
import joblib
import numpy as np
import pandas as pd

from src.transaction.logger import logger
from src.transaction.exception import CustomException
import sys
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        try:
            artifact_dir = Path(__file__).resolve().parents[3] / "artifacts"
            self.model_path = artifact_dir / "model.pkl"
            self.preprocessor_path = artifact_dir / "preprocessor.pkl"

            self.model = joblib.load(self.model_path)
            self.preprocessor = joblib.load(self.preprocessor_path)

            # tuned threshold
            self.threshold = 0.97807443

            logger.info("Prediction pipeline initialized")

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, input_df: pd.DataFrame):
        try:
            logger.info("Starting prediction")

            transformed_data = self.preprocessor.transform(input_df)

            probs = self.model.predict_proba(transformed_data)[:, 1]

            predictions = (probs >= self.threshold).astype(int)

            result = input_df.copy()
            result["fraud_probability"] = probs
            result["prediction"] = predictions

            return result

        except Exception as e:
            raise CustomException(e, sys)
