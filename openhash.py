from timeit import timeit
from random import randint

class Openhash:

	''' Dictionary using Open Hashtable '''
	
	# creates an empty hash table with b buckets
	def __init__(self, b):
<<<<<<< HEAD
		self.__htable = [[]] * b
=======
		self.__htable = [[]] * b 
>>>>>>> 541721bb129fe8f65413d2447cddaa33b40542d3
		
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
	print("input  |  timing (0.1s)  |  timing per elem. (0.1s)")
	print("-"*51)
	for i in range(100, 1000, 100):
		timing = 1000*timeit(lambda: populate(i), number=100)/100
		print("{0:d}{1:>5s}{2:^17.5f}{1}{3:^26f}".format(i, "|", timing, timing/i))

# test deletion on 100-900 elements
def deleteTest():
	print("input  |  timing (0.1s)  |  timing per elem. (0.1s)")
	print("-"*51)
	for i in range(100, 1000, 100):
		timing = 1000*timeit(lambda: dlt(i), number=100)/100
		print("{0:d}{1:>5s}{2:^17.5f}{1}{3:^26f}".format(i, "|", timing, timing/i))


if __name__ == '__main__':
	print("Inserting:\n")
	insertTest()
	print("\nDeleting:\n")
	deleteTest()
