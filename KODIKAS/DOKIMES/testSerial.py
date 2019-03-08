import serial

ser = serial.Serial('/dev/ttyUSB1',9600)
s = [0]
while True:
#	read_serial=ser.readline()
	s[0] = str( (ser.read(),16))
	print( s[0])
#	print ("aaa")
#	print(read_serial)
