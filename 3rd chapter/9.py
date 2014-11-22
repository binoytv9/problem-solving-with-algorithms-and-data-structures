"""	Modify the Hot Potato simulation to allow for a randomly chosen counting value so that
each pass is not predictable from the previous one	"""


from queue import *
import random

def hotPotato(nameList):
	sim_queue = Queue()
	for name in nameList:
		sim_queue.enqueue(name)

	while sim_queue.size() > 1:
		num = random.randint(1,10)
		for i in range(num):
			sim_queue.enqueue(sim_queue.dequeue())
		sim_queue.dequeue()
	return sim_queue.dequeue()

if __name__ == '__main__':
	print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent","Brad"]))
