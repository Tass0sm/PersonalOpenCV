import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,0,90])
    upper_red = np.array([230,200,150])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #Dilation/Eroision

    kernel = np.ones((10,10), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations = 1)
    dilation = cv2.dilate(mask, kernel, iterations = 1)
    
    #False Positives/Negatives & Opening/Closing

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    #black hat and top hat is the difference between the input and the opening/closing

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('erosion',erosion)
    #cv2.imshow('dilation',dilation)
    #cv2.imshow('opening',opening)
    #cv2.imshow('closing',closing)

    lower_gray = np.array([0,150,0])
    upper_gray = np.array([180,255,255])
    mask = cv2.inRange(frame, lower_gray, upper_gray)

    cv2.imshow('mask', mask)

    im2, contours, hierarchy = cv2.findContours(mask,
                                                cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame, [contours[1]], -1, 255, -1) # filled
    
    cv2.imshow('frame', frame)


    #cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
