import cv2
import numpy as np

img = cv2.imread('Object.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,0,0])
upper_red = np.array([180,180,255])
            
mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask= mask)


cv2.imshow('img',img)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
