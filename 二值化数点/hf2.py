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
  

def adj(img):
   
    img_mean_R = []
    img_mean_G = []
    img_mean_B = []

    img_mean_R.append(np.mean(img[:,range(0,320),0]))
    img_mean_G.append(np.mean(img[:,range(0,320),1]))
    img_mean_B.append(np.mean(img[:,range(0,320),2]))

    R_mean = np.mean(img_mean_R)
    G_mean = np.mean(img_mean_G)
    B_mean = np.mean(img_mean_B)
    
    img_mean_R1 = []
    img_mean_G1 = []
    img_mean_B1 = []

    img_mean_R1.append(np.mean(img[:,range(320,640),0]))
    img_mean_G1.append(np.mean(img[:,range(320,640),1]))
    img_mean_B1.append(np.mean(img[:,range(320,640),2]))

    R1_mean = np.mean(img_mean_R1)
    G1_mean = np.mean(img_mean_G1)
    B1_mean = np.mean(img_mean_B1)

    Rd =int( (R_mean + R1_mean)*0.5)
    Gd =int( (G_mean + G1_mean)*0.5)
    Bd = int((B_mean + B1_mean)*0.5)

    Lower = np.array([Rd, Gd, Bd])
    
    return Lower

def bin(img,c,td,Lower):
    
    red = (0, 0, 255)
    blue = (255,0,0)
    
    Upper = np.array([255, 255, 255])
    mask = cv.inRange(img, Lower, Upper)
    cv.imshow("HSV", mask)

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5), (-1, -1))
    kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (19, 19), (-1, -1))
    erode = cv.erode(mask, kernel)
    cv.imshow("erode", erode)
    dilate = cv.dilate(erode, kernel2)
    cv.imshow("dilate", dilate)
    edge_output3 = cv.cvtColor(dilate, cv.COLOR_GRAY2RGB)
   
    font = cv.FONT_HERSHEY_DUPLEX
    c2 = int(c)
    cv.line(edge_output3,(c2,0),(c2,480),red,3)
    cv.line(edge_output3,(220,0),(220,480),blue,1)
    cv.line(edge_output3,(420,0),(420,480),blue,1)

    c1 = 'direction = ''%.2f' %c
    cv.putText(edge_output3, c1,(0,25),font,1,(0,255,255),1,8)

    td = 'delay = ''%.2f' %td
    cv.putText(edge_output3, td,(0,85),font,1,(0,255,255),1,8)
    cv.imshow("Canny Edge3", edge_output3)
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
    l = adj(frame)
    img = bin(frame,c,td,l)
    img = cv.Canny(img, 3, 9, 3)
    cv.imshow('Canny',img)    

    dline(img,frame)

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('the L = ',l,'delay = ',td)
    time_end = time.time()
    td = time_end-time_start
    time_start = 0
    k = cv.waitKey(30) & 0xff
    if k == 27:
         break
cap.release()
cv.destroyAllWindows()


