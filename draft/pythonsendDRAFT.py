#!/usr/bin/env python

import serial
import os, sys

class portSetup():
	def __init__(self, port):
		self.com = serial.Serial(port, 115200)	#Can we make the baudrate higher?
		
	def sendData(self, data):
		data += "\r\n"
		self.com.write(data.encode())
def main(ascii, portname):
	com = portSetup(portname)
	with open(ascii, 'r') as ar:
		for line in ar:
			data = repr(line)
			com.sendData(line)
			print(data)

if __name__ == '__main__':
	ascii = sys.argv[1] 		#Set to the file path of the attached "IRV" ascii document
	portname = sys.argv[2]		#Set to the USB port connected to Linux ex: /dev/USB0
	main(ascii, portname)		#Launch program as a command in Linux, call the file and give the two argument listed above


