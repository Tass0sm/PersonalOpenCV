import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,0,90])
    upper_red = np.array([230,200,150])
    
    #mask = cv2.inRange(hsv, lower_red, upper_red)
    #res = cv2.bitwise_and(frame,frame, mask= mask)

    res = frame

    #average smooth blur
    #kernel = np.ones((15,15), np.float32)/225
    #smoothed = cv2.filter2D(res, -1, kernel)

    #gaussian blur
    #blur = cv2.GaussianBlur(res, (15,15), 0)

    #Median Blur
    median = cv2.medianBlur(res,15)

    #Bilateral Blur
    #bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    #cv2.imshow('smoothed',smoothed)
    #cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    #cv2.imshow('bilateral',bilateral)

    #edges = cv2.Canny(median, 5, 150)

    laplacian = cv2.Laplacian(median,cv2.CV_64F)

    #cv2.imshow('edges',edges)

    cv2.imshow('laplacian',laplacian)

    #lower_red = np.array([0,0,2])
    #upper_red = np.array([180,180,10])
    #mask = cv2.inRange(laplacian, lower_red, upper_red)

    #cv2.imshow('mask', mask)

    lower_gray = np.array([0,150,0])
    upper_gray = np.array([180,255,200])
    mask = cv2.inRange(median, lower_gray, upper_gray)

    cv2.imshow('mask', mask)

    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
