from LinkedListSingle import LinkedListSingle

l = LinkedListSingle()

alist = [4, 4, 1, 1, 3, 5, 5, 4, 5, 6, 7, 8, 8, 4]

for item in alist:
    l.addToTail(item)


l.printAll()
l.insertAfter(4, 4)
l.insertBefore(5, 5)
l.printAll()

