import cv2
import numpy as np
import matplotlib.pylab as plt


# 开运算
img = cv2.imread("D:\photo\girl3.jpg", 0)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# cv2.imshow("src", img)
cv2.imshow("show", opening)
# cv2.waitKey(0)


# 闭运算
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("src", img)
cv2.imshow("show1", opening)
cv2.waitKey(0)
