import numpy as np

import cv2 as cv


def add_demo(m1, m2):
    dst = cv.add(m1, m2)
    cv.imshow("add_demo", dst)


def subtract_demo(m1, m2):
    dst = cv.subtract(m1, m2)
    cv.imshow("subtract_demo", dst)


def divide_demo(m1, m2):
    dst = cv.divide(m1, m2)
    cv.imshow("divide_demo", dst)


def multiply_demo(m1, m2):
    dst = cv.multiply(m1, m2)
    cv.imshow("multiply_demo", dst)


def other_demo(m1, m2):
    M1, dev1 = cv.meanStdDev(m1)
    M2, dev2 = cv.meanStdDev(m2)
    h, w = m1.shape[:2]
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)


def contrast_brightness_demo(img, c, b):
    h, w, ch = img.shape
    blank = np.zeros([h, w, ch], img.dtype)
    dst = cv.addWeighted(img, c, blank, 1-c, b)
    cv.imshow("con-bri-demo", dst)

    img = np.zeros([h, w], np.uint8)
    m, dev = cv.meanStdDev(img)
    print(m)
    print(dev)


src1 = cv.imread("D:\photo\girl1.jpg")
src2 = cv.imread("D:\photo\girl5.jpg")
# print(src1)
# print(src2)
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)

# add_demo(src1, src2)
# subtract_demo(src1, src2)
# divide_demo(src1, src2)
# multiply_demo(src1, src2)

# other_demo(src1, src2)
contrast_brightness_demo(src1, 1.2, 10)
cv.waitKey(0)

