import serial
# import time

with serial.Serial('COM3', 9600, timeout=5) as ser:
    #x = ser.read()
    s = ser.read(50)
    #line = ser.readline()
    print(s.decode("utf-8"))
