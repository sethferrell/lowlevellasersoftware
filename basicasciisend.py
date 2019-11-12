import serial                           # import the module 

ComPort = serial.Serial('/dev/ttyUSB0') # open ttyUSB0 

ComPort.baudrate = 9600                 # set Baud rate 
ComPort.bytesize = 8                    # Number of data bits = 8
ComPort.parity = 'N'                    # No parity
ComPort.stopbits = 1                    # Number of Stop bits = 1

#Write character 'A' to serial port                            
data = bytearray(b'A')                  # Convert Character to byte array
No = ComPort.write(data)                # Write data to serial port

ComPort.close()                  #Close the Serial port
