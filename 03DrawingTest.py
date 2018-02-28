import cv2
import numpy as np
#import matplotlib.pyplot as plt

img = cv2.imread('oia.jpeg', cv2.IMREAD_COLOR)

#                                B  G    R
cv2.line(img, (0,0), (150,150), (0, 255, 0), 10)
cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)
cv2.circle(img, (100, 63), 55, (0, 255, 0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (0, 130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
