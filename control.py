import serial
import requests 
import time

PORT='/dev/ttyUSB0'

s=serial.Serial(PORT,115200,timeout=.5)

s.readline()
s.readline()
s.readline()

def x(steps_mm):
    print(s.readline().strip())
    s.write('G91\n')
    print(s.readline().strip())
    s.write('G0 X'+str(steps_mm)+'\n')
    print(s.readline().strip())
    s.write('G90\n')
    print(s.readline().strip())

def y(steps_mm):
    print(s.readline().strip())
    s.write('G91\n')
    print(s.readline().strip())
    s.write('G0 Y'+str(steps_mm)+'\n')
    print(s.readline().strip())
    s.write('G90\n')
    print(s.readline().strip())

def z(steps_mm):
    print(s.readline().strip())
    s.write('G91\n')
    print(s.readline().strip())
    s.write('G0 Z'+str(steps_mm)+'\n')
    print(s.readline().strip())
    s.write('G90\n')
    print(s.readline().strip())

def drill_on():
    print(s.readline().strip())
    print(s.readline().strip())
    s.write('M3 S10000\n')
    print(s.readline().strip())

def drill_off():
    print(s.readline().strip())
    print(s.readline().strip())
    s.write('M5\n')
    print(s.readline().strip())

# make it go


x(1)
y(3)
z(2)
drill_on()
time.sleep(2)
drill_off()