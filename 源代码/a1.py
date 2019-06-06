import cv2
import numpy as np

img = cv2.imread("C:/Users/hp-pc/Desktop/TDPS/q5.png")
cv2.imshow('image', img)

#cropped=img[0:263,0:350]
#cv2.imshow('cropped', cropped)

HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(HSV)
Lower = np.array([0, 15 ,50])
Upper = np.array([255, 255, 255])
mask = cv2.inRange(HSV, Lower, Upper)
cv2.imshow("HSV", mask)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5), (-1, -1))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (19, 19), (-1, -1))
erode = cv2.erode(mask, kernel)
cv2.imshow("erode", erode)
dilate = cv2.dilate(erode, kernel2)
cv2.imshow("dilate", dilate)

canny = cv2.Canny(dilate, 3, 9, 3)
cv2.imshow("canny", canny)

gblur = cv2.GaussianBlur(canny, (3,3), 4, 4)
cv2.imshow("guassianBlur", gblur)

lines = cv2.HoughLines(gblur, 1, np.pi / 180, 100, 0, 0)
result = img.copy()
cv2.waitKey()
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(result, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv2.imshow('result', result)
cv2.waitKey()
