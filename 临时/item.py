import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread(r'C:\Users\hp-pc\Desktop\2.png')
#print(img[598,30])
[h,w,x] = img.shape
print(h,w)
a = [0 for i in range(w)]
b = range(w)

for i in range(0,w):
      for j in range(0,h):
            if (img[j,i] > [100,100,100]).any():
                 a[i] = a[i] + 1
a = np.array(a)
b = np.array(b)

av = np.mean(a)
for i in range(0,w):
       if(a[i]<av):
             a[i] = 0

c = np.multiply(a,b)
c = sum(c/sum(a))
print(c)
#print(a)
plt.bar(b,a,label='graph 1')      
plt.bar(c,max(a), facecolor='red')
plt.show()


