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
	removed_files = 0


	for dirpath, dirname, files in os.walk(folder_path):
		""" For all the files in that particular path classifying files on the basis of their
			acutal size occupied on the disk.
		"""
		for file in files:
			#Actual path of the file
			clear_path = os.path.join(dirpath, file)
			clear_path = os.path.realpath(clear_path)
			file_size[os.path.getsize(file)].append(clear_path)

	for size_of_file, files in file.size.item():
		""" If only one file is present of a particular size than no similar image will be present.
			Or else will generate hash value of its meta data and classify files on this generated hash value.
		"""
		if len(files) < 2:
			continue
		for file in files:
			meta_hash = generate_hash(file, True)
			hash_meta[meta_hash].append(file)

	for meta_hash, files in hash_meta.item():
		"""If only one file is present of a particular meta_hash we will ignore it.
			Or for others we will generate complete hash value and than compare with it's fellow files.
			If generated hash match we will remove one of the file or else we will just add it's hash value in 
			hash_full dict.
		"""
		if len(files) < 2:
			continue
		for file in files:
			full_hash = generate_hash(file, False)
			similar_file = hash_full.get(full_hash)
			if similar_file:
				removed_files += 1
				os.remove(similar_file)
			else:
				hash_full[full_hash] = file

	print(f"Total files removed : {removed_files}")

if __name__ == '__main__':
	""" If this file is imported in another file than this part of the code will not execute. """
	if sys.argv[1]:
		RemoveSimilarImage(sys.argv[1])
	else:
		print("Path of the image folder is missing.")
