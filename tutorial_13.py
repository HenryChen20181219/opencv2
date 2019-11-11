import cv2 as cv
import numpy as np


def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:cw+col]
            print(np.std(roi), np.mean(roi))
            ret, dst = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
            gray[row:row+ch, col:cw+col] = dst
            print(np.std(dst), np.mean(dst))
    cv.imshow("big_image_binary", gray)
    cv.imread("D:\photo\girl3.jpg", gray)

    print("---------Hi Python")
    src = cv.imread("D:\photo\girl3.jpg")
    cv.namedWindow("input_image", src)
    big_image_binary(src)
    cv.waitKey(0)
    cv.destroyAllWindows()


def big_image_binary(image):
    print(image.shape)
    cw, ch = 128, 128
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row:row+ch, col:col+cw]
            dev = np.std(roi)
            avg = np.mean(roi)
            if dev < 15 and avg > 200:
                gray[row:row+ch, col+cw] = 0
            else:
                ret, binary = cv.threshold(roi, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
                gray[row:row+ch, col:col+cw] = binary
                print(np.std(binary), np.mean(binary))
    cv.imwrite("binary.jpg", gray)


