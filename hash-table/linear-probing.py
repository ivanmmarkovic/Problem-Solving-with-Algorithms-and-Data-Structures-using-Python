

from typing import Any, List, Tuple


class HashTable:

    def __init__(self, capacity:int = 11) -> None:
        self.capacity:int  = capacity
        self.keys: List[int] = [None] * self.capacity
        self.values: List[int] = [None] * self.capacity
        self.length: int = 0


    def put(self, key:int, value:Any):
        index, contains = self.find(key)
        if contains:
            self.values[index] = value
            return
        hash:int = self.hash(key)
        if self.keys[hash] == float('inf') or self.keys[hash] is None:
            self.keys[hash] = key 
            self.values[hash] = value
            self.length += 1
        else:
            new_hash:int = self.rehash(hash) % self.capacity
            while self.keys[new_hash] is not None and self.keys[new_hash] != float('inf') and new_hash != hash:
                new_hash = self.rehash(new_hash)
            if self.keys[new_hash] == float('inf') or self.keys[new_hash] is None:
                self.keys[new_hash] = key 
                self.values[new_hash] = value
                self.length += 1

        
    def contains(self, key:int) -> bool:
        _, contains = self.find(key)
        return contains


    def get(self, key:int) -> Any:
        index, contains = self.find(key)
        if contains:
            return self.values[index] 
        return None


    def delete(self, key:int):
        index, contains = self.find(key)
        if not contains:
            return
        self.keys[index] = float('inf')
        self.values[index] = None
        self.length -= 1


    def find(self, key:int) -> Tuple[int, bool]:
        hash:int = self.hash(key)
        if self.keys[hash] == key:
            return (hash, True)
        elif self.keys[hash] is None:
            return (None, False)
        else:
            new_hash:int = self.rehash(hash) % self.capacity
            while self.keys[new_hash] != key and self.keys[new_hash] is not None and new_hash != hash:
                new_hash = self.rehash(new_hash)

            if self.keys[new_hash] == key:
                return (new_hash, True)
            return (None, False)


    def size(self) -> int:
        return self.length

    def hash(self, key:int) -> int:
        return key % self.capacity


    def rehash(self, old_hash:int) -> int:
        return (old_hash + 1) % self.capacity


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
print('Get 22', ht.get(22))
print('Get 147', ht.get(147))
print('----------------------------------------')

print('Contains 22', ht.contains(22))
ht.delete(22)
print(ht.size())
print(ht.keys)
print(ht.values)
print('Contains 22', ht.contains(22))
print('----------------------------------------')

print('Contains 44', ht.contains(44))
print(ht.keys)
print(ht.values)
print('Contains 77', ht.contains(77))
ht.put(44, 'string 144')
ht.put(77, 'string 77')

print(ht.size())
print(ht.keys)
print(ht.values)
print('Contains 77', ht.contains(77))
print('Contains 44', ht.contains(44))

