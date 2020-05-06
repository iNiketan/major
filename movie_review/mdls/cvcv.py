import cv2
import sys

i = sys.argv[1]
cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resize = cv2.resize(gray, (200, 200))
    cv2.imshow('apage' ,resize)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
