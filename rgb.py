import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math as m
import time
import serial
    

def col_r(image):
    
    red = (0, 0, 255)
    blue = (255,0,0)

    #gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)

    Lower1 = np.array([130,90,90])
    Upper1 = np.array([170,255,255])
    Lower2 = np.array([25,100,100])
    Upper2 = np.array([35,255,255])
    Lower3 = np.array([100,90,90])
    Upper3 = np.array([130,255,255])
    edge_outputr = cv.inRange(image,Lower1,Upper1)
    edge_outputg = cv.inRange(image,Lower2,Upper2)
    edge_outputb = cv.inRange(image,Lower3,Upper3)
    #cv.imshow("r", edge_outputr)
    output1 = cv.cvtColor(edge_outputr, cv.COLOR_GRAY2RGB)
    #cv.imshow("g", edge_outputg)
    output2 = cv.cvtColor(edge_outputg, cv.COLOR_GRAY2RGB)
    #cv.imshow("b", edge_outputb)
    output3 = cv.cvtColor(edge_outputb, cv.COLOR_GRAY2RGB)
    #edge_output2 = cv.Canny(blurred, 50, 50)#gray法
    
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
    cv.line(output1, (0,400), (640,400), red, 1, 4)
    cv.imshow("r1", output1)
    

    erodeg = cv.erode(edge_outputg, kernel)
    #cv.imshow("erodeg", erodeg)
    dilateg = cv.dilate(erodeg, kernel2)
    #cv.imshow("dilateg", dilateg)
    
    M = cv.moments(dilateg)
    if(M["m00"] == 0 or M["m00"] == 0):
        tx = 'cg = no target'
        cXg = -1
        cYg = -1
    else:
        cXg = int(M["m10"] / M["m00"]);
        cYg = int(M["m01"] / M["m00"]);
        tx = 'cg = ''%.2f'%cXg+' %.2f'%cYg
        cv.circle(output2,(cXg,cYg),25,(255,0,255),1)
    cv.putText(output2, tx,(0,25),font,1,(0,255,255),1,8)
    cv.line(output2, (300,0), (300,480), blue, 1, 4)
    cv.line(output2, (340,0), (340,480), blue, 1, 4)
    cv.line(output2, (0,400), (640,400), red, 1, 4)
    cv.imshow("g1", output2)
    
    erodeb = cv.erode(edge_outputb, kernel)
    #cv.imshow("erodeb", erodeb)
    dilateb = cv.dilate(erodeb, kernel2)
    #cv.imshow("dilateb", dilateb)

    M = cv.moments(dilateb)
    if(M["m00"] == 0 or M["m00"] == 0):
        tx = 'cb = no target'
        cXb = -1
        cYb = -1
    else:
        cXb = int(M["m10"] / M["m00"]);
        cYb = int(M["m01"] / M["m00"]);
        tx = 'cb = ''%.2f'%cXb+' %.2f'%cYb
        cv.circle(output3,(cXb,cYb),25,(255,0,255),1)
    cv.putText(output3, tx,(0,25),font,1,(0,255,255),1,8)
    cv.line(output3, (300,0), (300,480), blue, 1, 4)
    cv.line(output3, (340,0), (340,480), blue, 1, 4)
    cv.line(output3, (0,400), (640,400), red, 1, 4)
    cv.imshow("b1", output3)

    return cXr,cYr,cXg,cYg,cXb,cYb

def phsv(img):
    HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    return HSV
    
def drive(rx,ry,gx,gy,bx,by):
    a = 0
    if(rx != -1):
        print('red detected')
        ser.write('6'.encode("utf-8"))
        a = 6
        oper(rx,ry,a)
    if(gx != -1):
        print('green detected')
        ser.write('7'.encode("utf-8"))
        a = 7
        oper(gx,gy,a)
    if(bx != -1):
        print('blue detected')
        ser.write('8'.encode("utf-8"))
        a = 8
        oper(bx,by,a)
        return a
        

def oper(x,y,a):
    if(y > 400):
        
        print('stop')
        ser.write('5'.encode("utf-8"))
        