import cv2
import time

# Load the cascade for face detection and smile detection
face_cascade = cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("cascade/haarcascade_smile.xml")

# Start the camera
camera = cv2.VideoCapture(0)
camera.set(3, 640)    # set Width
camera.set(4, 480)    # set Height

i=1     # for loop
interval=2      # for time interval between images
current_time=time.time()


while True:
    # Capture a frame from the camera
    isTrue, frame = camera.read()
    frame = cv2.flip(frame, 1)

    # Convert the frame to grayscale for face and smile detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        # minSize=(30, 30)
    )
    # faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # For each detected face, detect smiles
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        # for (x, y, w, h) in smiles:
        #     frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow('Selfie Camera', frame)

        # If a smile is detected, capture the selfie and save it
        now=time.time()
        if now-current_time>=interval:
            if len(smiles)>0:
                cv2.imwrite(f'Images\selfie{i}.png', frame)
                print('Selfie taken!')
                print(i)
                i+=1
                current_time=now

    # cv2.imshow('Selfie Camera', frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:    # press 'ESC' to quit
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
