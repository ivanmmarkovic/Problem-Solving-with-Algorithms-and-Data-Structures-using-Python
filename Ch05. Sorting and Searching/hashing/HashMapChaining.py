class KeyValue:
    def __init__(self, key: None, value: None):
        self.key = key
        self.value = value

class HashMap:
    def __init__(self, size:int = 11):
        self.size: int = size
        self.items: list = [None] * self.size
        self.length: int = 0

    def put(self, key, value):
        keyValue: KeyValue = KeyValue(key, value)
        hash: int = self.hash(key)
        if self.items[hash] is None:
            self.items[hash] = [keyValue]
            self.length += 1
        else:
            count: int = 0
            found: bool = False
            while count < len(self.items[hash]) and not found:
                if self.items[hash][count].key == keyValue.key:
                    found = True
                else:
                    count += 1
            if found:
                self.items[hash][count] = keyValue
            else:
                self.items[hash].append(keyValue)
                self.length += 1

    def get(self, key):
        hash: int = self.hash(key)
        if self.items[hash] is None:
            return None
        else:
            count: int = 0
            found: bool = False
            while count < len(self.items[hash]) and not found:
                if self.items[hash][count].key == key:
                    found = True
                else:
                    count += 1
            if found:
                return self.items[hash][count].value
            else:
                return None


    def contains(self, key)->bool:
        hash: int = self.hash(key)
        if self.items[hash] is None:
            return False
        else:
            count: int = 0
            found: bool = False
            while count < len(self.items[hash]) and not found:
                if self.items[hash][count].key == key:
                    found = True
                else:
                    count += 1
            return found

    def delete(self, key):
        hash: int = self.hash(key)
        if self.items[hash] is None:
            return None
        else:
            count: int = 0
            found: bool = False
            while count < len(self.items[hash]) and not found:
                if self.items[hash][count].key == key:
                    found = True
                else:
                    count += 1
            if found:
                return self.items[hash].pop(count)
            else:
                return None

    def hash(self, key):
        return key % self.size


ht: HashMap = HashMap()

ht.put(11, "string 11")
ht.put(22, "string 22")
ht.put(33, "string 33")
ht.put(44, "string 44")
ht.put(12, "string 12")

ht.put(21, "string 21")

print(ht.contains(11), ht.contains(33), ht.contains(21), ht.contains(117))
print(ht.delete(11).value)
print(ht.contains(22))
print(ht.get(22))
