
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
            elif self.keys[newHash] == key:
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


    def hash(self, key, size):
        return key % size

    def rehash(self, oldHash, size):
        return (oldHash + 1) % size

    

ht = HashTable(11)
ht.put(11, "eleven")
ht.put(22, "twenty-two")
ht.put(33, "thirty-three")
ht.put(12, "twelve")
print(ht.get(11), ht.get(33), ht.get(133))
