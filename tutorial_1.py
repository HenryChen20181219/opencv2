import cv2 as cv
import numpy as np


def video_demo():
    capture = cv.VideoCapture(0)  # 打开内置摄像头
    while True:
        ret, frame = capture.read()  # 按帧读取，ret是布尔值，frame是读取的图像，三维矩阵
        frame = cv.flip(frame, 1)
        cv.imshow("video", frame)
        c = cv.waitKey(50)  # 得到键盘的ascll码 esc是27，delay参数表示延时多久切换到下一帧，0表示暂停
        if c == 27:
            break


def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.dtype)
    print(image.size)
    plxel_data = np.array(image)


print("--------Hello Python--------")
src = cv.imread("D:\photo\girl1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
get_image_info(src)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
# cv.imwrite("D:\photo\result.png", gray)
cv.waitKey(0)

video_demo()
cv.destroyAllWindows()
