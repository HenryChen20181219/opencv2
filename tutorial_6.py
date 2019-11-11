import numpy as np

import cv2 as cv


def blur_demo(image):
    # 均值滤波
    dst = cv.blur(image, (5, 5))
    cv.imshow("blur_demo", dst)


def median_blur_demo(image):
    # 中值滤波
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur", dst)


def custom_blur_demo(image):

    kernel = np.ones([5, 5], np.float32)/25
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("custom_blur_demo", dst)


print("--------Hello Python-------------")
src = cv.imread("D:\photo\girl1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
median_blur_demo(src)

cv.waitKey(0)

cv.destroyAllWindows()

