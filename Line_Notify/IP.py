import requests
import os

os.system('ipconfig > ip.txt')
pyFile = open("ip.txt", "r")
for line in pyFile:
	Offset = line.find('IPv4')
	if Offset != -1:
		#print(line)
		SendIP = 'Your IP is' + line.split(":")[1]
		my_data = (('value1', SendIP ), ('value2', 'key1'))
		r = requests.post('https://maker.ifttt.com/trigger/Line1121/with/key/dvPQTSVDocYi0RHKPfPUAs', data = my_data)
pyFile.close()
os.system('del ip.txt')
		