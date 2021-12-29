
from typing import Any, List


class HashTable:

    def __init__(self, capacity:int = 11) -> None:
        self.capacity:int = capacity
        self.length: int = 0
        self.keys: List[int] = [None] * self.capacity
        self.values: List[Any] = [None] * self.capacity

    def put(self, key:int, value:Any):
        index:int = self.put_helper(key)
        if index != -1:
            self.values[index] = value
            return
        hash:int = self.hash(key)
        if self.keys[hash] is None or self.keys[hash] == -1:
            self.keys[hash] = key
            self.values[hash] = value
            self.length += 1
        elif self.keys[hash] == key:
            self.values[hash] = value
        else:
            new_hash:int = self.rehash(hash)
            while new_hash != hash and self.keys[new_hash] is not None and self.keys[new_hash] != -1 and self.keys[new_hash] != key:
                new_hash = self.rehash(new_hash)

            if self.keys[new_hash] is None or self.keys[new_hash] == -1:
                self.keys[new_hash] = key
                self.values[new_hash] = value
                self.length += 1
            elif self.keys[new_hash] == key:
                self.values[new_hash] = value

    def put_helper(self, key) -> int:
        hash:int = self.hash(key)
        if self.keys[hash] is None:
            return -1
        elif self.keys[hash] == key:
            return hash
        else:
            new_hash:int = self.rehash(hash)
            while new_hash != hash and self.keys[new_hash] is not None and self.keys[new_hash] != key:
                new_hash = self.rehash(new_hash)

            if self.keys[new_hash] == key:
                return new_hash
            else:
                return -1

    def get(self, key:int) -> Any:
        hash:int = self.hash(key)
        if self.keys[hash] is None:
            return None
        elif self.keys[hash] == key:
            return self.values[hash]
        else:
            new_hash:int = self.rehash(hash)
            while new_hash != hash and self.keys[new_hash] is not None and self.keys[new_hash] != key:
                new_hash = self.rehash(new_hash)

            if self.keys[new_hash] == key:
                return self.values[new_hash]
            else:
                return None

    def contains(self, key:int) -> bool:
        hash:int = self.hash(key)
        if self.keys[hash] is None:
            return False
        elif self.keys[hash] == key:
            return True
        else:
            new_hash:int = self.rehash(hash)
            while new_hash != hash and self.keys[new_hash] is not None and self.keys[new_hash] != key:
                new_hash = self.rehash(new_hash)

            if self.keys[new_hash] == key:
                return True
            else:
                return False

    def delete(self, key:int):
        hash:int = self.hash(key)
        if self.keys[hash] is None:
            return
        elif self.keys[hash] == key:
            self.keys[hash] = -1
            self.values[hash] = None
            self.length -= 1
        else:
            new_hash:int = self.rehash(hash)
            while new_hash != hash and self.keys[new_hash] is not None and self.keys[new_hash] != key:
                new_hash = self.rehash(new_hash)

            if self.keys[new_hash] == key:
                self.keys[new_hash] = -1
                self.values[new_hash] = None
                self.length -= 1
            else:
                return None

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
