import cv2
import numpy as np
#import matplotlib.pyplot as plt

img = cv2.imread('oia.jpeg', cv2.IMREAD_COLOR)

px = img[55,55]

img[55,55] = [255, 255, 255]
printpx

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
