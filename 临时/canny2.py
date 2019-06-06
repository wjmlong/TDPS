import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    edge_output2= cv.Canny(gray, 50, 150)#gray法
    cv.imshow("Canny Edge2", edge_output2)
    return edge_output2

def cal(img,h,h0,a,b):
    for i in range(0,w):
          for j in range(h,h + h0 - 1):
                if img[j,i] > 100:
                     a[i] = a[i] + 1
    a = np.array(a)
    b = np.array(b)

    av = np.mean(a)%remove te distribution
    for i in range(0,w):
           if(a[i]<av):
                 a[i] = 0

    c = np.multiply(a,b)
    c = sum(c/sum(a))

    print(c)
    return [a,c,h = h +h0] 

def sta(img,h,h0):
    #print(img[598,30])
    [h,w] = img.shape
    print(h,w)
    a = [0 for i in range(w)]
    b = range(w)
    h0 = floor(h/4) - 1
 

    #print(a)
    plt.plot(b,a,'g-')    
    plt.plot([c,c],[0,max(a)],'red') 
    plt.pause(0.1)
    plt.cla()

cap = cv.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    ret,frame = cap.read()
    #frame = cv.flip(frame, -1) # Flip camera vertically
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame)
    #cv.imshow('gray', gray)
    img = edge_demo(frame)
    sta(img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

