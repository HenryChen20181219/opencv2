import numpy as np

import cv2 as cv


def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)


def extrace_object_demo():
    capture = cv.VideoCapture(r"C:\Users\12801\Videos\Captures\雷电模拟器 2019-08-30 21-47-02.mp4")  # \U是转义成unicode,需加r不转义
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        low_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        cv.inRange(hsv, low_hsv, upper_hsv)
        cv.imshow("video", frame)
        c = cv.waitKey(40)
        if c == 27:
            break


print("--------Hello Python--------")
src = cv.imread("D:\photo\girl3.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)

b, g, r = cv.split(src)
print(r.shape)

# cv.imshow("b", b)
# cv.imshow("g", g)
# cv.imshow("r", r)
# src1 = cv.merge([b, g, r])
# src1[0, :, :] = 0
# cv.imshow("srcb", src1)
# src1[:, 0, :] = 0
# cv.imshow("srcg", src1)
# src1[:, :, 0] = 0
# cv.imshow("srcr", src1)
# color_space_demo(src)
extrace_object_demo()
cv.waitKey(0)
cv.destroyAllWindows()
