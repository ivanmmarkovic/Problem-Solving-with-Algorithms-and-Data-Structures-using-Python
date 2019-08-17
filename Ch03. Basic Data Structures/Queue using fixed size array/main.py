
from queue import Queue

queue = Queue(5)

queue.enqueue(1221)
queue.enqueue(1)

for i  in range(10):
    queue.enqueue(i)

print(queue.dequeue())

while not queue.isEmpty():
    print(queue.dequeue())


