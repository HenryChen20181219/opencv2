import cv2

img = cv2.imread("D:\photo\girl3.jpg", 0)
template = cv2.imread("D:\photo\girl3.jpg", 0)
h, w = template.shape[:2]


res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
left_top = max_loc
right_bottom = (left_top[0]+2, left_top[2]+h)
cv2.rectangle(img, left_top, right_bottom, 255, 2)
