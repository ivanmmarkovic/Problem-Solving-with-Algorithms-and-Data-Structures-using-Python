class BinarySearchTree:
    def __init__(self, key=None, parent=None, leftChild=None, rightChild=None):
        self.key = key
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild

    def hasLeftChild(self):
        return self.leftChild is not None

    def hasRightChild(self):
        return self.rightChild is not None

    def isLeaf(self):
        return self.leftChild is None and self.rightChild is None

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def isRoot(self):
        return self.parent is None

    def isLeftChild(self):
        return self.parent.leftChild == self

    def isRightChild(self):
        return self.parent.rightChild == self

    def findMax(self):
        if self.key is None:
            return None
        elif self.hasRightChild():
            return self.rightChild.findMax()
        else:
            return self

    def findMin(self):
        if self.key is None:
            return None
        elif self.hasLeftChild():
            return self.leftChild.findMin()
        else:
            return self

    def put(self, key):
        if self.key is None or self.key == key:
            self.key = key
        elif key < self.key:
            if self.hasLeftChild():
                self.leftChild.put(key)
            else:
                self.leftChild = BinarySearchTree(key, self)
        elif self.key < key:
            if self.hasRightChild():
                self.rightChild.put(key)
            else:
                self.rightChild = BinarySearchTree(key, self)

    def get(self, key):
        if self.key is None:
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

    def delete(self, key):
        bst = self.get(key)
        if bst is None:
            return None
        toReturn = bst
        if bst.isLeaf():
            if bst.isRoot():
                bst = None
            elif bst.isLeftChild():
                bst.parent.leftChild = None
            elif bst.isRightChild():
                bst.parent.rightChild = None
        elif bst.hasBothChildren():
            tmpNode = bst.leftChild.findMax()
            tmpKey = tmpNode.key
            bst.delete(tmpNode.key)
            bst.key = tmpKey
        elif bst.hasLeftChild():
            if bst.isRoot():
                bst.parent.leftChild = None
            elif bst.isLeftChild():
                bst.parent.leftChild = bst.leftChild
                bst.leftChild.parent = bst.parent
            elif bst.isRightChild():
                bst.parent.rightChild = bst.leftChild
                bst.leftChild.parent = bst.parent
        elif bst.hasRightChild():
            if bst.isRoot():
                bst.rightChild.parent = None
            elif bst.isLeftChild():
                bst.parent.leftChild = bst.rightChild
                bst.rightChild.parent = bst.parent
            elif bst.isRightChild():
                bst.parent.rightChild = bst.rightChild
                bst.rightChild.parent = bst.parent

    def contains(self, key):
        if self.key is None:
            return False
        elif self.key == key:
            return True
        elif self.key < key:
            if self.hasRightChild():
                return self.rightChild.contains(key)
            else:
                return False
        elif self.key > key:
            if self.hasLeftChild():
                return self.leftChild.contains(key)
            else:
                return False

    def size(self):
        count = 1
        if self.hasLeftChild():
            count += self.leftChild.size()
        if self.hasRightChild():
            count += self.rightChild.size()
        return count

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
