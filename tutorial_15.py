import cv2 as cv


def sobel_demo(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)

    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)

    cv.imshow("gradient_x", gradx)
    cv.imshow("gradient_y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)


src = cv.imread("D:\photo\girl3.jpg")
cv.namedWindow("input_image", cv.WINDOW_NORMAL)
cv.imshow("input_image", src)
sobel_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
