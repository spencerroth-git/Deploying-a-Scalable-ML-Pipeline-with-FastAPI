import pytest
# TODO: add necessary import
import numpy as np
from ml.model import train_model, compute_model_metrics, inference

# TODO: implement the first test. Change the function name and input as needed
def test_train_model():
    """
    Testing that the model train and resturns a fitted estimator.
    """
    X_train = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 0], [0, 0, 1]])
    y_train = np.array([1, 0, 1, 0])
    model = train_model(X_train, y_train)
    assert model is not None
    assert hasattr(model, "predict")
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Testing that the metric outputs are within the expected range.
    """
    y = np.array([1, 0, 1, 1])
    preds = np.array([1, 0, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_inference():
    """
    Testing that the inference returns predictions that are the correct length.
    """
    X_train = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
    y_train = np.array([1, 0, 1, 0])
    model = train_model(X_train, y_train)
    X_test = np.array([[1, 0], [0, 1]])
    preds = inference(model, X_test)
    assert len(preds) == X_test.shape[0]
    pass
