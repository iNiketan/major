import numpy as np
import pandas as pd
from keras.models import load_model
from keras.preprocessing import image
#from keras.preprocessing.image import ImageDataGenerator
import cv2

import datetime
import os

file = "mdl33.h5"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
this = os.path.join(BASE_DIR, file)
# load model
model = load_model(this)
#----------------------------------------------

##
cascade = "haarcascade_frontalface_default.xml"
face_haar_cascade = cv2.CascadeClassifier(os.path.join(BASE_DIR, cascade))
lst = []
timestamp = []
cap=cv2.VideoCapture(0)  # keep it zero for live feed from webcam


while True:
    ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
    if not ret:
        continue
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)
        roi_gray = gray_img[y:y + w, x:x + h]  # cropping region of interest i.e. face area from  image
        # formating image for model
        roi_gray = cv2.resize(roi_gray, (48, 48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255

        predictions = model.predict(img_pixels)

        # find max indexed array
        # print(predictions)
        max_index = np.argmax(predictions[0])

        emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        predicted_emotion = emotions[max_index]
        lst.append(predicted_emotion)
        timestamp.append(datetime.datetime.now())
        cv2.putText(test_img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    resized_img = cv2.resize(test_img, (200, 200))

    # out.write(resized_img)
    cv2.imshow('Facial emotion analysis ', resized_img)

    # to tweak with frame per second change the value inside the cv2.waitKey(?)

    if cv2.waitKey(100) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows()

data = {'expressions': lst, 'timestamp': timestamp}
df = pd.DataFrame(data)
df_name = "dataout.pkl"
df.to_pickle(os.path.join(os.path.dirname(os.path.abspath(__file__)), df_name))

