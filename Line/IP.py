import requests
import os

os.system('ipconfig > ip.txt')
keyFile = open("key.txt", "r")
for line in keyFile:
	IFTTT = line.split("\n")[0]
keyFile.close()
#Key example: https://maker.ifttt.com/trigger/Line1121/with/key/dvPQTSVDocYi0RHKPfPUAs

pyFile = open("ip.txt", "r")
for line in pyFile:
	Offset = line.find('IPv4')
	if Offset != -1:
		#print(line.split(":")[0])
		SendIP = 'Your IEC IP is' + line.split(":")[1]
		my_data = (('value1', SendIP ), ('value2', 'key1'))
		r = requests.post( IFTTT , data = my_data)
		#print(IFTTT)
pyFile.close()
os.system('del ip.txt')
		