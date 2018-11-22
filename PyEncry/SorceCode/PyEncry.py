import os
import py_compile

os.system("dir/s/b *.py > pyc.txt")
#dir/s 可以搜尋當前資料夾符合該字串檔名的檔案
#dir/b 可以簡單列出檔案列表

pyFile = open("pyc.txt", "r")
print("\n######### PYC tool v0.1 by Rick@20181114 #########")
print("################ Encryption Start ################ \n")
for line in pyFile:
	Offset = line.find('.py') #再次檢查，有py副檔名才會做，其實這邊可以刪掉
	if Offset != -1:
		print(line.split("\n")[0] + " is encrypted") 
		#在dir/s/b產生的txt，每行最後會帶換行字元 \n ，所以使用split的方式來弄掉他。
		py_compile.compile(line.split("\n")[0])
pyFile.close()
os.system("del pyc.txt")
#刪除pyc.txt暫存檔
print("\n################ Encryption  End  ################ \n")
print("You can find pyc file in __pycache__ folder")
