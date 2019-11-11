import cv2 as cv
import numpy as np


def detect_circles_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 100)
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    for i in circles[0, : ]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (0, 0, 255), 2)
    cv.imshow("D:\photo\girl3.jpg")


src = cv.imread("D:\photo\girl3.jpg")
cv.namedWindow("input_image", cv.WINDOW_NORMAL)
cv.imshow("input_image", src)
detect_circles_demo(src)
cv.destroyAllWindows()
