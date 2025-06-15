import cv2
import numpy as np


img = cv2.imread('vada_pav_delight.png')
img = cv2.resize(img, (360, 360))
imgBlack = np.zeros((360, 360, 3),np.uint8)
imgJoin = cv2.vconcat((img, imgBlack))
imgJoinh = cv2.hconcat((img, imgBlack))


cv2.imshow('Joining Image', imgJoin)
cv2.imshow('Joining Image Horizontal', imgJoinh)
cv2.waitKey(0)