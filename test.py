from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime

from win32com.client import Dispatch
def speak(str1):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str1)

# File paths
names_file = 'Data/names.pkl'
faces_data_file = 'Data/faces_data.pkl'

# Ensure 'Data/' directory exists
if not os.path.exists('Data'):
    os.makedirs('Data')

video = cv2.VideoCapture(0)
trained = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load data from the pickle files
with open(names_file, 'rb') as f:
    LABELS = pickle.load(f)
with open(faces_data_file, 'rb') as f:
    FACES = pickle.load(f)

# Initialize and train KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

COL_NAMES=['NAME','TIME']
while True:
    success, frame = video.read()
    if not success or frame is None:  # Checking if the frame was successfully captured
        continue

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = trained.detectMultiScale(gray_image)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        crop_image = frame[y:y + h, x:x + w]
        resize_image = cv2.resize(crop_image, (50, 50)).flatten().reshape(1, -1)

        # Predict the label for the detected face
        output = knn.predict(resize_image)
        ts=time.time()
        date=datetime.fromtimestamp(ts).strftime("%d-%m-%y")
        timestamp=datetime.fromtimestamp(ts).strftime("%H:%M-%S")
        exist=os.path.isfile("Attendance/Attendance"+ date +".csv")
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(50,50,255),2)
        cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
        cv2.putText(frame, str(output[0]), (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

        attendance=[str(output[0]),str(timestamp)]
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key==ord('o'):
        speak("Attendance taken")
        time.sleep(5)

        if exist:
            with open("Attendance/Attendance"+ date +".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
           
                writer.writerow(attendance)
            csvfile.close()
        else:
            with open("Attendance/Attendance"+ date +".csv","+a") as csvfile:
                writer=csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
            csvfile.close()

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
