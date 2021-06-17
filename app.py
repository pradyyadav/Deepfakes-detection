import os
from flask import Flask, request, jsonify, render_template
import model
from model import select_model
from model import prediction

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict/',methods=['POST','GET'])
def predict():
    if request.method == 'GET':
        return f"the predict is accessed directly, go to /"
    if request.method == 'POST':
        model = request.form
        return render_template('predict.html',model = model)

if __name__  ==  "__main__":        
    app.run(debug=True)