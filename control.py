import serial
ser = serial.Serial("/dev/ttyAMA0",9600)
while 1:
   c = input('the direction =')
   if c == 'a':
       for i in range(0,2):
          print(c,'left')
          ser.write('3'.encode('utf-8'))
   if c == 'd':
       for i in range(0,2):
          print(c,'right')
          ser.write('1'.encode('utf-8'))
   if c == 'w':
       for i in range(0,2):
          print(c,'forward')
          ser.write('2'.encode('utf-8'))
   if c == 'b':
       for i in range(0,10):
           print(c,'boost')
           ser.write('2'.encode('utf-8'))
   if c == 'v':
       for i in range(0,12):
           print(c,'boost left')
           ser.write('3'.encode('utf-8'))
   if c == 'n':
       for i in range(0,12):
           print(c,'boost right')
           ser.write('1'.encode('utf-8'))
