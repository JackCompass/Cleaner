import hashlib

def file_reader(file_obj, size = 1024):
	""" This function will read 1024 byte of data or read complete data of a file depending upon the
		meta condition. """
	while True:
		data = file_obj.read(size)
		if not data:
			return
		yield data

def generate_hash(file, meta, hash = hashlib.sha1):
	"""It will generate the hash value of the file data. After opening in binary mode we will evaluate the
	meta condition if result true we will return hash value of 1024 byte data or else will return the 
	complete hash value of the file data.
	"""
	hash_obj = hash()
	file_obj = open(file, 'rb')
	if meta:
		hash_obj.update(file_obj.read(1024))
	else:
		for data in file_reader(file_obj):
			hash_obj.update(data)
	hashed = hash_obj.digest()
	file_obj.close()
	return hashed
