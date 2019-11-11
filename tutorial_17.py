import cv2
import numpy as np


img = cv2.imread("D:\photo\girl3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 21, 75, 75)
gray = cv2.convertScaleAbs(cv2.Laplacian(gray, cv2.CV_64F))
edges = cv2.Canny(gray, 50, 150)
cv2.imshow("edges", edges)
cv2.waitKey(0)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 38)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

cv2.imshow("houghLine", img)

