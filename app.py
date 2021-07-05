import os
import shutil
import cv2
from flask import Flask, request, jsonify, render_template
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
        result = []
        os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'    
        action = request.form
        action = request.form.to_dict()
        model = select_model(action['model'])
        video = os.path.join('test_videos',action['video'])
        result = prediction(model,video)
        return render_template('predict.html',form = result,video_path = video)
if __name__  ==  "__main__":        
    app.run(debug=True)