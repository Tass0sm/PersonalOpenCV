import cv2
import numpy as np
import matplotlib.pyplot as plt

print(cv2.__version__)
#imgloc = "C:\\Users\\tasso\\Desktop\\oia.jpeg

img = cv2.imread('oia.jpeg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('guh', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
