import cv2 as cv


def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.namedWindow("input_image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input_image", gray)
    dst = cv.equalizeHist(gray)
    cv.namedWindow("equalHist_demo", cv.WINDOW_AUTOSIZE)
    cv.imshow("equalHist_demo", dst)


def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(5, (8, 8))
    dst = clahe.apply(gray)
    cv.namedWindow("clahe_demo", cv.WINDOW_AUTOSIZE)
    cv.imshow("clahe_demo", dst)


src = cv.imread("")


equalHist_demo(src)
clahe_demo(src)

cv.waitKey(0)
cv.destroyAllWindows()
