import cv2 as cv
import numpy as np


def contours_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image", binary)
    cloneTmage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), -1)
    cv.imshow("pcontours", image)


src = cv.imread("D:\photo\girl3.jpg")
cv.namedWindow("input_image", src)
contours_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()