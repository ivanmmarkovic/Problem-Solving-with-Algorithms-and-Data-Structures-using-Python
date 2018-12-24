class BinarySearchTree:
    def __init__(self, key = None, payload = None, parent = None, leftChild = None, rightChild = None):
        self.key = key
        self.payload = payload
        self.parent = parent
        self.leftChild = None
        self.rightChild = None

    def hasParent(self):
        return self.parent != None

    def getParent(self):
        return self.parent

    def isRoot(self):
        return self.parent == None
    
    def isLeaf(self):
        return self.leftChild == None and self.rightChild == None

    def isLeftChild(self):
        return self.parent.leftChild == self

    def isRightChild(self):
        return self.parent.rightChild == self

    def hasLeftChild(self):
        return self.leftChild != None

    def hasRightChild(self):
        return self.rightChild != None

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def put(self, key, payload = None):
        if self.key == None:
            self.key = key
            self.payload = payload
        elif self.key == key:
            self.payload = payload
        elif self.key > key:
            if self.leftChild == None:
                self.leftChild = BinarySearchTree(key, payload, self)
            else:
                self.leftChild.put(key, payload)
        elif self.key < key:
            if self.rightChild == None:
                self.rightChild = BinarySearchTree(key, payload, self)
            else:
                self.rightChild.put(key, payload)

    def get(self, key):
        if self.key == None:
            return None
        elif self.key == key:
            return self
        elif self.key > key:
            if self.leftChild == None:
                return None
            else:
                return self.leftChild.get(key)
        elif self.key < key:
            if self.rightChild == None:
                return None
            else:
                return self.rightChild.get(key)

    def contains(self, key):
        if self.key == None:
            return False
        elif self.key == key:
            return True
        elif self.key > key:
            if self.leftChild == None:
                return False
            else:
                return self.leftChild.contains(key)
        elif self.key < key:
            if self.rightChild == None:
                return False
            else:
                return self.rightChild.contains(key)

    def findMax(self):
        if self.key == None:
            return None
        elif not self.hasRightChild():
            return self
        else:
            return self.rightChild.findMax()

    def findMin(self):
        if self.key == None:
            return None
        elif not self.hasLeftChild():
            return self
        else:
            return self.leftChild.findMin()


    def delete(self, key):
        bst = self.get(key)
        if bst == None:
            return
        elif bst.isRoot() and bst.isLeaf():
            bst = None
        elif bst.isLeaf():
            if bst.isLeftChild():
                bst.parent.leftChild = None
            elif bst.isRightChild():
                bst.parent.rightChild = None
            bst = None
        elif bst.hasBothChildren():
            maxNode = bst.leftChild.findMax()
            tmpKey = maxNode.key
            tmpPayload = maxNode.payload
            bst.delete(maxNode.key)
            bst.key = tmpKey
            bst.payload = tmpPayload
        elif bst.hasLeftChild():
            if bst.isLeftChild():
                bst.parent.leftChild = bst.leftChild
            elif bst.isRightChild():
                bst.parent.rightChild = bst.leftChild
            bst = None
        elif bst.hasRightChild():
            if bst.isLeftChild():
                bst.parent.leftChild = bst.rightChild
            elif bst.isRightChild():
                bst.parent.rightChild = bst.rightChild
            bst = None

            
    def show(self):
        result = ""
        result += str(self.key) + ", "
        if self.leftChild:
            result += self.leftChild.show()
        if self.rightChild:
            result += self.rightChild.show()
        return result

bst = BinarySearchTree()


bst.put(15)
bst.put(7)
bst.put(8)
bst.put(6)
bst.put(30)
bst.put(20)
bst.put(40)
bst.put(18)
bst.put(19)
bst.put(25)
bst.put(24)
bst.put(17)
bst.put(3)
print(bst.show())

print("contains #############")
print(bst.contains(8), bst.contains(19), bst.contains(1101))
print("Min ",bst.findMin().key, ", max ", bst.findMax().key)
bst20 = bst.get(20)
print(bst20.findMax().key, bst20.findMin().key)


print("delete node with value 20 - has both children")
bst.delete(20)
print(bst.show())

