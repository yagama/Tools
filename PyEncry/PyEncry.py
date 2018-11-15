import os
import py_compile

os.system("dir/s/b *.py > pyc.txt")
pyFile = open("pyc.txt", "r")
print("\n######### PYC tool v0.1 by Rick@20181114 #########")
print("################ Encryption Start ################ \n")
for line in pyFile:
	Offset = line.find('.py')
	if Offset != -1:
		print(line.split("\n")[0] + " is encrypted")
		py_compile.compile(line.split("\n")[0])
pyFile.close()
os.system("del pyc.txt")
print("\n################ Encryption  End  ################ \n")
print("You can find pyc file in __pycache__ folder")
