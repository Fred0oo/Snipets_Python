import os
from os import path
print("debut")
path = r'/Users/fredericquivron/Music'
f = open('somefile.txt', 'w')
list = os.listdir(path)
def getFile(dirpath) :
	listing = os.listdir(dirpath);
	for words in listing:	
		test= os.path.join(dirpath,words)
		if(os.path.isdir(test)):
			getFile(test)
		elif(os.path.isfile(test) and words.endswith("mp3")):
			f.write(test+"\n")
				
for word in list:
	test = os.path.join(path,word)
	if(os.path.isdir(test)):
		getFile(test)
	elif(os.path.isfile(test) and test.endswith("mp3")):
		f.write(test+"\n");