import cv2
import numpy as np

width = 360
height = 144
cap = cv2.VideoCapture(1)
cap.set(3, width)
cap.set(4, height)

# Function to do nothing for trackbar callback
def nothing(x):
    pass
# Function to horizontally stack images with resizing   
def hstack(scale, arrays):
    # If arrays is 2D (list of lists), stack each row then stack rows vertically
    if isinstance(arrays[0], (list, tuple)):
        rows = [np.hstack([cv2.resize(img, (0, 0), fx=scale, fy=scale) for img in row]) for row in arrays]
        return np.vstack(rows)
    else:
        # 1D: just stack horizontally
        return np.hstack([cv2.resize(img, (0, 0), fx=scale, fy=scale) for img in arrays])
# Create a window for trackbars
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 23, 255, nothing)
cv2.createTrackbar("Threshold2", "Parameters", 219, 255, nothing)

# Function to get contours and draw them on the image   
def  getcounter(img, imgContours):
    contours, hierarchy = cv2.findContours(imgContours, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(img, cnt, -1, (0, 255, 0), 7)
            per1 = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * per1, True)
            print(len(approx))
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 5)
            cv2.putText(img, "Points:" + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 155), 2)
            cv2.putText(img, "Area:" + str(int(area)), (x + w + 20, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 155), 2)

            # Count the number of sides
            num_sides = len(approx)
            if num_sides == 3:
                shape_name = "Triangle"
            elif num_sides == 4:
                aspect_ratio = w / h
                shape_name = "Square" if 0.95 < aspect_ratio < 1.05 else "Rectangle"
            elif num_sides == 5:
                shape_name = "Pentagon"
            elif num_sides == 6:
                shape_name = "Hexagon"
            else:
                shape_name = "Circle"
            cv2.putText(img, shape_name, (x + w + 20, y + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 155), 2)

# Main loop to capture video and process frames
while True:
    success, img = cap.read()

    imgContours = img.copy()

    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    imgCanny =  cv2.Canny(imgGray, threshold1, threshold2)
    imgGrayColor = cv2.cvtColor(imgGray, cv2.COLOR_GRAY2BGR)  # Convert grayscale to color
    imgCannyColor = cv2.cvtColor(imgCanny, cv2.COLOR_GRAY2BGR)  # Convert Canny output to color
    
    kernal = np.ones((4, 4), np.uint8)
    imgDilat =cv2.dilate(imgCanny, kernal, iterations=1)
    imgDilat = cv2.cvtColor(imgDilat, cv2.COLOR_GRAY2BGR)

    getcounter(imgContours, imgCanny)

    #hstacked = hstack(0.9, [[img, imgBlur], [imgCannyColor, imgContours]])
    cv2.imshow("Contours", imgContours)
    #cv2.imshow("stacked", hstacked)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

    #stack = np.hstack((img, imgBlur, imgGrayColor, imgCannyColor))
    #cv2.imshow("Canny", imgCanny)
    #cv2.imshow('Video Feed', img)   
    #cv2.imshow('Video Feed', hstacked) 
"""
def hstack(scale, arrays):
return np.hstack([cv2.resize(a, (0, 0), fx=scale, fy=scale) for a in arrays])"""