from flask import Flask, request, jsonify, render_template
import model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        result = request.form
    return render_template("index.html",result = model.prediction(model.select_model(model_name='VGG16'),'./test_videos/aomqqjipcp.mp4'))

if __name__  ==  "__main__":        
    app.run(debug=False)