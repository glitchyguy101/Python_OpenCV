import cv2
import numpy as np

img = cv2.imread('vada_pav_delight.png')


width, height = 400, 350
imgResize = cv2.resize(img, (width, height))
imgCrop = img[:320,:]

cv2.imshow('vada pav resize', imgResize)
cv2.imshow('vada pav crop', imgCrop)
cv2.waitKey(0)