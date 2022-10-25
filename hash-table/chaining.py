

from typing import Any, List

class KeyValue:

    def __init__(self, key: int, value: Any) -> None:
        self.key: int = key
        self.value: Any = value


class HashTable:


    def __init__(self, capacity:int = 11) -> None:
        self.capacity: int = capacity
        self.length: int = 0
        self.table: List[List[KeyValue]] = [None] * self.capacity

    
    def put(self, key: int, value: Any) -> int:
        index: int = self.hash(key)
        if self.table[index] is None:
            self.table[index] = [KeyValue(key, value)]
            self.length += 1
        else:
            found: bool = False
            i: int = 0
            items: List[KeyValue] = self.table[index]
            while i < len(items) and not found:
                if items[i].key == key:
                    found = True
                else:
                    i += 1
            if found:
                items[i].value = value
            else:
                items.append(KeyValue(key, value))
                self.length += 1


    def get(self, key: int) -> Any:
        index: int = self.hash(key)
        if self.table[index] is None:
            return None
        else:
            found: bool = False
            i: int = 0
            items: List[KeyValue] = self.table[index]
            while i < len(items) and not found:
                if items[i].key == key:
                    found = True
                else:
                    i += 1
            if found:
                return items[i].value
            else:
                return None


    def contains(self, key: int) -> bool:
        index: int = self.hash(key)
        if self.table[index] is None:
            return False
        else:
            found: bool = False
            i: int = 0
            items: List[KeyValue] = self.table[index]
            while i < len(items) and not found:
                if items[i].key == key:
                    found = True
                else:
                    i += 1
            if found:
                return True
            else:
                return False


    def delete(self, key: int) -> None:
        index: int = self.hash(key)
        if self.table[index] is None:
            return None
        else:
            found: bool = False
            i: int = 0
            items: List[KeyValue] = self.table[index]
            while i < len(items) and not found:
                if items[i].key == key:
                    found = True
                else:
                    i += 1
            if not found:
                return None
            
            items.pop(i)
            if len(items) == 0:
                self.table[index] = None
            return None


    def hash(self, key: int) -> int:
        return key % self.capacity


    def size(self) -> int:
        return self.length



ht: HashTable = HashTable()
ht.put(11, 'string 11')
ht.put(22, 'string 22')
ht.put(33, 'string 33')
ht.put(44, 'string 44')

ht.put(21, 'string 21')
ht.put(12, 'string 12')

print(ht.size())
print('Get 11', ht.get(11))
print('Get 33', ht.get(33))
print('Get 147', ht.get(147))
print('----------------------------------------')

print('Contains 22', ht.contains(22))
ht.delete(22)
print(ht.size())
print('Contains 22', ht.contains(22))
print('----------------------------------------')

print('Contains 77', ht.contains(77))
ht.put(44, 'string 144')
ht.put(77, 'string 77')

print(ht.size())
print('Contains 77', ht.contains(77))
