import time
from datetime import datetime
import serial

ser = serial.Serial("/dev/ttyAMA0",9600,timeout = 1)

times =datetime.now().strftime('%Y-%m-%d %H:%M:%S')
a = '\n Team 20\n Name of member:\n Xu zhihan\n Jiang Zhouhang\n Li Ke\n Mou Ruiqiang\n Ai chenghao\n Wang Sicheng\n Wu Jiaming\n Cheng Hongjing'

while 1:
    response = ser.read()
    print(response)
    if(response == 's'):
        ser.write("%s %s",times,a)




