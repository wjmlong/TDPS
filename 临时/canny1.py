import numpy as np
import cv2 as cv
import time

def edge_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    edge_output1= cv.Canny(gray, 50, 150)#gray法
    cv.imshow("Canny Edge1", edge_output1)

    #cv.imshow("Canny Edge2", edge_output2)
    #dst = cv.bitwise_and(image, image, mask= edge_output2)
    #cv.imshow("Color Edge2", dst)#gray法

cap = cv.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    ts = time.time()
    ret,frame = cap.read()
    #frame = cv.flip(frame, -1) # Flip camera vertically
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame)
    #cv.imshow('gray', gray)
    edge_demo(frame)
    te = time.time()
    td = te - ts
    print(td)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

