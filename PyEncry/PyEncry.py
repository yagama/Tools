import os
import py_compile

os.system("dir/s/b *.py > pyc.txt")
pyFile = open("pyc.txt", "r")
print("\n ######## Encryption Start ######## \n")
for line in pyFile:
	Offset = line.find('.py')
	if Offset != -1:
		print(line.split("\n")[0] + " is encrypted")
		py_compile.compile(line.split("\n")[0])
pyFile.close()
print("\n ######## Encryption  End  ######## \n")
print("You can find pyc file in __pycache__ folder")