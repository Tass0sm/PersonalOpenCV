import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    
    fgmask = fgbg.apply(frame)

    kernel = np.ones((5,5), np.uint8)

    erosion = cv2.erode(fgmask, kernel, iterations = 1)

    closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)
    cv2.imshow('closing', closing)
    cv2.imshow('erosion', erosion)
    

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
