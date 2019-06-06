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
    except:
            cv.imshow('frame1',frame)
 
'''
def adj(img,w):
   
   imgr = img[:,:,0]
   imgg = img[:,:,1]
   imgb = img[:,:,2]
   q1, dst1 = cv.threshold(imgr, 0, 255, cv.THRESH_OTSU)
   q2, dst2 = cv.threshold(imgg, 0, 255, cv.THRESH_OTSU)
   q3, dst3 = cv.threshold(imgg, 0, 255, cv.THRESH_OTSU)
   
   cv.imshow('r',dst1)
   cv.imshow('g',dst2)
   cv.imshow('b',dst3)

   q = np.array([int(q1),int(q2),int(q3)])
   print(q)
   return q
'''
def adj(img,w):

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

def bin(img,HSV,h,s,v):
    
    red = (0, 0, 255)
    blue = (255,0,0)
    
    Lower = np.array([30,20,100])
    Upper = np.array([255,255,255])

    mask = cv.inRange(HSV, Lower,Upper)
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

def draw(a,s,n):
    blue = (255,255,0)
    #print(a)
    av = np.mean(a)
    s1 = sum(a)
    graph = np.zeros((480, 640, 3), dtype="uint8")
    for i in range(0,n - 1):
           if(a[i]<av):
                 a[i] = 0
           x =  int(640/(n + 1)*(i + 1))
           cv.line(graph,(x,480),(x,480 - int(a[i]/20)),blue,3)

    if s1 == 0:
        c = 320
    else: 
        c = np.multiply(a,s)
        c = sum(c/s1)
    ci = int(c)

    cv.line(graph,(ci,0),(ci,480),(0,0,255),3)
    cv.imshow("graph",graph)
    #plt.plot(s,a,'-g')    
    #plt.plot([c,c],[0,max(a)],'red') 
    #plt.pause(0.1)
    #plt.cla()
    return s1,c


frame = cv.imread("C:/Users/hp-pc/Desktop/TDPS/q5.png")

cv.imshow('B',frame)
[h,w,n] = frame.shape
print(h,w,n)
h,s,v,HSV = adj(frame,w)
img = bin(frame,HSV,h,s,v)
img = cv.Canny(img, 3, 9, 3)
cv.imshow('Canny',img)    

dline(img,frame)

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
#print('the L = ',l)

cv.waitKey(0)
cv.destroyAllWindows()