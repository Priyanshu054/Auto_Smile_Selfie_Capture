import cv2
import time

# Start the camera
camera = cv2.VideoCapture(0)
camera.set(3, 640)    # set Width
camera.set(4, 480)    # set Height

interval=2
current_time=time.time()

i=1
while True:
    # Capture a frame from the camera
    isTrue, frame = camera.read()
    frame = cv2.flip(frame, 1)

    now=time.time()
    if now-current_time>=interval:
        cv2.imwrite(f'Images\selfie{i}.png', frame)
        print('Selfie taken!')
        i+=1
        current_time=now
        # cv2.imshow("frame",frame)
    cv2.imshow("frame",frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:    # press 'ESC' to quit
        break

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
    

