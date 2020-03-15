from timeit import timeit
from random import randint

class Closedhash:

	''' Dictionary using Open Hashtable '''
	
	# creates an empty hash table with b buckets
	def __init__(self, b):
        self.__insertCount = 0
        self.__deleteCount = 0
		self.__htable = [[None,None]] * b 
		
	# overwrites the __getitem__ function 
    # member function
	def __getitem__(self, key):
		i = self.hash(str(key))
		while self.__htable[i][0] is not None:
			if self.__htable[i][0] == key:
				return self.__htable[i][1]
			else:
				i += 1
		raise IndexError

	def __str__(self):
		return str(self.__htable)

	# basic hash function
	def hash(self, x):
		return (ord(str(x)[0]) % len(self.__htable))
	
	# inserts a key, value pair 
	def insert(self, key, value):
		i = self.hash(key)
		count = 0
		while self.__htable[i][0] is not None:
			if count >= len(self.__htable):
				raise IndexError
			if i < (len(self.__htable) - 1): 
				i += 1
			else:
				i = 0
			count += 1
		self.__htable[i] = [key, value]

	# deletes a key, value pair with a given key
	def delete(self, key):
		i = self.hash(key)
		while self.__htable[i][0] is not None:
			if self.__htable[i][0] == key:
				self.__htable[i] = [None,None]
				return
			else:
				i += 1
		return 0


def insrt(i):
	ch = Closedhash(i)
	for k in range(i):
		ch.insert(k, randint(0, k))
	return ch

def dlt(i):
	ch = insrt(i)
	for k in range(i):
		ch.delete(k)

def insertTest():
	print("input  |  timing (ms)")
	for i in range(100, 1000, 100):
		print(i, "   | ", insrt(i))
	
def deleteTest():
	print("\ninput  |  timing (ms)")
	for i in range(100, 1000, 100):
		print(i, "   | ", dlt(i))

if __name__ == '__main__':
	print("Inserting: ")
	insertTest()
	print("\nDeleting: ")
	deleteTest()