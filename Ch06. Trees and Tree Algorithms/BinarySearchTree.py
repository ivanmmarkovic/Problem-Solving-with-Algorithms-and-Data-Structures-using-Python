

class BinarySearchTree:
    def __init__(self, key = None, payload = None, parent = None, leftChild = None, rightChild = None):
        self.key = key
        self.payload = payload
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild

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
        if self.key == None or self.key == key:
            self.key = key
            self.payload = payload
        elif self.key > key:
            if self.hasLeftChild():
                self.leftChild.put(key, payload)
            else:
                self.leftChild = BinarySearchTree(key,payload, self)
        elif self.key < key:
            if self.hasRightChild():
                self.rightChild.put(key,payload)
            else:
                self.rightChild = BinarySearchTree(key, payload, self)

    def get(self, key):
        if self.key == None:
            return None
        elif self.key == key:
            return self
        elif self.key > key:
            if self.hasLeftChild():
                return self.leftChild.get(key)
            else:
                return None
        elif self.key < key:
            if self.hasRightChild():
                return self.rightChild.get(key)
            else:
                return None

    def contains(self, key):
        if self.key == None:
            return False
        elif self.key == key:
            return True
        elif self.key > key:
            if self.hasLeftChild():
                return self.leftChild.contains(key)
            else:
                return False
        elif self.key < key:
            if self.hasRightChild():
                return self.rightChild.contains(key)
            else:
                return False

    def findMin(self):
        if self.key == None:
            return None
        elif self.hasLeftChild():
            return self.leftChild.findMin()
        else:
            return self

    def findMax(self):
        if self.key == None:
            return None
        elif self.hasRightChild():
            return self.rightChild.findMax()
        else:
            return self

    def delete(self,key):
        bst = self.get(key)
        if bst.isRoot():
            if bst.isLeaf():
                bst = None
            elif bst.hasBothChildren():
                toDelete = bst.leftChild.findMax()
                tmpKey = toDelete.key
                tmpPayload = toDelete.payload
                bst.delete(toDelete.key)
                bst.key = tmpKey
                bst.payload = tmpPayload
            elif bst.hasLeftChild():
                bst.leftChild.parent = None
            elif bst.hasRightChild():
                bst.rightChild.parent = None
        elif bst.isLeaf():
            if bst.isLeftChild():
                bst.parent.leftChild == None
            elif bst.isRightChild():
                bst.parent.rightChild == None
        elif bst.hasBothChildren():
            toDelete = bst.leftChild.findMax()
            tmpKey = toDelete.key
            tmpPayload = toDelete.payload
            bst.delete(toDelete.key)
            bst.key = tmpKey
            bst.payload = tmpPayload
        elif bst.hasLeftChild():
            if bst.isLeftChild():
                bst.parent.leftChild = bst.leftChild
            elif bst.isRightChild():
                bst.parent.rightChild = bst.leftChild
        elif bst.hasRightChild():
            if bst.isLeftChild():
                bst.parent.leftChild = bst.rightChild
            elif bst.isRightChild():
                bst.parent.rightChild = bst.rightChild

    def show(self):
        result = ""
        if self.hasLeftChild():
            result += self.leftChild.show()
        result += str(self.key) + ", "
        if self.hasRightChild():
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
print(bst20.key)
print(bst20.findMax().key, bst20.findMin().key)


print("delete node with value 20 - has both children")
bst.delete(20)
print(bst.show())
        

        
