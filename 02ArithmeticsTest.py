import cv2
import numpy as np
#import matplotlib.pyplot as plt

img1 = cv2.imread('oia.jpeg')
img2 = cv2.imread('ProfileTwo.png')

#shape
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

#grayscale temp
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#threshold grayscale temp
ret, mask = cv2.threshold(img2gray, 100, 255, cv2.THRESH_BINARY_INV)

#invert that thresholded image
mask_inv = cv2.bitwise_not(mask)

#Get the bg of image one with the fg from the inverted threshold on image two
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

#Add the two images together
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
