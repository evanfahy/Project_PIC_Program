#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import serial

print "Sending Test Parameters."

ser = serial.Serial(
 port='/dev/ttyUSB0',
 baudrate = 10417,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)

time.sleep(.3)

#open file to parse data
file = open('/home/pi/NetBeansProjects/mainProject/dist/testData.txt', 'r') 

ser.flushInput()
ser.flushOutput()

rx = 0
rx1 = 0
tx = 0
rxFlag = 0
PoW = 0
cycle = 0

#Connecting with PIC
try:
	#data = "test"
	ser.write("3")
	time.sleep(.01)
        #Reading from UART
        print "Reading....."
        rx = 0
        while (rxFlag != 1):
                if ser.inWaiting()>0:
                        rx = ser.readline()
                        rxFlag =  1
			break

	print "RX: "
	print (rx)


except:
	print "Error: Could not sent PoW value."

try:
	if "3" in rx:
		print "Connection 1 Established"
	else:
		print "Connection 1 is bad"
		
except:
	print "Error!"

#Parse POW from data.txt and send to PIC
try:
	fileRead = file.readline()
	print ("Read from inputData.txt: " + fileRead)
	parseArray = fileRead.split("/")

	print parseArray[2]
	PoWArray = parseArray[2]
	PoWArray = PoWArray.split(":")
	PoW = PoWArray[1]

	print parseArray[3]
	cycleArray = parseArray[3]
	cycleArray = cycleArray.split(":")
	cycle = cycleArray[1]

	print ("PoW = " + PoW)
	print ("Number of cycles = " + cycle)
	ser.flushInput()
	time.sleep(1)
except:
	print "Error: Could not read file."

try:
	ser.write(PoW)
	time.sleep(.01)
        #Reading from UART
        print "Reading....."
        rx1 = 0
	rxFlag = 0
        while (rxFlag != 1):
                if ser.inWaiting()>0:
                        rx1 = ser.readline()
                        rxFlag =  1
			break

	print ("PoW: " + (rx1))
	time.sleep(1)

except:
	print "Error: Could not send PoW value."


try:
        ser.write(cycle)
        time.sleep(.01)
        #Reading from UART
        print "Reading....."
        rx1 = 0
        rxFlag = 0
        while (rxFlag != 1):
                if ser.inWaiting()>0:
                        rx1 = ser.readline()
                        rxFlag =  1
                        break

        print ("Cycles: " + (rx1))
	time.sleep(1)

except:
        print "Error: Could not send PoW value."



finally:
	ser.close()
	file.close()

