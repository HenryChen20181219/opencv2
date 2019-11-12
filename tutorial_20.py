import cv2 as cv
import numpy as np
from scipy.spatial import distance as dist


# 定义中点坐标运算
def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)


def measure(img):
    # 转灰度
    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    # 图像二值化
    ret, thresh = cv.threshold(gray, 127, 255, 0)
    # 计算黑色方块的4个角点坐标
    contours, hierarchy = cv.findContours(thresh, 1, 2)
    for cnt in contours:
        # 求取轮廓的几何距
        M = cv.moments(cnt)
        # 获取轮廓的外接矩形，x,y是绿框左上角的像数坐标点，w,h是绿框的长，宽
        x, y, w, h = cv.boundingRect(cnt)
        # 计算最小轮廓，红框
        rect = cv.minAreaRect(cnt)
        # 计算红框4个角的像数坐标
        box = cv.boxPoints(rect)
        # 像数是整型，所以将坐标转成整型
        box = np.int0(box)

    if M['m00'] != 0:
        # print(M)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        # 根据几何距获取的中心点，画出中心圆，被蓝线挡了所以看不到
        cv.circle(img, (np.int(cx), np.int(cy)), 2, (0, 255, 255), -1)
        # 画绿框
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # 画红框4个角
        cv.drawContours(img, [box], 0, (0, 0, 255), 2)
        for (x, y) in box:
            cv.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
            # tl左上角像数坐标，tr右上角像数坐标，br右下角像数坐标，bl左下角像数坐标
            (tl, tr, br, bl) = box
            # 计算红框4条边的中心点
            (tltrX, tltrY) = midpoint(tl, tr)
            (blbrX, blbrY) = midpoint(bl, br)
            (tlblX, tlblY) = midpoint(tl, bl)
            (trbrX, trbrY) = midpoint(tr, br)
            # 画点
            cv.circle(img, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
            cv.circle(img, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
            cv.circle(img, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
            cv.circle(img, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
            # 画线连接4个点，也就是图片中2条蓝线

            cv.line(img, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)),
                    (255, 0, 0), 2)
            cv.line(img, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)),
                    (255, 0, 0), 2)
            # 计算中心点的坐标
            dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
            dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))
            # 将像数长度转成实际长度，6.5相当于比例尺，我用的是mm单位，也就是所1mm相当于6.5个像数

            dimA = dA / 6.5
            dimB = dB / 6.5
            # 将计算结果打印在原图上，也就是黄色的内容

            cv.putText(img, "{:.1f}mm".format(dimA),
                       (int(tltrX - 15), int(tltrY - 10)), cv.FONT_HERSHEY_SIMPLEX,
                       0.65, (0, 255, 255), 2)
            cv.putText(img, "{:.1f}mm".format(dimB),
                       (int(trbrX + 10), int(trbrY)), cv.FONT_HERSHEY_SIMPLEX,
                       0.65, (0, 255, 255), 2)
    cv.imshow("mo", img)


# 启动摄像头，设置分辨率
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 600)
while (cap.isOpened()):
    ret, frame = cap.read()
    img = cv.flip(frame, -1)
    # 创建GUI窗口,形式为自适应
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    # 通过名字将图像和窗口联系
    cv.imshow("input image", img)
    measure(img)
    # 如果按下P键，将保存图片到D:/Program Files/jawa.jpg并退出
    if cv.waitKey(1) & 0xFF == ord('p'):
        cv.imwrite("D:/Program Files/jawa.jpg", img)
    break
