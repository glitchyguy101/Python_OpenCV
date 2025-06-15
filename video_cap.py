import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    cv2.imshow('Video Feed', img)   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    