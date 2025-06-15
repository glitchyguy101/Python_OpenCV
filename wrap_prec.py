import cv2
import numpy as np


imgCard = cv2.imread('Credit-cards.webp')

height, width = 250, 360
pts1 = np.float32([[388, 94], [1038, 204], [278, 314], [917, 427]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(imgCard, matrix, (width, height))

"""for x in range(0, 4):
    cv2.circle(imgCard, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 255, 0), cv2.FILLED)"""

cv2.imshow('Card orignal', imgCard)
cv2.imshow('Card', output)

cv2.waitKey(0)