import time
import cv2

time.sleep(1)
cap =cv2.VideoCapture(0)

_, frame1 = cap.read()
frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1 = cv2.GaussianBlur(frame1, (21, 21), 0)

while True:
    _, frame2 = cap.read()
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame2 = cv2.GaussianBlur(frame2, (21, 21), 0)
    framedif = cv2.absdiff(frame1, frame2)
    frame1 =frame2
    flipframedif = cv2.flip(framedif, 1)
    cv2.imshow('e', flipframedif)
    cv2.waitKey(1)