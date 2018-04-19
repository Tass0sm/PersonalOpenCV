import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()

    #laplacian
    laplacian = cv2.Laplacian(frame,cv2.CV_64F)

    #sobel

    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    #Canny Edges

    edges = cv2.Canny(frame, 80, 200)

    #cv2.imshow('original',frame)
    cv2.imshow('laplacian',laplacian)
    #cv2.imshow('sobelX', sobelx)
    #cv2.imshow('sobelY', sobely)
    cv2.imshow('edges', edges)
    
    #cv2.imshow('res',res)

    
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
