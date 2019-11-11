import numpy as np

import cv2 as cv


def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width:%s,height:%s,channels:%s"%(width, height, channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv

    cv.imshow("pixels_demo", image)


def create_image():
    img = np.zeros([400, 400, 3], np.uint8)
    img[:, :, 0] = np.ones([400, 400])*255
    cv.imshow("new image", img)

    # m1 = np.ones([3, 3], np.float64)
    # m1.fill(1222.388)
    # print(m1)


print("--------Hello Python--------")
src = cv.imread("D:\photo\girl1.jpg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
t1 = cv.getTickCount()
access_pixels(src)
t2 = cv.getTickCount()
time = (t2 - t1)/cv.getTickFrequency()
print(time)
create_image()
cv.waitKey(0)

