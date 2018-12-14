class BinarySearchTree:
    def __init__(self, key = None, payload = None, parent = None, leftChild = None, rightChild = None):
        self.key = key
        self.payload = payload
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild

    def getKey(self):
        return self.key

    def put(self, key, payload = None):
        if self.key == None:
            self.key = key
            self.payload = payload
        elif key < self.key:
            if self.hasLeftChild():
                self.leftChild.put(key, payload)
            else:
                self.leftChild = BinarySearchTree(key, payload, self) 
        elif key > self.key:
            if self.hasRightChild():
                self.rightChild.put(key, payload)
            else:
                self.rightChild = BinarySearchTree(key, payload, self)
        elif self.key == key:
            self.payload = payload

    def get(self, key):
        if self.key == key:
            return self.payload
        elif self.key == None:
            return None
        elif key < self.key:
            if self.hasLeftChild():
                return self.leftChild.get(key)
            else:
                return None
        elif key > self.key:
            if self.hasRightChild():
                return self.rightChild.get(key)
            else:
                return None  

    def getbst(self, key):
        if self.key == key:
            return self
        elif self.key == None:
            return None
        elif key < self.key:
            if self.hasLeftChild():
                return self.leftChild.getbst(key)
            else:
                return None
        elif key > self.key:
            if self.hasRightChild():
                return self.rightChild.getbst(key)
            else:
                return None  

    def contains(self, key):
        if self.key == key:
            return True
        elif self.key == None:
            return False
        elif key < self.key:
            if self.hasLeftChild():
                return self.leftChild.contains(key)
            else:
                return False
        elif key > self.key:
            if self.hasRightChild():
                return self.rightChild.contains(key)
            else:
                return False

    def hasParent(self):
        return self.parent != None

    def getParent(self):
        return self.parent

    def isLeftChild(self):
        return self.parent != None and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent != None and self.parent.rightChild == self

    def hasLeftChild(self):
        return self.leftChild != None
    
    def hasRightChild(self):
        return self.rightChild != None

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild != None and self.leftChild != None

    def delete(self, key):
        bst = self.getbst(key)
        if bst == None:
            return None
        else:
            if bst.isRoot() and bst.isLeaf():
                bst = None
            elif bst.isLeaf():
                if bst.isLeftChild():
                    bst.parent.leftChild = None
                elif bst.isRightChild():
                    bst.parent.rightChild = None
            elif bst.hasBothChildren():
                maxInLeft = bst.leftChild.findMax()
                key = maxInLeft.key
                payload = maxInLeft.payload
                self.delete(maxInLeft.key) 
                bst.key = key
                bst.payload = payload
            elif bst.hasAnyChildren():
                if bst.hasLeftChild():
                    if bst.isLeftChild():
                        bst.parent.leftChild = bst.leftChild
                        bst.leftChild.parent = bst.parent
                        bst = None
                    elif bst.isRightChild():
                        bst.parent.rightChild = bst.leftChild
                        bst.leftChild.parent = bst.parent
                        bst = None
                elif bst.hasRightChild():
                    if bst.isLeftChild():
                        bst.parent.leftChild = bst.rightChild
                        bst.rightChild.parent = bst.parent
                        bst = None
                    elif bst.isRightChild():
                        bst.parent.rightChild = bst.rightChild
                        bst.rightChild.parent = bst.parent
                        bst = None

    def findMin(self):
        if self.hasLeftChild():
            return self.leftChild.findMin()
        else:
            return self

    def findMax(self):
        if self.hasRightChild():
            return self.rightChild.findMax()
        else:
            return self

    def print(self): # preorder
        print("Key: ", self.key, "Payload : ", self.payload)
        if self.hasLeftChild():
            self.leftChild.print()
        if self.hasRightChild():
            self.rightChild.print()



bst = BinarySearchTree()

print("Checking put method : ")
bst.put(115)
bst.put(3)
bst.put(200)
bst.put(4)
bst.put(210)
bst.put(150)
bst.put(160)
bst.put(1)
bst.put(140)
bst.put(130)
bst.put(141)
bst.put(211)


bst.print()   
print("--------------")

print("Checking put method again : ")
bst.put(3, "Number 3")
bst.put(4, "Number 4")
bst.print()
print("--------------")

print("Checking get method : ")
print(bst.get(3))
print(bst.get(1001))
print("--------------")


print("Checking contains method : ")
print(bst.contains(3))
print(bst.contains(1001))
print(bst.contains(115))
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
        
print(bst.findMin().key, bst.rightChild.findMin().key)

# print(bst.getbst(150).hasBothChildren())
print("---------------->", bst.getbst(140).rightChild.key)
bst.delete(150)
print(bst.rightChild.leftChild.key)
print(bst.rightChild.leftChild.hasBothChildren())
print(bst.getbst(140).rightChild)
bst.print()






