import os
from flask import Flask, request, jsonify, render_template
import models
from models import select_model
from models import prediction

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == 'GET':
        return f"the predict is accessed directly, go to /"
    if request.method == 'POST':
        os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
        model = request.form
        model = request.form.to_dict(model)
        model = select_model(model['model'])
        result = prediction(model,'test_videos/aomqqjipcp.mp4')
        return render_template('predict.html',form = result)

if __name__  ==  "__main__":        
    app.run(debug=True)