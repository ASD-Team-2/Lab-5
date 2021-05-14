INITIAL_CAPACITY = 50

class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	def __str__(self):
		return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)
	def __repr__(self):
		return str(self)

class HashTable:

	# Initialize hash table
	def __init__(self):
		self.capacity = INITIAL_CAPACITY
		self.size = 0
		self.buckets = [None]*self.capacity

	def hash(self, key):
		hashsum = 0
		for idx, c in enumerate(key):
			hashsum += (idx + len(key)) ** ord(c)
			hashsum = hashsum % self.capacity
		return hashsum

	def insert(self, key, value):
		self.size += 1
		index = self.hash(key)
		node = self.buckets[index]

		if node is None:
			self.buckets[index] = Node(key, value)
			return

		prev = node
		while node is not None:
			prev = node
			node = node.next

		prev.next = Node(key, value)

	def hash_function(self, key):
		i = key % self.capacity
		return i

	
	def find(self, key):
		index = self.hash(key)
		node = self.buckets[index]

		while node is not None and node.key != key:
			node = node.next

		if node is None:
			return None
		else:
			return node.value

	def remove(self, key):
		index = self.hash(key)
		node = self.buckets[index]
		prev = None

		while node is not None and node.key != key:
			prev = node
			node = node.next

		if node is None:
			return None
		else:
			self.size -= 1
			result = node.value
			if prev is None:
				self.buckets[index] = node.next 
			else:
				prev.next = prev.next.next 
			return result


def creating_ht(n):
	ht = HashTable()
	for i in range(n):
		obj="key"+str(i)
		ht.insert(obj, "value")
	return ht

def benchmark():
	import time
	from timeit import default_timer as timer

	for i in range(3):
		n=(10**(i+3))
	
		ht = creating_ht(n)
		start = timer()
		#ht=(creating_ht(n))
		ht.insert("key2", "value1")
		end = timer()
		print("Insertion time: {} sec".format(end-start) + " of {} nums.".format(n))

		start = timer()
		#ht=(creating_ht(n))
		ht.remove("key4")   
		end = timer()
		print("Removing time: {} sec".format(end-start) + " of {} nums.".format(n))

		start = timer()
		ht=(creating_ht(n))
		ht.find("key3")
		end = timer()
		print("Searcing time: {} sec".format(end-start) + " of {} nums.".format(n))

if __name__=="__main__":
	benchmark()