from utils import *

model = load_model()

def predict(sentence):
    ans = list(predict_sentence(model, sentence))
    print()
    return {
        'target':ans[0][0],
        'probability':ans[1][0]

    }
 