import  cv2
def bi_demo(image):#高斯双边滤波
    dst = cv2.bilateralFilter(src=image, d=0, sigmaColor=100, sigmaSpace=30)
    cv2.imshow('dst',dst)

img = cv2.imread(r'C:\Users\hp-pc\Desktop\q5.png')
bi_demo(img)
cv2.waitKey(0)
cv2.destroyAllWindows()