import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math as m
import time

def edge_demo(image,t1,c,td):
    
    red = (0, 0, 255)
    blue = (255,0,0)
    blurred = cv.GaussianBlur(image, (7, 7), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    edge_output2 = cv.Canny(gray, t1, 150)#gray法
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
    img = edge_demo(frame,t1,c,td)
    [h,w] = img.shape
    [a,s] = sam(n,h,w,img)
    s1,c = draw(a,s,n) 
    t1 = adj(s1)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    if(c > 420):        
        if(c > 500):
            print(c,'left2')
        else:
            print(c,'left')
    elif(c < 220):
        if(c <150):
             print(c,'right2')
        else:
             print(c,'right')
    else:
        print(c,'middle')

    print('lower limit = ',t1,'the total point = ',s1,'direction = ',c)
    time_end = time.time()
    td = time_end-time_start
    time_start = 0
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()



