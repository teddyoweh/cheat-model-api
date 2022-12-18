from .utils import *
model = load_model()

def predict(sentence):
    ans = list(predict_sentence(model, sentence))
    print()
    return {
        'target':str(ans[0][0]),
        'probability':str(ans[1][0])

    }
 