﻿import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img=cv2.imread(r'C:\Users\hp-pc\Desktop\11.jpg')
imgblur = cv2.GaussianBlur(img, (7,7) ,0)
gray=cv2.cvtColor(imgblur,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,140,150,apertureSize=7)
minLineLength=100
maxLineGap=10
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow("edge",edges)
cv2.imshow("image",img)
cv2.waitKey(0)