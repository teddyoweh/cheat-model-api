from .utils import *

model = load_model()

def predict(sentence):
    return predict_sentence(model, sentence)
