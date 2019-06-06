﻿import numpy as np
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
  


def prep(img):
    HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    H, S, V = cv.split(HSV)
    Lower = np.array([0, 30 ,100])
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


def edge_demo(image,t1,c,td):
    
    red = (0, 0, 255)
    blue = (255,0,0)
    blurred = cv.GaussianBlur(image, (7, 7), 0)
    #gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    edge_output2 = cv.Canny(blurred, 3, 9, 3)#gray法
    edge_output3 = cv.cvtColor(edge_output2, cv.COLOR_GRAY2RGB)

    
    font = cv.FONT_HERSHEY_DUPLEX
    c2 = int(c)
    cv.line(edge_output3,(c2,0),(c2,480),red,3)
    cv.line(edge_output3,(220,0),(220,480),blue,1)
    cv.line(edge_output3,(420,0),(420,480),blue,1)

    c1 = 'direction = ''%.2f' %c
    cv.putText(edge_output3, c1,(0,25),font,1,(0,255,255),1,8)
    t = 'lower limit = ''%d'%t1
    cv.putText(edge_output3, t,(0,55),font,1,(0,255,255),1,8)
    td = 'delay = ''%.2f' %td
    cv.putText(edge_output3, td,(0,85),font,1,(0,255,255),1,8)
    cv.imshow("Canny Edge3", edge_output3)
    return edge_output2

def sam(n,h,w,img):
    a = [0 for i in range(1,n)]
    s = [0 for i in range(1,n)]
    for x in range(1,n):
        s1 = int(m.floor(w/n*x))
        s2 = s1 + int(m.floor(w/5/n))
        s[x - 1] = (s1 + s2)/2
        for i in range(s1, s2):
              for j in range(int(m.floor(h/2)),h):
                    if img[j,i] > 100:
                         a[x - 1] = a[x - 1] + 1

    return [a, s]
    
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
           cv.line(graph,(x,480),(x,480 - 8*a[i]),blue,3)

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

def adj(s):
    if(s >= 290)and(s <= 320):
        t1 = 50
    elif(s >= 250)and(s < 290):
        t1 = 30
    elif(s > 320)and(s <= 400):
        t1 = 70
    elif(s < 250):
        t1 = 20
    elif(s > 400):
        t1 = 100
    return t1    


cap = cv.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
t1 = 50
c = 320
td = 0
while(True):
    
    time_start = time.time()
    n = 50
    ret,frame = cap.read()
    #cv.imshow('frame', frame)
    frame1 = prep(frame)
    img = edge_demo(frame1,t1,c,td)
    [h,w] = img.shape
    [a,s] = sam(n,h,w,img)
    s1,c = draw(a,s,n) 
    t1 = adj(s1)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    if(c > 420):        
        print(c,'left')
    elif(c < 220):
        print(c,'right')
    else:
        print(c,'middle')
    
    dline(img,frame)
    print('lower limit = ',t1,'the total point = ',s1,'direction = ',c)
    time_end = time.time()
    td = time_end-time_start
    time_start = 0
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()



