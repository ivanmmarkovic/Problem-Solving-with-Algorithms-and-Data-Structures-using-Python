
class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.heapListSize = 0

    def insert(self, item):
        self.heapList.append(item)
        self.heapListSize += 1
        self.percUp(self.heapListSize)

    def percUp(self, size):
        while size // 2 > 0:
            if self.heapList[size // 2] > self.heapList[size]:
                tmp = self.heapList[size // 2]
                self.heapList[size // 2] = self.heapList[size]
                self.heapList[size] = tmp
            size = size // 2

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.heapListSize]
        self.heapListSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def percDown(self, index):
        while index * 2 <= self.heapListSize:
            minChildIndex = self.minChildIndex(index)
            if self.heapList[index] > self.heapList[minChildIndex]:
                tmp = self.heapList[index]
                self.heapList[index] = self.heapList[minChildIndex]
                self.heapList[minChildIndex] = tmp
            index = minChildIndex
        
    def minChildIndex(self, index):
        if index * 2 + 1 > self.heapListSize:
            return index * 2
        else:
            if self.heapList[index * 2] < self.heapList[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def buildHeap(self, alist):
        for item in alist:
            self.insert(item)

    def findMin(self):
        if not self.isEmpty():
            return self.heapList[1]
        else:
            return None

    def size(self):
        return self.heapListSize

    def isEmpty(self):
        return self.heapListSize == 0

    def show(self):
        print(self.heapList)

bh = BinaryHeap()
bh.insert(10)
bh.insert(7)
bh.insert(15)
bh.insert(16)
bh.insert(3)

bh.show()
bh.delMin()
bh.show()

bh1 = BinaryHeap()
bh1.buildHeap([13, 5, 8, 1, 118, 91])
bh1.show()