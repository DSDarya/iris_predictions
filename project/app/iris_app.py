"""Приложение Fast API для модели предсказания вида ириса."""

from fastapi import FastAPI

from .iris_request_handler import IrisRequestHandler

app = FastAPI()
iris_handler = IrisRequestHandler()
iris_handler.load_model()
app.handler = iris_handler


@app.get("/", status_code=200)
def show_status():
    return {"status": "OK"}


@app.post("/species/")
def iris_predictions(model_params: dict):
    """Функция определяет вид ириса."""

    all_params = {"iris_params": model_params}
    iris_prediction = app.handler.handle(all_params, False)
    return iris_prediction


@app.post("/species/probability/")
def iris_predictions(model_params: dict):
    """Функция определяет вид ириса."""

    all_params = {"iris_params": model_params}
    iris_prediction = app.handler.handle(all_params, True)
    return iris_prediction
