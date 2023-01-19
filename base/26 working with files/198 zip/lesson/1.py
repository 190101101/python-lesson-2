import zipfile
import os

p1 = zipfile.ZipFile('files/2.zip', 'r')

for i in p1.filelist:
	print(i)


p1.extractall()	
p1.close()