import cv2
import numpy as np


imgCard = cv2.imread('Credit-cards.webp')

circles = np.zeros((4, 2), np.int32)
counter = 0
def mousPoint(event, x, y, flags, params):
    global counter

    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        print(x, y)
        cv2.circle(imgCard, (x, y), 10, (0, 255, 0), cv2.FILLED)
        cv2.imshow('Card', imgCard)

cv2.imshow('Card', imgCard)

cv2.setMouseCallback('Card', mousPoint)
cv2.waitKey(0)
