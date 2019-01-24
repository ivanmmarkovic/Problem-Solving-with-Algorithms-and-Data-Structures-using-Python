# NOT FINISHED
# update balance rotateRight
# delete method
# height property


class AVLTree:

    def __init__(self, key = None, payload = None, parent = None, leftChild = None, rightChild = None, balanceFactor = 0):
        self.key = key
        self.payload = payload
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.balanceFactor = balanceFactor

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

    def put(self, key, payload):
        if self.key == None:
            self.key = key
            self.payload = payload
        elif self.key == key:
            self.payload = payload
        elif self.key > key:
            if self.hasLeftChild():
                self.leftChild.put(key, payload)
            else:
                self.leftChild = AVLTree(key, payload, self)
                self.leftChild.height = self.leftChild.updateHeight()
                self.updateBalance(self.leftChild)
        elif self.key < key:
            if self.hasRightChild():
                self.rightChild.put(key, payload)
            else:
                self.rightChild = AVLTree(key, payload, self)
                self.rightChild.height = self.rightChild.updateHeight()
                self.updateBalance(self.rightChild)

    def updateHeigth(self):
        if self.parent == None:
            return 0
        else:
            return 1 + self.parent.updateHeigth()
            
    def updateBalance(self, node):
        if node.isLeftChild():
            self.balanceFactor += 1
        elif node.isRightChild():
            self.balanceFactor -= 1
        
        if self.balanceFactor < -1 or self.balanceFactor > 1:
            self.rebalance()
            return

        if self.hasParent() and self.balanceFactor != 0:
            self.parent.updateBalance(self)

    def rebalance(self):
        if self.balanceFactor > 0:
            if self.leftChild.balanceFactor < 0:
                self.leftChild.rotateLeft()
                self.rotateRight()
            else:
                self.rotateRight()
        elif self.balanceFactor < 0:
            if self.rightChild.balanceFactor > 0:
                self.rightChild.rotateRight()
                self.rotateLeft()
            else:
                self.rotateLeft()

    def rotateLeft(self):
        oldRoot = self
        newRoot = self.leftChild
        # children
        oldRoot.rightChild = newRoot.leftChild
        if newRoot.hasLeftChild():
            newRoot.leftChild.parent = oldRoot
        # oldRoot parent
        newRoot.parent = oldRoot.parent
        if oldRoot.hasParent():
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            elif oldRoot.isRightChild():
                oldRoot.parent.rightChild = newRoot
        # set parent child relation
        oldRoot.parent = newRoot
        newRoot.leftChild = oldRoot

    def rotateRight(self):
        oldRoot = self
        newRoot = oldRoot.leftChild
        # children
        oldRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = oldRoot
        # oldRoot parent
        newRoot.parent = oldRoot.parent
        if oldRoot.hasParent():
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            elif oldRoot.isRightChild():
                oldRoot.parent.rightChild = newRoot
        # set parent child relation
        newRoot.rightChild = oldRoot
        oldRoot.parent = newRoot

