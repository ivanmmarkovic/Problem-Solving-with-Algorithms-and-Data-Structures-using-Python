
# min heap
class BinaryHeap:
    def __init__(self):
        self.pointer: int = 0
        self.heap: list = [None]

    def is_empty(self) -> bool:
        return self.pointer == 0

    def insert(self, item):
        self.heap.append(item)
        self.pointer += 1
        self.perc_up(self.pointer)

    def perc_up(self, index: int):
        while index // 2 > 0:
            if self.heap[index] < self.heap[index // 2]:
                self.heap[index], self.heap[index // 2] = self.heap[index // 2], self.heap[index]
            index = index // 2

    def get_min(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        return self.heap[1]

    def delete_min(self):
        if self.is_empty():
            raise Exception("Heap is empty")
        ret_value: int = self.heap[1]
        self.heap[1] = self.heap[self.pointer]
        self.heap.pop()
        self.pointer -= 1
        self.perc_down(1)
        return ret_value

    def perc_down(self, index: int):
        while index * 2 <= self.pointer:
            swap_index: int = self.find_swap_index(index)
            if self.heap[swap_index] < self.heap[index]:
                self.heap[swap_index], self.heap[index] = self.heap[index], self.heap[swap_index]
            index = swap_index

    def find_swap_index(self, index: int) -> int:
        if index * 2 + 1 > self.pointer:
            return index * 2
        else:
            if self.heap[index * 2] <= self.heap[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def build_heap(self, nums: list):
        for n in nums:
            self.insert(n)


h: BinaryHeap = BinaryHeap()
h.insert(10)
h.insert(1)
h.insert(3)
print(h.heap)  # [None, 1, 10, 3]
print(h.get_min())  # 1

while not h.is_empty():
    print(h.delete_min())
