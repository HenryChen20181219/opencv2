import cv2 as cv
import numpy as np


def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down_"+str(i), dst)
        temp = dst.copy()
    return pyramid_images


def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)
    level = len(pyramid_images)
    for i in range(level-1, -1, -1):
        if i - 1 < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[0:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_down_"+str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[0:2])
            cv.imshow("lapalian_down_" + str(i), lpls)


if __name__ == "__main__":
    img = cv.imread("")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
