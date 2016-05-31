import os
import sys
from os.path import isfile, join

def populate():
	files = {}
	folders = {}
	new_folders = {}
	path = os.getcwd()
	#read all the files and get all the extentions
	all_dirs = os.listdir(path)
	for folders_file in all_dirs:
		if isfile(join(path , folders_file)):
			#it is a file
			#get the extension of the files
			temp = folders_file.split('.')
			extn = temp[-1];
			files[folders_file] = extn
			print(extn)
			new_folders[extn] = True
		else:
			#it is a directory
			#print folders_file
			folders[folders_file] = True

	#create all the necessary folders
	for f in new_folders:
		if f not in folders:
			#creata a new folder
			os.makedirs(path+'/'+f)

	#move the files
	for f in files:
		# do somethning
		os.rename(path+'/'+f , path+'/' + files[f]+'/'+f)

populate()
