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
            new_hash = self.rehash(hash, len(self.keys))
            while new_hash != hash and self.keys[new_hash] != None and self.keys[new_hash] != key:
                new_hash = self.rehash(new_hash, len(self.keys))
            if self.keys[new_hash] == None:
                self.keys[new_hash] = key
                self.values[new_hash] = value
            elif self.keys[new_hash] == key:
                self.values[new_hash] = value

    def get(self, key):
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == None:
            return None
        elif self.keys[hash] == key:
            return self.values[hash]
        else:
            new_hash = self.rehash(hash, len(self.keys))
            while new_hash != hash and self.keys[new_hash] != None and self.keys[new_hash] != key:
                new_hash = self.rehash(new_hash, len(self.keys))
            if self.keys[new_hash] == None:
                return None
            elif self.keys[new_hash] == key:
                return self.values[new_hash]
            else:
                return None

    def delete(self, key):
        ret_value = None
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == key:
            ret_value =self.values[hash]
            self.keys[hash] = None
            self.values[hash] = None
            return ret_value
        elif self.keys[hash] == None:
            return ret_value
        else:
            new_hash = self.rehash(hash, len(self.keys))
            while new_hash != hash and self.keys[new_hash] != None and self.keys[new_hash] != key:
                new_hash = self.rehash(new_hash, len(self.keys))
            if self.keys[new_hash] == None:
                return ret_value
            elif self.keys[new_hash] == key:
                ret_value = self.values[new_hash]
                self.keys[new_hash] = None
                self.values[new_hash] = None
                return ret_value
            else:
                return ret_value

    def size(self):
        count = 0
        pos = 0
        while pos < len(self.keys):
            if self.keys[pos] != None:
                count += 1
            pos += 1
        return count

    def contains(self, key):
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == None:
            return False
        elif self.keys[hash] == key:
            return True
        else:
            new_hash = self.rehash(hash, len(self.keys))
            while new_hash != hash and self.keys[new_hash] != None and self.keys[new_hash] != key:
                new_hash = self.rehash(new_hash, len(self.keys))
            if self.keys[new_hash] == None:
                return False
            elif self.keys[new_hash] == key:
                return True
            else:
                return False

    def hash(self, item, size):
        return item % size

    def rehash(self, old_hash, size):
        return (old_hash + 1) % size

    def show(self):
        print(self.keys)
        print(self.values)

ht = HashTable(11)
print("put ##########################")
ht.put(11, "11 - string")
ht.put(22, "22 - string")
ht.put(33, "33 - string")
ht.put(44, "44 - string")
ht.put(12, "12 - string")
ht.put(10, "10 - string")

print("size #########################", ht.size())
print("contains #########################", ht.contains(33))

print("get ##########################")
print(ht.get(22), ht.get(33), ht.get(117))

ht.show()

print("delete ##########################")
print(ht.delete(33), ht.delete(15))
print(ht.get(22), ht.get(33), ht.get(117))
print("size #########################", ht.size())
print("contains #########################", ht.contains(33))
ht.show()