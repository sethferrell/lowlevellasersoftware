#!/usr/bin/env python

import serial

def sendFile(port, filename)

	com = serial.Serial(port)
	textfile = open(filename, 'r')
	data = textfile.read()

	no = com.write(data)

	textfile.close()

sendFile(/dev/tnt1, script.txt)
print(com.name)
