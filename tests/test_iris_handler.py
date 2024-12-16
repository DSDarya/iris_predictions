from typing import Sequence
from _pytest.mark.structures import ParameterSet
import pytest
from project.app.iris_request_handler import IrisRequestHandler

handler = IrisRequestHandler()
model_path = "project/models/iris_clf.pkl"

def test_load_model():
    loaded_model = IrisRequestHandler()
    loaded_model.load_model()
    assert loaded_model is not None
    
@pytest.mark.parametrize(
    "query_params",
    [{"iris_params": dict}],
)    
def check_required_query_params(query_params: dict):
    assert handler.check_required_model_params(query_params["iris_params"])

@pytest.mark.parametrize(
    "model_params",
    [{"SepalLengthCm": 1.0,"SepalWidthCm": 2,"PetalLengthCm": 2,"PetalWidthCm": 4}]
)    
def test_check_required_model_params(model_params: dict):
    assert handler.check_required_model_params(model_params)