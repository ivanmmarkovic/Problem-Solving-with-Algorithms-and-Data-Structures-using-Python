
class HashMap:
    def __init__(self, size: int = 11):
        self.size = size
        self.keys: list = [None] * self.size
        self.values: list = [None] * self.size
        self.length: int = 0

    def put(self, key, value):
        hash: int = self.hash(key)
        if self.keys[hash] is None:
            self.keys[hash] = [key]
            self.values[hash] = [value]
            self.length += 1
        else:
            found: bool = False
            count: int = 0
            while count < len(self.keys[hash]) and not found:
                if self.keys[hash][count] == key:
                    found = True
                else:
                    count += 1
            if found:
                self.values[hash][count] = value
            else:
                self.keys[hash].append(key)
                self.values[hash].append(value)
                self.length += 1
            
    def get(self, key):
        hash: int = self.hash(key)
        if self.keys[hash] is None:
            return None
        else:
            found: bool = False
            count: int = 0
            while count < len(self.keys[hash]) and not found:
                if self.keys[hash][count] == key:
                    found = True
                else:
                    count += 1
            if found:
                return self.values[hash][count]
            else:
                return None

    def delete(self, key):
        hash: int = self.hash(key)
        if self.keys[hash] is None:
            return
        else:
            found: bool = False
            count: int = 0
            while count < len(self.keys[hash]) and not found:
                if self.keys[hash][count] == key:
                    found = True
                else:
                    count += 1
            if found:
                self.keys[hash].pop(count)
                self.values[hash].pop(count)
                self.length -= 1
            else:
                return None

    def contains(self, key)->bool:
        hash: int = self.hash(key)
        if self.keys[hash] is None:
            return False
        else:
            found: bool = False
            count: int = 0
            while count < len(self.keys[hash]) and not found:
                if self.keys[hash][count] == key:
                    found = True
                else:
                    count += 1
            return found

    def hash(self, key):
        return key % self.size
    
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

