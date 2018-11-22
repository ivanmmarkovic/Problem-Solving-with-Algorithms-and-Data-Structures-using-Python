from Queue import Queue

def hotPotato(people, number):
    q = Queue()
    for person in people:
        q.enqueue(person)

    while q.size() > 1:
        for i in range(number):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
