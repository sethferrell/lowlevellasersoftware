#!/usr/bin/env python

import serial

com = serial.Serial('/dev/tnt1')

textfile = open('scipt.txt', 'r')

data = textfile.read()

no = com.write(data)

textfile.close()

print(com.name)
