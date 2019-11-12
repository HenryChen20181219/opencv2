import cv2

img = cv2.imread('D:\photo\girl3.jpg')  # 读取一张图片

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将图片转化成灰度

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")  # 加载级联分类器模型
face_cascade.load(r'E:\TSBrowserDownloads\haarcascade_frontalface_alt2.xml')  # 一定要告诉编译器文件所在的具体位置
'''此文件是opencv的haar人脸特征分类器'''
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# 在原先的彩图上画出包围框（蓝色框，边框宽度为2）
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# 显示图片
cv2.imshow('img', img)
cv2.waitKey()
