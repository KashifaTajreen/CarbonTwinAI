from predictor import train_model


def test_model_training():
    model = train_model()

    assert model is not None
    assert hasattr(model, "predict")