import cv2
import numpy as np
from matplotlib import pyplot as plt


roi = cv2.imread("D:\photo\girl1.jpg")
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)


target = cv2.imread("D:\photo\girl1.jpg")
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)


roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
# 输入图像，选择图像通道，掩膜，None代表处理整幅图像，柱子，范围


cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)


disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(dst, -1, disc, dst)


ret, thresh = cv2.threshold(dst, 50, 255, 0)
thresh = cv2.merge((thresh, thresh, thresh))
res = cv2.bitwise_and(target, thresh)


res = np.vstack((target, thresh, res))
cv2.imshow("res", res)
cv2.waitKey(0)