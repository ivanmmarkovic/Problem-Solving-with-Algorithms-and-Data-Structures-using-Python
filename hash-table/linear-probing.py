

from typing import Any, List


class HashTable:


    def __init__(self, capacity:int = 11) -> None:
        self.capacity: int = capacity
        self.length: int = 0
        self.keys: List[int] = [None] * self.capacity
        self.values: List[Any] = [None] * self.capacity

    
    def put(self, key: int, value: Any) -> int:
        index: int = self.hash(key)
        if self.keys[index] is None or self.keys[index] == -1:
            self.keys[index] = key
            self.values[index] = value
            self.length += 1
        elif self.keys[index] == key:
            self.values[index] = value
        else:
            new_index: int = self.rehash(index)
            while new_index != index and self.keys[new_index] is not None and self.keys[new_index] != -1 and self.keys[new_index] != key:
                new_index = self.rehash(new_index)

            if self.keys[new_index] is None or self.keys[new_index] == -1:
                self.keys[new_index] = key
                self.values[new_index] = value
                self.length += 1
            elif self.keys[new_index] == key:
                self.values[new_index] = value 


    def get(self, key: int) -> Any:
        index: int = self.hash(key)
        if self.keys[index] == key:
            return self.values[index]
        elif self.keys[index] is None:
            return None
        else:
            new_index: int = self.rehash(index)
            while new_index != index and self.keys[new_index] is not None and self.keys[new_index] != key:
                new_index = self.rehash(new_index)

            if self.keys[new_index] == key:
                return self.values[new_index] 
            elif self.keys[new_index] is None:
                return None


    def contains(self, key: int) -> bool:
        index: int = self.hash(key)
        if self.keys[index] == key:
            return True
        elif self.keys[index] is None:
            return False
        else:
            new_index: int = self.rehash(index)
            while new_index != index and self.keys[new_index] is not None and self.keys[new_index] != key:
                new_index = self.rehash(new_index)

            if self.keys[new_index] == key:
                return True
            elif self.keys[new_index] is None:
                return False


    def delete(self, key: int) -> None:
        index: int = self.hash(key)
        if self.keys[index] == key:
            self.values[index] = -1
            self.values[index] = None
            self.length -= 1
            return None
        elif self.keys[index] is None:
            return None
        else:
            new_index: int = self.rehash(index)
            while new_index != index and self.keys[new_index] is not None and self.keys[new_index] != key:
                new_index = self.rehash(new_index)

            if self.keys[new_index] == key:
                self.values[new_index] = -1
                self.values[new_index] = None
                self.length -= 1
                return None
            else:
                return None


    def hash(self, key: int) -> int:
        return key % self.capacity

    
    def rehash(self, index: int) -> int:
        return (index + 1) % self.capacity


    def size(self) -> int:
        return self.length



ht: HashTable = HashTable()
ht.put(11, 'string 11')
ht.put(22, 'string 22')
ht.put(33, 'string 33')
ht.put(44, 'string 44')

ht.put(21, 'string 21')
ht.put(12, 'string 12')

print(ht.keys)
print(ht.values)
print(ht.size())
print('Get 11', ht.get(11))
print('Get 33', ht.get(33))
print('Get 147', ht.get(147))
print('----------------------------------------')

print('Contains 22', ht.contains(22))
ht.delete(22)
print(ht.size())
print(ht.keys)
print(ht.values)
print('Contains 22', ht.contains(22))
print('----------------------------------------')

print('Contains 77', ht.contains(77))
ht.put(44, 'string 144')
ht.put(77, 'string 77')

print(ht.size())
print(ht.keys)
print(ht.values)
print('Contains 77', ht.contains(77))
