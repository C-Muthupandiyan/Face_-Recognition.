# Face_-Recognition.

I am excited to share that I have completed a face recognition project. Here are the details:

 Programming Language: Python (version 3.12)
 Face-Detection Algorithm: haarcascade_frontalface_default.xml
 Modules and Packages:
  OpenCV: Used to access the webcam, draw a rectangle around the detected face, and add text to the output.
   Pickle: Used to create a pickle file in the same folder (face_detection), capturing face images from different angles and storing them in the pickle format to improve prediction efficiency.
   NumPy: Used for array operations and numerical computations.
   OS Module: Used to check whether a file is present in the folder.
   Scikit-Learn: This package is used for training the model with face data. In this project, I used KNeighborsClassifier, a machine learning algorithm in Scikit-Learn for classification tasks. It implements the K-Nearest Neighbors (KNN) algorithm, a supervised learning method.
   CSV Module: Used to store attendance data in CSV file format.
  -win32com.client and Dispatch: When the 'o' key is pressed, it uses the SAP voice to announce "attendance taken" and holds the image for 5 seconds.

Major Steps Involved in the Project:
1. Detecting the Faces
2. Capturing Face Images from Different Angles and Storing Them in Pickle Format
3. Using Scikit-Learn and KNeighborsClassifier for Face Recognition

