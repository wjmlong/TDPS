import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math as m
import time
import serial

def phsv(img):
    HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    return HSV

def col_r(image):
    
    red = (0, 0, 255)
    blue = (255,0,0)

    #gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)

    Lower1 = np.array([100,90,90])
    Upper1 = np.array([130,255,255])

    edge_outputr = cv.inRange(image,Lower1,Upper1)

    #cv.imshow("r", edge_outputr)
    output1 = cv.cvtColor(edge_outputr, cv.COLOR_GRAY2RGB)
  
    font = cv.FONT_HERSHEY_DUPLEX
    
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (11, 11), (-1, -1))
    kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (19, 19), (-1, -1))

    eroder = cv.erode(edge_outputr, kernel)
    #cv.imshow("eroder", eroder)
    dilater = cv.dilate(eroder, kernel2)
    #cv.imshow("dilater", dilater)
    
    
    M = cv.moments(dilater)
    if(M["m00"] == 0 or M["m00"] == 0):
        tx = 'cr = no target'
        cXr = -1
        cYr = -1
    else:
        cXr = int(M["m10"] / M["m00"]);
        cYr = int(M["m01"] / M["m00"]);
        tx = 'cr = ''%.2f'%cXr+' %.2f'%cYr
        cv.circle(output1,(cXr,cYr),25,(255,0,255),1)
    cv.putText(output1, tx,(0,25),font,1,(0,255,255),1,8)
    cv.line(output1, (300,0), (300,480), blue, 1, 4)
    cv.line(output1, (340,0), (340,480), blue, 1, 4)
    cv.line(output1, (0,350), (640,350), red, 1, 4)
    cv.imshow("r1", output1)
 
    return cXr,cYr

def drive(rx,ry):
    if(rx != -1):
        print('red detected')
        oper(rx,ry)

def oper(x,y):
    if(y > 350):
        print('stop')
        ser.write('5'.encode("utf-8"))
    elif(x < 300):
        print('turn right')
        ser.write('3'.encode("utf-8"))
    elif(x > 340):
        print('turn left')
        ser.write('1'.encode("utf-8"))
    else:
        print('go forward')
        ser.write('2'.encode("utf-8"))      


cap = cv.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
td = 0
ser = serial.Serial("/dev/ttyAMA0", 9600)
while(True):
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    time_start = time.time()
    ret,frame = cap.read()
    cv.imshow('frame', frame)
    HSV = phsv(frame)
    rx,ry = col_r(HSV)
    drive(rx,ry)
    time_end = time.time()
    td = time_end-time_start
    time_start = 0
    print('time delay = ',td)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()