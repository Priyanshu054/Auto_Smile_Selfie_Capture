''' Smile Detection using OpenCV '''

import cv2

# Load the cascade for face detection and smile detection
faceCascade = cv2.CascadeClassifier("cascade\haarcascade_frontalface_default.xml")
smileCascade = cv2.CascadeClassifier("cascade\haarcascade_smile.xml")

capture = cv2.VideoCapture(0)   # start capturing
capture.set(3, 640)   # set Width
capture.set(4, 480)   # set Height

while True:
    isTrue, img = capture.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
    # print(faces) --> it will return a 2D array containing face coordinates

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        smiles = smileCascade.detectMultiScale(gray, 1.5, 20) 
        for (x, y, w, h) in smiles:
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    cv2.imshow('Detecting Smile.....', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:      # press 'ESC' to quit
        break
    
capture.release()
cv2.destroyAllWindows()