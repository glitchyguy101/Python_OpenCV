import cv2
import numpy as np

kernal = np.ones((5, 5), np.uint8)

#width, height = 400, 350
img = cv2.imread('vada_pav_delight.png')
imgCard = cv2.imread('Credit-cards.webp')
#imgCard = cv2.resize(imgCard, (360, 360))
img = cv2.resize(img, (360, 360))
imgBlack = np.zeros((360, 360, 3),np.uint8)
imgJoin = cv2.vconcat((img, imgBlack))


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
#cv2.imshow("Jined Image", imgJoin)
#cv2.imshow('Black Img', imgBlack)
#cv2.imshow('vada pav', img)
print(imgCard.shape)

cv2.waitKey(0)










# Uncomment the following lines to apply image processing techniques



"""
height, width = 250, 360
pts1 = np.float32([[388, 94], [1038, 204], [278, 314], [917, 427]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(imgCard, matrix, (width, height))

for x in range(0, 4):
    cv2.circle(imgCard, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 255, 0), cv2.FILLED)

cv2.imshow('Card orignal', imgCard)
cv2.imshow('Card', output)"""


"""imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(imgBlur,100, 100 )
imgResize = cv2.resize(img, (width, height))
imgCrop = img[:320,:]

imgDilation = cv2.dilate(imgCanny,kernal, iterations=1)
imgErode = cv2.erode(imgDilation, kernal, iterations=1)

cv2.line(imgBlack, (150, 150), (440, 440), (255, 0, 0), 3)
cv2.rectangle(imgBlack, (320, 240), (520, 440), (0, 255, 0), cv2.FILLED)
cv2.circle(imgBlack, (320, 120), 50, (255, 0, 0), 3, cv2.FILLED)
cv2.putText(imgBlack, "OPEN CV2", (80, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (150, 150, 150), 2)

"""

'''cv2.imshow('vada pav gray', imgGray)
cv2.imshow('vada pav blur', imgBlur)
cv2.imshow('vada pav canny', imgCanny)
cv2.imshow('vada pav dilte', imgDilation)

cv2.imshow('vada pav resize', imgResize)
cv2.imshow('vada pav crop', imgCrop)
cv2.imshow('vada pav erode', imgErode)'''
