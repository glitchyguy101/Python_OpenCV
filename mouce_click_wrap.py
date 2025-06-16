import cv2
import numpy as np


imgCard = cv2.imread('Credit-cards.webp')
if imgCard is None:
    raise FileNotFoundError("Credit-cards.webp not found in the current directory.")

imgCopy = imgCard.copy()
circles = np.zeros((4, 2), np.int32)
counter = 0


height, width = 250, 360

def mousPoint(event, x, y, flags, params):
    global counter, imgCopy
    if event == cv2.EVENT_LBUTTONDOWN and counter < 4:
        circles[counter] = x, y
        counter += 1
        cv2.circle(imgCopy, (x, y), 10, (0, 255, 0), cv2.FILLED)
        cv2.imshow('Card orignal', imgCopy)
        if counter == 4:
            pts1 = np.float32(circles)
            pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            output = cv2.warpPerspective(imgCard, matrix, (width, height))
            cv2.imshow('Card', output)


cv2.imshow('Card orignal', imgCopy)
cv2.setMouseCallback('Card orignal', mousPoint)
cv2.waitKey(0)
cv2.destroyAllWindows()
