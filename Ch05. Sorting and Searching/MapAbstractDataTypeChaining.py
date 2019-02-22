class HashTable:
    def __init__(self, size):
        self.keys = [None] * size
        self.values = [None] * size

    def put(self, key, value):
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == None:
            self.keys[hash] = [key]
            self.values[hash] = [value]
        else:
            self.keys[hash] = self.keys[hash] + [key]
            self.values[hash] =self.values[hash] + [value]

    def get(self, key):
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == None:
            return None
        else:
            ret_value = None
            found = False
            pos = 0
            while pos < len(self.keys[hash]) and not found:
                if self.keys[hash][pos] == key:
                    ret_value = self.values[hash][pos]
                    found = True
                else:
                    pos += 1
            return ret_value


    def delete(self, key):
        ret_value = None
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == None:
            return ret_value
        else:
            found = False
            pos = 0
            while pos < len(self.keys[hash]) and not found:
                if self.keys[hash][pos] == key:
                    found = True
                else:
                    pos += 1
            if found:
                ret_value = self.values[hash][pos]
                self.keys[hash].pop(pos)
                self.values[hash].pop(pos)
            return ret_value

    def size(self):
        count = 0
        pos = 0
        while pos < len(self.keys):
            if self.keys[pos] != None:
                count += len(self.keys[pos])
            pos += 1
        return count

    def contains(self, key):
        hash = self.hash(key, len(self.keys))
        if self.keys[hash] == None:
            return False
        else:
            found = False
            pos = 0
            while pos < len(self.keys[hash]) and not found:
                if self.keys[hash][pos] == key:
                    found = True
                else:
                    pos += 1
            if found:
                return True
            else:
                return False

    def hash(self, item, size):
        return item % size

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