import cv2
import numpy as np

kernal = np.ones((5, 5), np.uint8)

img = cv2.imread('vada_pav_delight.png')

imgBlur = cv2.GaussianBlur(img, (7, 7), 0)


imgCanny = cv2.Canny(imgBlur,100, 100 )
imgDilation = cv2.dilate(imgCanny,kernal, iterations=1)
imgErode = cv2.erode(imgDilation, kernal, iterations=1)
cv2.imshow('vada pav canny', imgCanny)
cv2.imshow('vada pav dilte', imgDilation)
cv2.imshow('vada pav erode', imgErode)

cv2.waitKey(0)