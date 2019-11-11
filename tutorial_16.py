import cv2 as cv


def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)

    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)
    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("Color Edge", dst)


src = cv.imread("D:\photo\girl3.jpg")
cv.namedWindow("input_image", cv.WINDOW_NORMAL)
cv.imshow("input_image", src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
