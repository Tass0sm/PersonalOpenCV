import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('Object.jpg')
img2 = cv2.imread('Test 1.jpg')

#CORNERS --

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray1 = np.float32(gray1)

corners1 = cv2.goodFeaturesToTrack(gray1, 100, 0.01, 10)

corners1 = np.int0(corners1)

for corner in corners1:
    x, y = corner.ravel()
    cv2.circle(img1, (x,y), 3, 255, -1)


cv2.imshow('Corner', img1)

##OIAJO

#gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#gray2 = np.float32(gray2)

#corners2 = cv2.goodFeaturesToTrack(gray2, 100, 0.01, 10)

#corners2 = np.int0(corners2)

#for corner in corners2:
#    x, y = corner.ravel()
#    cv2.circle(img2, (x,y), 3, 255, -1)


#cv2.imshow('Corner', img2)






#-- CORNERS

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
plt.imshow(img3)
plt.show()
