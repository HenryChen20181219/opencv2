import cv2 as cv
from matplotlib import pyplot as plt


def plot(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show("直方图")


def image_his(image):
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv.calcHist(image, [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()

