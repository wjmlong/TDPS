import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math as m

def edge_demo(image):
    blurred = cv.GaussianBlur(image, (7, 7), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    edge_output2= cv.Canny(gray, 50, 150)#gray法
    cv.imshow("Canny Edge2", edge_output2)
    return edge_output2

def sam(n,h,w,img):
    a = [0 for i in range(1,n)]
    s = [0 for i in range(1,n)]
    for x in range(1,n):
        s1 = m.floor(w/n*x)
        s2 = s1 + m.floor(w/10/n)
        s[x - 1] = (s1 + s2)/2
        for i in range(s1, s2):
              for j in range(0,m.floor(h/2)):
                    if img[j,i] > 100:
                         a[x - 1] = a[x - 1] + 1

    return [a, s]
    
def draw(a,s,n):
    #print(a)
    av = np.mean(a)
    s = sum(a)
    for i in range(0,n - 1):
           if(a[i]<av):
                 a[i] = 0
    c = np.multiply(a,s)
    c = sum(c/sum(a))
    if(c > 400):        
        print(c,'right')
    elif(c < 200):
        print(c,'left')
    else:
        print(c,'middle')
    
    print(s)
   
    #plt.plot(s,a,'g-')    
    #plt.plot([c,c],[0,max(a)],'red') 
    #plt.pause(0.1)
    #plt.cla()

cap = cv.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    n = 20
    ret,frame = cap.read()
    #cv.imshow('frame', frame)
    img = edge_demo(frame)
    [h,w] = img.shape
    [a,s] = sam(n,h,w,img)
    draw(a,s,n) 
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()



