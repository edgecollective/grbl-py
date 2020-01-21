import serial
import requests 
import time

PORT='/dev/ttyUSB0'

s=serial.Serial(PORT,115200,timeout=1)

s.readline()
s.readline()
s.readline()

def x(steps_mm):
    s.write('G91\r\n')
    print(s.readline().strip())
    s.write('G0 X'+str(steps_mm)+'\r\n')
    print(s.readline().strip())
    s.write('G90\r\n')
    print(s.readline().strip())

def y(steps_mm):
    s.write('G91\r\n')
    print(s.readline().strip())
    s.write('G0 Y'+str(steps_mm)+'\r\n')
    print(s.readline().strip())
    s.write('G90\r\n')
    print(s.readline().strip())

def z(steps_mm):
    s.write('G91\r\n')
    print(s.readline().strip())
    s.write('G0 Z'+str(steps_mm)+'\r\n')
    print(s.readline().strip())
    s.write('G90\r\n')
    print(s.readline().strip())

# make it go

x(1)
y(3)
z(-2)