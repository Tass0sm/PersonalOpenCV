import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners = np.int0(corners)

    harris = cv2.cornerHarris(frame, 100, 100, 10)

    edges = cv2.Canny(frame, 80, 200)
    
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(frame, (x,y), 3, 255, -1)

    cv2.imshow('Corner', frame)

    edgeCorners = cv2.goodFeaturesToTrack(edges, 100, 0.01, 10)
    edgeCorners = np.int0(edgeCorners)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(edges, (x,y), 3, 255, -1)

    cv2.imshow('edges', edges)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()
cap.release()
