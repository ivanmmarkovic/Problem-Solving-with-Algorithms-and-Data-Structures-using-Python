
class HashTable:
    def __init__(self, size: int = 11):
        self.size = size
        self.keys: list = [None] * self.size
        self.values: list = [None] * self.size

    def put(self, key: int, value: str):
        hash = self.hash(key)
        if self.keys[hash] is None:
            self.keys[hash] = key
            self.values[hash] = value
        elif self.keys[hash] == "deleted":
            self.keys[hash] = key
            self.values[hash] = value
        elif self.keys[hash] == key:
            self.values[hash] = value
        else:
            newHash = self.rehash(hash)
            while newHash != hash and self.keys[newHash] is not None and self.keys[newHash] != "deleted" and self.keys[newHash] != key:
                newHash = self.rehash(newHash)
            if self.keys[newHash] is None:
                self.keys[newHash] = key
                self.values[newHash] = value
            elif self.keys[newHash] == "deleted":
                self.keys[newHash] = key
                self.values[newHash] = value
            elif self.keys[newHash] == key:
                self.values[newHash] = value

    def delete(self, key: int):
        hash = self.hash(key)
        if self.keys[hash] is None:
            return
        elif self.keys[hash] == key:
            self.keys[hash] = "deleted"
            return
        else:
            newHash = self.rehash(hash)
            while newHash != hash and self.keys[newHash] is not None and self.keys[newHash] != key:
                newHash = self.rehash(newHash)
            if self.keys[newHash] is None:
                return
            elif self.keys[newHash] == key:
                self.keys[newHash] = "deleted"
                return
            
    def contains(self, key: int)-> bool:
        hash = self.hash(key)
        if self.keys[hash] is None:
            return False
        elif self.keys[hash] == key:
            return True
        else:
            newHash = self.rehash(hash)
            while newHash != hash and self.keys[newHash] is not None and self.keys[newHash] != key:
                newHash = self.rehash(newHash)
            if self.keys[newHash] is None:
                return False
            elif self.keys[newHash] == key:
                return True
            else:
                return False

    def elementsCount(self)->int:
        count: int = 0
        for key in self.keys:
            if key is not None and key != "deleted":
                count += 1
        return count

    def hash(self, key: int):
        return key % self.size

    def rehash(self, oldHash: int):
        return (oldHash + 1) % self.size

    def show(self):
        print(self.keys)
        print(self.values)

ht = HashTable()
ht.put(11, "string 11")
ht.put(22, "string 22")
ht.put(33, "string 33")
ht.put(44, "string 44")
ht.put(12, "string 12")
ht.put(21, "string 21")

print("Size ", ht.elementsCount())
ht.show()
print(ht.contains(11), ht.contains(44), ht.contains(21), ht.contains(117))

print("Deleting elements")
ht.delete(11)
ht.delete(44)
ht.show()
print("Contains 33", ht.contains(33))
print("Contains 44", ht.contains(44))


ht.put(55, "string 55")
ht.show()
print("Contains 55", ht.contains(55))

