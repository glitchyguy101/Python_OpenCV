import cv2
import numpy as np

print(cv2.__version__)
img = cv2.imread("image.jpg.png")
print(img.shape)
cv2.imshow("Image", img)
cv2.waitKey(0)
imgResize = cv2.resize(img, (300, 200))
print(imgResize.shape)
cv2.imshow("Resized Image", imgResize)
cv2.waitKey(0)
cap = cv2.VideoCapture(1)
cap.set(3, 640) # set width
cap.set(4, 480) # set height
cap.set(10, 100) # set brightness

#imgFace = cv2.FaceDetectorYN.create()
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#"""