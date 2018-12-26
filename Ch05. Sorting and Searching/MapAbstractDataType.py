
class HashTable:

    def __init__(self, size):
        self.keys = [None] * size
        self.values = [None] * size

    def put(self, key, value):
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == None:
            self.keys[hash] = key
            self.values[hash] = value
        elif self.keys[hash] == key:
            self.values[hash] = value
        else:
            newHash = self.rehash(hash, len(self.keys))
            while newHash != hash and self.keys[newHash] != None and self.keys[newHash] != key:
                newHash = self.rehash(newHash, len(self.keys))
            if self.keys[newHash] == None:
                self.keys[newHash] = key
                self.values[newHash] = value
            elif self.keys[newHash] == key :
                self.values[newHash] = value

    def get(self, key):
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == None:
            return None
        elif self.keys[hash] == key:
            return self.values[hash]
        else:
            newHash = self.rehash(hash, len(self.keys))
            while newHash != hash and self.keys[newHash] != None and self.keys[newHash] != key:
                newHash = self.rehash(newHash, len(self.keys))
            if self.keys[newHash] == None:
                return None
            elif self.keys[newHash] == key:
                return self.values[newHash]
            else:
                return None

    def delete(self, key):
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == None:
            return None
        elif self.keys[hash] == key:
            toReturn = self.values[hash]
            self.keys[hash] = None
            self.values[hash] = None
            return toReturn
        else:
            newHash = self.rehash(hash, len(self.keys))
            while newHash != hash and self.keys[newHash] != None and self.keys[newHash] != key:
                newHash = self.rehash(newHash, len(self.keys))
            if self.keys[newHash] == None:
                return None
            elif self.keys[newHash] == key:
                toReturn = self.values[newHash]
                self.keys[newHash] = None
                self.values[newHash] = None
                return toReturn
            else:
                return None

    def show(self):
        print(self.keys)
        print(self.values)

    def hash(self, key, size):
        return key % size

    def rehash(self, oldHash, size):
        return (oldHash + 1) % size



ht = HashTable(11)
print("put ##########################")
ht.put(11, "11 - string")
ht.put(22, "22 - string")
ht.put(33, "33 - string")
ht.put(44, "44 - string")
ht.put(12, "12 - string")
ht.put(10, "10 - string")
print("get ##########################")
print(ht.get(22), ht.get(33), ht.get(117))

ht.show()

print("delete ##########################")
print(ht.delete(33), ht.delete(15))
print(ht.get(22), ht.get(33), ht.get(117))

ht.show()

