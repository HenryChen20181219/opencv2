import numpy as np
import cv2 as cv


def fill_color_demo(image):
    copyImg = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2], np.uint8)
    cv.floodFill(copyImg, mask, (30, 30), (0, 255, 255), \
                 (100, 100, 100), (50, 50, 50), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyImg)


src1 = cv.imread("D:\photo\girl1.jpg")
src2 = cv.imread("D:\photo\girl2.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("image1", src1)
cv.imshow("image2", src2)
fill_color_demo(src1)
cv.waitKey(0)
cv.imshow()
