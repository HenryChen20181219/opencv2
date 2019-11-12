import cv2
import numpy as np


# 形态学梯度
img = cv2.imread("D:\photo\girl3.jpg", 0)
kernel = np.ones((5, 5), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# 顶帽
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# 黑帽
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("src", img)
cv2.imshow("show", gradient)
cv2.imshow("show2", tophat)
cv2.imshow("show3", blackhat)
cv2.waitKey(0)




