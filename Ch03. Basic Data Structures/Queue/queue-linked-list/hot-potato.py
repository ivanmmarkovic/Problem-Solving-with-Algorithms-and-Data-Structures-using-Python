from queue import Queue


def hotPotato(people: list, number: int):
    queue: Queue = Queue()

    for person in people:
        queue.enqueue(person)

    while queue.size() > 1:
        for i in range(number):
            queue.enqueue(queue.dequeue())
        
        queue.dequeue()

    return queue.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 7))
