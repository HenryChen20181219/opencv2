import cv2
import numpy as np

# 腐蚀
img = cv2.imread('D:\photo\girl3.jpg', 0)

kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)


# cv2.imshow("src", img)
# cv2.imshow("show", erosion)
# cv2.waitKey(0)

# 膨胀
dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("src", img)
cv2.imshow("show", dilation)
cv2.waitKey(0)


