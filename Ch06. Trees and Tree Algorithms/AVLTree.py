# NOT FINISHED
# delete method



class AVLTree:
    def __init__(self, key = None, payload = None, parent = None, leftChild = None, rightChild = None,
                 leftHeight = 0, rightHeight = 0, balanceFactor = 0):
        self.key = key
        self.payload = payload
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.leftHeight = leftHeight
        self.rightHeight = rightHeight
        self.balanceFactor = balanceFactor

    def hasParent(self):
        return self.parent != None

    def getParent(self):
        return self.parent

    def isRoot(self):
        return self.parent == None

    def isLeaf(self):
        return self.leftChild == None and self.rightChild == None

    def hasLeftChild(self):
        return self.leftChild != None

    def hasRightChild(self):
        return self.rightChild != None

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def isLeftChild(self):
        return self.parent.leftChild == self

    def isRightChild(self):
        return self.parent.rightChild == self


    def put(self, key, payload = None):
        if self.key == None:
            self.key = key
            self.payload = payload
        elif self.key > key:
            if self.hasLeftChild():
                self.leftChild.put(key, payload)
            else:
                self.leftChild = AVLTree(key, payload, self)
                self.updateHeight(self.leftChild)
        elif self.key < key:
            if self.hasRightChild():
                self.rightChild.put(key, payload)
            else:
                self.rightChild = AVLTree(key, payload,self)
                self.updateHeight(self.rightChild)

    def updateHeight(self, node):
        if node.isLeftChild():
            self.leftHeight += 1
            #self.balanceFactor += 1
        elif node.isRightChild():
            self.rightHeight += 1
            # self.balanceFactor -= 1
        self.balanceFactor = self.leftHeight - self.rightHeight

        if self.balanceFactor < -1 or self.balanceFactor > 1:
            self.rebalance()
            return

        if self.hasParent() and self.balanceFactor != 0:
            self.parent.updateHeight(self)

    def updateHeightAfterRotation(self):
        if self.hasLeftChild():
            self.leftHeight = max(self.leftChild.leftHeight, self.leftChild.rightHeight) + 1
        else:
            self.leftHeight = 0

        if self.hasRightChild():
            self.rightHeight = max(self.rightChild.leftHeight, self.rightChild.rightHeight) + 1
        else:
            self.rightHeight = 0

        self.balanceFactor = (self.leftHeight - self.rightHeight)

    def rebalance(self):
        if self.balanceFactor < 0:
            if self.rightChild.balanceFactor > 0:
                self.rightChild.rotateRight()
                self.rotateLeft()
            else:
                self.rotateLeft()
        elif self.balanceFactor > 0:
            if self.leftChild.balanceFactor < 0:
                self.leftChild.rotateLeft()
                self.rotateRight()
            else:
                self.rotateRight()

    def rotateLeft(self):
        oldRoot = self
        newRoot = oldRoot.rightChild
        # children
        oldRoot.rightChild = newRoot.leftChild
        if newRoot.hasLeftChild():
            newRoot.leftChild.parent = oldRoot
        # oldRoot parent
        newRoot.parent = oldRoot.parent
        if oldRoot.hasParent():
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        # set parent child relation
        oldRoot.parent = newRoot
        newRoot.leftChild = oldRoot

        # first oldRoot, then newRoot - use data from oldRoot
        oldRoot.updateHeightAfterRotation()
        newRoot.updateHeightAfterRotation()

    def rotateRight(self):
        oldRoot = self
        newRoot = oldRoot.leftChild
        # children
        oldRoot.leftChild = newRoot.rightChild
        if newRoot.hasRightChild():
            newRoot.rightChild.parent = oldRoot
        # oldRoot parent
        newRoot.parent = oldRoot.parent
        if oldRoot.hasParent():
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        # set parent child relation
        oldRoot.parent = newRoot
        newRoot.leftChild = oldRoot

        # first oldRoot, then newRoot - use data from oldRoot
        oldRoot.updateHeightAfterRotation()
        newRoot.updateHeightAfterRotation()



