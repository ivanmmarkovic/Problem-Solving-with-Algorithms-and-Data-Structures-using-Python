
class HashMap:
    def __init__(self, length: int = 11):
        self._length: int = length
        self._keys: list = [None] * self._length
        self._values: list = [None] * self._length
        self._elements_count: int = 0

    def put(self, key: int, value: str):
        hash: int = self.hash(key)
        if self._keys[hash] is None or self._keys[hash] == "deleted" or self._keys[hash] == key:
            if self._keys[hash] is None or self._keys[hash] == "deleted":
                self._elements_count += 1
            self._keys[hash] = key
            self._values[hash] = value
        else:
            new_hash: int = self.rehash(hash)
            while new_hash != hash and self._keys[new_hash] is not None and self._keys[new_hash] != "deleted"\
                    and self._keys[new_hash] != key:
                new_hash = self.rehash(new_hash)
            if self._keys[new_hash] is None or self._keys[new_hash] == "deleted" or self._keys[new_hash] == key:
                if self._keys[new_hash] is None or self._keys[new_hash] == "deleted":
                    self._elements_count += 1
                self._keys[new_hash] = key
                self._values[new_hash] = value

    def get(self, key: int):
        hash: int = self.hash(key)
        if self._keys[hash] is None:
            return None
        elif self._keys[hash] == key:
            return self._values[hash]
        else:
            new_hash: int = self.rehash(hash)
            while new_hash != hash and self._keys[new_hash] is not None and self._keys[new_hash] != key:
                new_hash = self.rehash(new_hash)
            if self._keys[new_hash] is None:
                return None
            elif self._keys[new_hash] == key:
                return self._values[new_hash]
            else:
                return None

    def contains(self, key: int) -> bool:
        hash: int = self.hash(key)
        if self._keys[hash] is None:
            return False
        elif self._keys[hash] == key:
            return True
        else:
            new_hash: int = self.rehash(hash)
            while new_hash != hash and self._keys[new_hash] is not None and self._keys[new_hash] != key:
                new_hash = self.rehash(new_hash)
            if self._keys[new_hash] is None:
                return False
            elif self._keys[new_hash] == key:
                return True
            else:
                return False

    def delete(self, key):
        hash: int = self.hash(key)
        if self._keys[hash] is None:
            return
        elif self._keys[hash] == key:
            self._elements_count -= 1
            self._keys[hash] = "deleted"
            self._values[hash] = None
        else:
            new_hash: int = self.rehash(hash)
            while new_hash != hash and self._keys[new_hash] is not None and self._keys[new_hash] != key:
                new_hash = self.rehash(new_hash)
            if self._keys[new_hash] == key:
                self._elements_count -= 1
                self._keys[new_hash] = "deleted"
                self._values[new_hash] = None

    def size(self) -> int:
        return self._elements_count

    def hash(self, key: int) -> int:
        return key % self._length

    def rehash(self, old_hash: int):
        return (old_hash + 1) % self._length


hm: HashMap = HashMap()
hm.put(11, "string 11")
hm.put(22, "string 22")
hm.put(33, "string 33")
hm.put(44, "string 44")
hm.put(12, "string 12")
hm.put(21, "string 21")

print(hm._keys)
print(hm._values)

print("Get 11", hm.get(11))
print("Get 33", hm.get(33))
print("Get 21", hm.get(21))
print("Get 7", hm.get(7))

print("Contains key 7", hm.contains(7))
print("Contains key 33", hm.contains(33))


print("Delete key 7", hm.delete(7))
print("Delete key 33", hm.delete(33))

print("Contains key 33", hm.contains(33))

print(hm._keys)
print(hm._values)

hm.put(14, "string 14")

print("Contains key 33", hm.contains(33))

print(hm._keys)
print(hm._values)
