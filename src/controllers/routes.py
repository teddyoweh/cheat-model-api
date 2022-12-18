from flask import render_template, Blueprint, request
from model import predict

blueprint = Blueprint('pages', __name__)


################
#### routes ####
################
@blueprint.route('/')
def home():
    return {'message': 'Hey there! got to /model to get a prediction'}

@blueprint.route('/model', methods=['GET', 'POST'])
def cheat_model():
    if request.method == 'POST':
        sentence = request.json['sentence']
    else:
        sentence = request.args.get('sentence')

    # Pass the sentence to the example function
    result = predict(sentence)

    return result

 