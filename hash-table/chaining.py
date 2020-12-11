
class KeyValue:
    def __init__(self, key: int = None, value: str = None):
        self.key: int = key
        self.value: str = value

class HashMap:
    def __init__(self, length: int = 11):
        self._length: int = length
        self._items: list = [None] * self._length
        self._elements_count: int = 0

    def put(self, key: int, value: str):
        hash: int = self.hash(key)
        if self._items[hash] is None:
            self._items[hash] = [KeyValue(key, value)]
            self._elements_count += 1
        else:
            i: int = 0
            found: bool = False
            while i < len(self._items[hash]) and not found:
                if self._items[hash][i].key == key:
                    found = True
                else:
                    i += 1
            if found:
                self._items[hash][i].value = value
            else:
                self._items[hash].append(KeyValue(key, value))
                self._elements_count += 1

    def get(self, key: int) -> str:
        hash: int = self.hash(key)
        if self._items[hash] is None:
            return None
        else:
            i: int = 0
            found: bool = False
            while i < len(self._items[hash]) and not found:
                if self._items[hash][i].key == key:
                    found = True
                else:
                    i += 1
            if found:
                return self._items[hash][i].value
            else:
                return None

    def contains(self, key: int) -> bool:
        hash: int = self.hash(key)
        if self._items[hash] is None:
            return False
        else:
            i: int = 0
            found: bool = False
            while i < len(self._items[hash]) and not found:
                if self._items[hash][i].key == key:
                    found = True
                else:
                    i += 1
            return found

    def delete(self, key):
        hash: int = self.hash(key)
        if self._items[hash] is None:
            return
        else:
            i: int = 0
            found: bool = False
            while i < len(self._items[hash]) and not found:
                if self._items[hash][i].key == key:
                    found = True
                else:
                    i += 1
            if found:
                self._items[hash].pop(i)
                self._elements_count -= 1

    def size(self) -> int:
        return self._elements_count

    def hash(self, key: int) -> int:
        return key % self._length


hm: HashMap = HashMap()
hm.put(11, "string 11")
hm.put(22, "string 22")
hm.put(33, "string 33")
hm.put(44, "string 44")
hm.put(12, "string 12")
hm.put(21, "string 21")


print("Get 11", hm.get(11))
print("Get 33", hm.get(33))
print("Get 21", hm.get(21))
print("Get 7", hm.get(7))

print("Contains key 7", hm.contains(7))
print("Contains key 33", hm.contains(33))


print("Delete key 7", hm.delete(7))
print("Delete key 33", hm.delete(33))

print("Contains key 33", hm.contains(33))


hm.put(14, "string 14")

print("Contains key 33", hm.contains(33))
