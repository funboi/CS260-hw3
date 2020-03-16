from timeit import timeit
from random import randint, seed

class Closedhash:
	# Dictionary using Open Hashtable
	# creates an empty hash table with b buckets
	def __init__(self, b):
		self.__htable = [[None,None]] * b
		self.__insrtCnt = 0
		self.__dltCnt = 0	

	# overwrites the __getitem__ function 
    # member function
	def __getitem__(self, key):
		i = self.hash(str(key))
		while self.__htable[i][0] is not None:
			if self.__htable[i][0] == key:
				return self.__htable[i][1]
			else:
				i += 1
		raise IndexError # raise error if element not found

	# overwrites the string function
	def __str__(self):
		return str(self.__htable)

	# return insertion count (# of probes)
	def insertCnt(self):
		return self.__insrtCnt
	
	# return deletion count (# of probes)
	def deleteCnt(self):
		return self.__dltCnt

	# basic hash function
	def hash(self, x):
		return (ord(str(x)[0]) % len(self.__htable))
	
	# inserts a key, value pair 
	def insert(self, key, value):
		i = self.hash(key)
		self.__insrtCnt = 0
		while self.__htable[i][0] is not None:
			if self.__insrtCnt > len(self.__htable) + 1:
				raise IndexError
			if i < (len(self.__htable) - 1): 
				i += 1
			else:
				i = 0
			self.__insrtCnt += 1
		self.__htable[i] = [key, value]

	# deletes a key, value pair with a given key
	# returns -1 if not found
	def delete(self, key):
		i = self.hash(key)
		self.__dltCnt = 0
		while self.__htable[i][0] is not None:
			if self.__htable[i][0] == key:
				self.__htable[i] = [None,None]
				return 0
			else:
				i += 1
				if i == len(self.__htable):
					i = 0
				if i == self.hash(key):
					break
				self.__dltCnt += 1
		return -1

# creates a closed hash table and populates it with i items
def populate(i):
	ch = Closedhash(i)
	for k in range(i):
		ch.insert(k, randint(0, k))
	return ch

# counts # of probes in i insertions
def insrtCounter(i):
	probes = 0
	ch = Closedhash(i)
	for k in range(100):
		ch.insert(randint(0, k), randint(0, k))
		probes += ch.insertCnt()
	return probes

# counts # of probes in i deletions
def dltCounter(i):
	probes = 0
	ch = populate(i)
	for k in range(100):
		x = randint(0, i-1)
		ch.delete(x)
		probes += ch.deleteCnt()
	return probes

# tests # of probes in insertion on 100-900 elements
def insertTest():
	print("input  |  number of probes")
	print("-"*25)
	for i in range(100, 1000, 100):
		print(i, "   | ", insrtCounter(i))
	
# tests # of probes in deletion on 100-900 elements
def deleteTest():
	print("\ninput  |  number of probes")
	print("-"*25)
	for i in range(100, 1000, 100):
		print(i, "   | ", dltCounter(i))

if __name__ == '__main__':
	print("\nInserting:\n")
	insertTest()
	print("\nDeleting:")
	deleteTest()