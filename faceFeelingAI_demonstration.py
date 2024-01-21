import tensorflow as tf
import cv2
import os
import numpy as np
import frameTime

# 비디오를 0.1초씩 잘라 이미지로 저장
try:
    file = input("동영상 경로명을 입력하세요 : ")
    path = frameTime.imageSave(file, 1)  # 이미지 저장된 디렉토리 경로명
except:
    print("Error: 제대로 된 파일 경로인지 확인하세요")
    exit(0)
    
    
# 얼굴 인식 안 하고 정규화
def imageResize(path):
    imageList = os.listdir(path)
    prediction = [0] * len(imageList)     # 고려사항:image 개수가 너무 많으면 리스트에 다 안 담길 수도 있음
    
    for imagePath in imageList:
        image = cv2.imread(os.path.join(path, imagePath))
        roi = cv2.resize(image, (64, 64))
        roi = roi / 255
        roi = np.expand_dims(roi, axis=0)
        
        time = int(imagePath[4] + imagePath[5] + imagePath[7] + imagePath[8] + imagePath[10] + imagePath[11] + imagePath[13])
        prediction[time - 1] = roi
    return prediction
    
# 얼굴 인식 하고 정규화
def imageFaceRecogResize(path):
    imageList = os.listdir(path)
    prediction = [0] * len(imageList)
    
    for imagePath in imageList:
        image = cv2.imread(os.path.join(path, imagePath))
        
        # 얼굴 인식 먼저
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        original_image = image.copy()
        faces = face_detector.detectMultiScale(original_image)
        if faces != ():
            roi = image[faces[0][1]:faces[0][1]+faces[0][3], faces[0][0]:faces[0][0]+faces[0][2]]
            print("OK okokokokok")
    
            roi = cv2.resize(roi, (64, 64))
    
        else:
            roi = cv2.resize(image, (64, 64))
        
        roi = roi / 255
        roi = np.expand_dims(roi, axis=0)
        
        time = int(imagePath[4] + imagePath[5] + imagePath[7] + imagePath[8] + imagePath[10] + imagePath[11] + imagePath[13])
        prediction[time - 1] = roi
        
    return prediction



prediction = imageResize(path)
prediction2 = imageFaceRecogResize(path)

# AI 모델을 이용하여 감정 예측
with open(os.path.join('seventhAI', 'faceFeelingAI7_56.json'), 'r') as json_file:
    json_saved_model = json_file.read()

aiModel = tf.keras.models.model_from_json(json_saved_model)
aiModel.load_weights(os.path.join('seventhAI', 'weights7_56.hdf5'))
aiModel.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])

probs = []
for i in range(len(prediction)):
    probs.append(aiModel.predict(prediction[i]))
print(probs[:5])


############################################################
############################################################

# 가장 높은 확률의 감정 결과  (0:기쁨, 1:당황, 2:분노, 3:슬픔, 4:중립)
result = np.argmax(probs[0])
print(result)

import matplotlib.pyplot as plt
import unicodedata
import seaborn as sns
import pandas as pd

x = ["기쁨", "당황", "분노", "슬픔", "중립"]

'''
x = list(test_set.class_indices)
for i in range(len(x)):
    x[i] = unicodedata.normalize('NFC', x[i])
'''

y = probs[0][0]
data = pd.DataFrame(x, y)

plt.rcParams['font.family'] = 'AppleGothic'

sns.set_palette('Spectral')
sns.barplot(data, x=x, y=y)
plt.title("단일 이미지 감정 분석 결과")
plt.show()
