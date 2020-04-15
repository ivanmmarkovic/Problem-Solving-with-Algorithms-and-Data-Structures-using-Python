
class HashMap:
    def __init__(self, size: int = 11):
        self.size = size
        self.keys: list = [None] * self.size
        self.values: list = [None] * self.size
        self.length: int = 0

    def put(self, key, value):
        hash: int = self.hash(key)
        if self.keys[hash] == key or self.keys[hash] is None or self.keys[hash] == "deleted":
            self.keys[hash] = key
            self.values[hash] = value
            self.length += 1
        else:
            newHash: int = self.rehash(hash)
            while newHash != hash and self.keys[newHash] != key and self.keys[newHash] is not None and self.keys[newHash] != "deleted":
                newHash = self.rehash(newHash)
            if self.keys[newHash] != key or self.keys[newHash] is not None or self.keys[newHash] != "deleted":
                if self.keys[newHash] != key:
                    self.length += 1
                self.keys[newHash] = key
                self.values[newHash] = value

    def get(self, key):
        hash: int = self.hash(key)
        if self.keys[hash] == key:
            return self.values[hash]
        elif self.keys[hash] is None:
            return None
        else:
            newHash: int = self.rehash(hash)
            while newHash != hash and self.keys[newHash] is not None and self.keys[newHash] != key:
                newHash = self.rehash(newHash)
            if self.keys[newHash] == key:
                return self.values[newHash]
            else:
                return None

    def delete(self, key):
        hash: int = self.hash(key)
        if self.keys[hash] == key:
            self.keys[hash] = "deleted"
            self.values[hash] = None
            self.length -= 1
        elif self.keys[hash] is None:
            return
        else:
            newHash: int = self.rehash(hash)
            while newHash != hash and self.keys[newHash] is not None and self.keys[newHash] != key:
                newHash = self.rehash(newHash)
            if self.keys[newHash] == key:
                self.keys[newHash] = "deleted"
                self.values[newHash] = None
                self.length -= 1

    def contains(self, key)->bool:
        hash: int = self.hash(key)
        if self.keys[hash] == key:
            return True
        elif self.keys[hash] is None:
            return False
        else:
            newHash: int = self.rehash(hash)
            while newHash != hash and self.keys[newHash] is not None and self.keys[newHash] != key:
                newHash = self.rehash(newHash)
            if self.keys[newHash] == key:
                return True
            else:
                return False

    def hash(self, key):
        return key % self.size

    def rehash(self, oldHash):
        return (oldHash + 1) % self.size

    
ht: HashMap = HashMap()

ht.put(11, "string 11")
ht.put(22, "string 22")
ht.put(33, "string 33")
ht.put(44, "string 44")
ht.put(12, "string 12")

ht.put(21, "string 21")

print(ht.keys)
print(ht.values)

print(ht.contains(11), ht.contains(33), ht.contains(21), ht.contains(117))
print(ht.delete(11))
print(ht.contains(22))
print(ht.get(22))

