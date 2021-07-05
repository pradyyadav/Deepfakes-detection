"""This code forms a video out of the collection of images"""

import os
import cv2

RESULT = 'result'
CONTENT = os.listdir(RESULT)

for each in CONTENT:
    frames = os.listdir(RESULT + '/' + each)
    img=[]
    for frame in frames:
        img.append(cv2.imread(f'{RESULT}/{each}/{frame}'))

    height,width,layers=img[1].shape
    size = (width,height)
    video=cv2.VideoWriter(f'{RESULT}/{each}.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, size)

    for i in range(len(frames)):
        video.write(img[i])

cv2.destroyAllWindows()
video.release()
