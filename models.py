import os
import tensorflow as tf
import dlib
import cv2
import os
import numpy as np
from PIL import Image, ImageChops, ImageEnhance
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

def select_model(model_name):
    if model_name == 'InceptionResnetv2':
        print("using inception")
        detection_model = load_model('detection_models/deepfake-detection-model-vgg.h5')
    elif model_name == 'VGG16':
        print("using vgg")
        detection_model = load_model('detection_models/deepfake-detection-model-vgg.h5')
    else:
        print("An Error Occurred!!!")
    return detection_model

def prediction(model,video_path):
    input_shape = (128, 128, 3)
    pr_data = []
    detector = dlib.get_frontal_face_detector()
    cap = cv2.VideoCapture(video_path)
    frameRate = cap.get(5)
    while cap.isOpened():
        frameId = cap.get(1)
        ret, frame = cap.read()
        if ret != True:
            break
        if frameId % ((int(frameRate)+1)*1) == 0:
            face_rects, scores, idx = detector.run(frame, 0)
            for i, d in enumerate(face_rects):
                x1 = d.left()
                y1 = d.top()
                x2 = d.right()
                y2 = d.bottom()
                crop_img = frame[y1:y2, x1:x2]
                data = img_to_array(cv2.resize(crop_img, (128, 128))).flatten() / 255.0
                data = data.reshape(-1, 128, 128, 3)
                return np.argmax(model.predict(data))


# model = select_model('VGG16')
# print(prediction(model,'./test_videos/dgmevclvzy.mp4'))