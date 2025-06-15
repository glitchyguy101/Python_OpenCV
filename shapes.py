import cv2
import numpy as np


img = cv2.imread('vada_pav_delight.png')
imgBlack = np.zeros((640, 640, 3),np.uint8)



cv2.line(imgBlack, (150, 150), (440, 440), (255, 0, 0), 3)
cv2.rectangle(imgBlack, (320, 240), (520, 440), (0, 255, 0), cv2.FILLED)
cv2.circle(imgBlack, (320, 120), 50, (255, 0, 0), 3, cv2.FILLED)
cv2.putText(imgBlack, "OPEN CV2", (80, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (150, 150, 150), 2)
cv2.imshow('Black Img', imgBlack)
cv2.waitKey(0)