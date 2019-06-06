import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math as m
import time


def dline(img,frame):
    lines = cv.HoughLines(img, 1, np.pi / 180, 70, 70, 40)
    try:
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
            cv.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 1)
            cv.imshow('frame1',frame)
            print(theta)
    except:
            cv.imshow('frame1',frame)


def adj(img):
    

    HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    imgh = HSV[:,:,0]
    imgs = HSV[:,:,1]
    imgv = HSV[:,:,2]
    
    s, dst = cv.threshold(imgs, 0, 255, cv.THRESH_OTSU)
    h, dst = cv.threshold(imgh, 0, 255, cv.THRESH_OTSU)
    v, dst = cv.threshold(imgv, 0, 255, cv.THRESH_OTSU)
    print(h,s,v)
    cv.imshow('dst',dst)
    return int(h),int(s),int(v),HSV
"""
def bin(img,HSV,h,s,v):
    
    red = (0, 0, 255)
    blue = (255,0,0)
    
    Lower = np.array([0,s,0])
    Upper = np.array([255,255, 255])

    mask = cv.inRange(HSV, Lower,Upper)
    mask[:,15] = 50
    cv.imshow("HSV", mask)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))
    kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (19, 19), (-1, -1))
    erode = cv.erode(mask, kernel)
    cv.imshow("erode", erode)
    dilate = cv.dilate(erode, kernel2)
    cv.imshow("dilate", dilate)
    edge_output3 = cv.cvtColor(dilate, cv.COLOR_GRAY2RGB)
   
    font = cv.FONT_HERSHEY_DUPLEX

    return dilate
"""
def prep(img,HSV,h,s,v):
    Lower = np.array([h, s ,v])
    Upper = np.array([255, 255, 255])
    mask = cv.inRange(HSV, Lower, Upper)
    cv.imshow("HSV", mask)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))
    kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (19, 19), (-1, -1))
    erode = cv.erode(mask, kernel)
    cv.imshow("erode", erode)
    dilate = cv.dilate(erode, kernel2)
    cv.imshow("dilate", dilate)

    return dilate


cap = cv.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    ret,frame = cap.read()
    h,s,v,HSV = adj(frame)
    frame1 = prep(frame,HSV,h,s,v)
    frame1 = cv.Canny(frame1, 3, 9, 3)#gray法
    dline(frame1,frame)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()



