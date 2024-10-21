import cv2
import pickle
import numpy as np
import os

# Ensure 'Data/' directory exists
if not os.path.exists('Data'):
    os.makedirs('Data')

video = cv2.VideoCapture(0)
trained = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces_data = []
i = 0
name = input("Enter Your Name:")

while True:
    success, frame = video.read()
    if not success or frame is None:  # Checking if the frame was successfully captured
        continue

    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = trained.detectMultiScale(gray_image)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        crop_image = frame[y:y + h, x:x + w]
        resize_image = cv2.resize(crop_image, (50, 50))

        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append(resize_image)

    i += 1
    cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow('video', frame)

    key = cv2.waitKey(1)
    if key == ord('q') or len(faces_data) == 100:
        break

video.release()
cv2.destroyAllWindows()

# Reshape face data
faces_data = np.asarray(faces_data)
faces_data = faces_data.reshape(100, -1)

# Save the names data
names_file = 'Data/names.pkl'
if 'names.pkl' not in os.listdir('Data'):
    names = [name] * 100
    with open(names_file, 'wb') as f:
        pickle.dump(names, f)
else:
    with open(names_file, 'rb') as f:
        names = pickle.load(f)
    names = names + [name] * 100
    with open(names_file, 'wb') as f:
        pickle.dump(names, f)

# Save the faces data
faces_data_file = 'Data/faces_data.pkl'
if 'faces_data.pkl' not in os.listdir('Data'):
    with open(faces_data_file, 'wb') as f:
        pickle.dump(faces_data, f)
else:
    with open(faces_data_file, 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
    with open(faces_data_file, 'wb') as f:
        pickle.dump(faces, f)
