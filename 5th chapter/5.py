"""	Implement the del method for the HashTable class	"""


class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size

	def put(self, key, data):
		hash_value = self.hash_function(key,len(self.slots))
		if self.slots[hash_value] == None:
			self.slots[hash_value] = key
			self.data[hash_value] = data
		else:
			if self.slots[hash_value] == key:
				self.data[hash_value] = data #replace
			else:
				next_slot = self.rehash(hash_value, len(self.slots))
				while self.slots[next_slot] != None and self.slots[next_slot] != key:
					next_slot = self.rehash(next_slot, len(self.slots))

				if self.slots[next_slot] == None:
					self.slots[next_slot] = key
					self.data[next_slot] = data
				else:
					self.data[next_slot] = data #replace

	def hash_function(self, key, size):
		return key % size

	def rehash(self, old_hash, size):
		return (old_hash + 1) % size

	def get(self, key):
		start_slot = self.hash_function(key, len(self.slots))
		data = None
		stop = False
		found = False
		position = start_slot
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position=self.rehash(position, len(self.slots))
				if position == start_slot:
					stop = True
		return data

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		self.put(key, data)

	def __len__(self):
		l = 0
		for i in self.slots:
			if i:
				l += 1
		return l

	def __contains__(self,data):
		return data in self.data

	def __delitem__(self,key):
		data = self.get(key)
		self.data[self.data.index(data)] = None
		self.slots[self.slots.index(key)] = None


if __name__ == '__main__':
	h=HashTable()
	h[54]="cat"
	h[26]="dog"
	h[93]="lion"
	h[17]="tiger"
	h[77]="bird"
	h[31]="cow"
	h[44]="goat"
	h[55]="pig"
	h[20]="chicken"

	print h.slots
	print h.data
	del h[93]
	print h.slots
	print h.data
