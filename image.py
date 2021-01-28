from collections import defaultdict
import os
import sys
import hashlib
from . import utility

def RemoveSimilarImage(folder_path, hash = hashlib.sha1):
	"""This funtion will find the similar images and than remove one of the two similar images.
	Store the size of each file and if two file have same size it will create a hash value of it's meta
	data and if the hash value also mathces than it will check the complete hash value of the file.
	If hash value of two files matches than they are similar.
	"""
	file_size = defaultdict(list)
	hash_meta = defaultdict(list)
	hash_full = dict()


	for dirpath, dirname, files in os.walk(folder_path):
		""" For all the files in that particular path """
		for file in files:
			#Actual path of the file
			clear_path = os.path.join(dirpath, file)
			clear_path = os.path.realpath(clear_path)
			file_size[os.path.getsize(file)].append(clear_path)



if __name__ == '__main__':
	""" If this file is imported in another file than this part of the code will not execute. """
	if sys.argv[1]:
		RemoveSimilarImage(sys.argv[1])
	else:
		print("Path of the image folder is missing.")
