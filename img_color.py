import cv2
import numpy as np


img = cv2.imread('vada_pav_delight.png')


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

cv2.imshow('vada pav gray', imgGray)
cv2.imshow('vada pav blur', imgBlur)

cv2.waitKey(0)

