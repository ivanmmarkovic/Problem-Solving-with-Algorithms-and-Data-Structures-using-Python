
from queue import Queue

queue = Queue(5)

for i in range(10):
    queue.enqueue(i)

print(queue.showFirst())

print(queue.dequeue())
print(queue.dequeue())

queue.enqueue(1000)

queue.printAll()



