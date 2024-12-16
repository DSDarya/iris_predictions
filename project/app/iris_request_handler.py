"""Класс FastApiHandler, который обрабатывает запросы API."""

import logging

import joblib
from sklearn.linear_model import LogisticRegression

logger = logging.getLogger(__name__)
model_path = "./models/iris_clf.pkl"


class IrisRequestHandler:
    """Класс обработки запроса, возвращает предсказание."""

    def __init__(self):

        self.param_types = {"iris_params": dict}
        self.required_model_params = [
            "SepalLengthCm",
            "SepalWidthCm",
            "PetalLengthCm",
            "PetalWidthCm",
        ]
        self.model = None

    def load_model(self):
        """Загрузка обученной модели."""

        try:
            self.model = joblib.load(model_path)
        except Exception as e:
            logger.warning(f"Failed to load model: {e}")

    def species_predict(self, model_params: dict, probability: bool) -> float:
        """Предсказание вида ириса."""
        request_features = [list(model_params.values())]
        if probability:
            probas = self.model.predict_proba(request_features)
            classes = self.model.classes_
            result = {}
            for class_name, proba in zip(classes, *probas):
                result[class_name] = f"{round(proba * 100, 2)}%"
            return result
        return self.model.predict(request_features)[0]

    def check_required_query_params(self, query_params: dict) -> bool:
        """Проверка параметров запроса на наличие обязательного набора."""

        if not isinstance(query_params["iris_params"], self.param_types["iris_params"]):
            return False
        return True

    def check_required_model_params(self, model_params: dict) -> bool:
        """Проверка параметров для получения предсказаний."""

        if set(model_params.keys()) == set(self.required_model_params):
            return True
        return False

    def validate_params(self, params: dict) -> bool:
        """Проверка корректности параметров запроса и параметров модели."""

        if not self.check_required_query_params(params):
            logging.warning("Not all query params exist")
            return False

        if not self.check_required_model_params(params["iris_params"]):
            logging.warning("Not all model params exist")
            return False
        return True

    def handle(self, params, probability):
        """Функция для обработки запросов API."""

        try:
            if not self.validate_params(params):
                logging.warning("Error while handling request")
                response = {"Error": "Problem with parameters"}
            else:
                model_params = params["iris_params"]
                logging.info(f"Predicting for iris: model_params:\n{model_params}")
                predicted_species = self.species_predict(model_params, probability)
                response = {"predicted_iris_species": predicted_species}
        except Exception as e:
            logging.warning(f"Error while handling request: {e}")
            return {"Error": "Problem with request"}
        else:
            return response

