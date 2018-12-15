from Queue import Queue

def hotPotato(alist, number):
	d = Queue()
	for member in alist:
		d.enqueue(member)

	while d.size() > 1:
		for i in range(number):
			d.enqueue(d.dequeue())

		d.dequeue()

	return d.dequeue()


print(hotPotato(['a', 'b', 'c'], 5))

