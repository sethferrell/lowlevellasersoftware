#!/usr/bin/env python

import serial
import os, sys

class portSetup():
	def __init__(self, port):
		self.com = serial.Serial(port, 115200)
		
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
	ascii = sys.argv[1]
	portname = sys.argv[2]
	main(ascii, portname)


