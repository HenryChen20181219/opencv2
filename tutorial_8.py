import cv2 as cv
import numpy as np


def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)


def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)


