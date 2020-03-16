from timeit import timeit
from random import randint

class Openhash:

	''' Dictionary using Open Hashtable '''
	
	# creates an empty hash table with b buckets
	def __init__(self, b):
		self.__htable = [[]] * b 
		
	# overwrites the __getitem__ function 
	# member function
	def __getitem__(self, key):
		i = self.hash(str(key))
		for k in self.__htable[i]:
			if k[0] == key:
				return k[1]
		raise IndexError

	def __str__(self):
		return str(self.__htable)

	# basic hash function
	def hash(self, x):
		return (ord(str(x)[0]) % len(self.__htable))
	
	# inserts a key, value pair 
	def insert(self, key, value):
		i = self.hash(key)
		self.__htable[i].append([key, value])

	# deletes a key, value pair with a given key
	def delete(self, key):
		i = self.hash(key)
		for k in self.__htable[i]:
			if k[0] == key:
				self.__htable[i].remove([key, k[1]])
				return 0
		return -1

# populates a hash table with i elements and i // 10 buckets
def populate(i):
	oh = Openhash(i // 10)
	for k in range(i):
		oh.insert(k, randint(0, k))
	return oh

# create an open hash table with i elements and then delete them
def dlt(i):
	oh = populate(i)
	for k in range(i):
		oh.delete(k)

# test insertion on 100-900 elements
def insertTest():
	print("input  |  timing (ms)")
	for i in range(100, 1000, 100):
		print(i, "   | ", 1000*timeit(lambda: populate(i), number=100)/100)

# test deletion on 100-900 elements
def deleteTest():
	print("\ninput  |  timing (ms)")
	for i in range(100, 1000, 100):
		print(i, "   | ", 1000*timeit(lambda: dlt(i), number=100)/100)


if __name__ == '__main__':
	print("Inserting:\n")
	insertTest()
	print("\nDeleting: ")
	deleteTest()
