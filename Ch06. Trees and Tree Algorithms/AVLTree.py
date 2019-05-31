class AVLTree:
    def __init__(self, key=None, payload=None, parent=None, leftChild=None, rightChild=None,
                 leftSubtreeHeight=0, rightSubtreeHeight=0, balanceFactor=0):
        self.key = key
        self.payload = payload
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.leftSubtreeHeight = leftSubtreeHeight
        self.rightSubtreeHeight = rightSubtreeHeight
        self.balanceFactor = balanceFactor

    def hasParent(self):
        return self.parent is not None

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

    def put(self, key, payload=None, parent=None):
        if self.key is None or self.key == key:
            self.payload = payload
        elif self.key > key:
            if self.hasLeftChild():
                self.leftChild.put(key, payload)
            else:
                self.leftChild = AVLTree(key, payload, self)
                self.updateBalanceAfterPut(self.leftChild)
        elif self.key < key:
            if self.hasRightChild():
                self.rightChild.put(key, payload)
            else:
                self.rightChild = AVLTree(key, payload, self)
                self.updateBalanceAfterPut(self.rightChild)

    def updateBalanceAfterPut(self, avl):
        if avl.isLeftChild():
            self.leftSubtreeHeight += 1
        if avl.isRightChild():
            self.rightSubtreeHeight += 1
        self.balanceFactor = self.leftSubtreeHeight - self.rightSubtreeHeight

        if self.balanceFactor > 1 or self.balanceFactor < -1:
            self.rebalance()
            return

        if self.balanceFactor != 0 and self.hasParent():
            self.parent.updateBalanceAfterPut(self)

    def rebalance(self):
        if self.balanceFactor > 0:
            if self.leftChild.balanceFactor < 0:
                self.leftChild.rotateLeft()
                self.rotateRight()
            else:
                self.rotateRight()
        elif self.balanceFactor < 0:
            if self.rightChild.balanceFactor > 0:
                self.leftChild.rotateRihgt()
                self.rotateLeft()
            else:
                self.rotateLeft()

    def rotateLeft(self):
        oldRoot = self
        newRoot = self.rightChild
        oldRoot.rightChild = newRoot.leftChild
        if newRoot.hasLeftChild():
            newRoot.leftChild.parent = oldRoot
        newRoot.parent = oldRoot.parent
        if oldRoot.hasParent():
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        oldRoot.parent = newRoot
        newRoot.leftChild = oldRoot

        oldRoot.updateHeightAfterRotation()
        newRoot.updateHeightAfterRotation()

    def rotateRight(self):
        oldRoot = self
        newRoot = self.leftChild
        oldRoot.leftChild = newRoot.rightChild
        if newRoot.hasRightChild():
            newRoot.rightChild.parent = oldRoot
        newRoot.parent = oldRoot.parent
        if oldRoot.hasParent():
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        oldRoot.parent = newRoot
        newRoot.rightChild = oldRoot

        oldRoot.updateHeightAfterRotation()
        newRoot.updateHeightAfterRotation()

    def updateHeightAfterRotation(self):
        if self.hasLeftChild():
            self.leftSubtreeHeight = max(self.leftChild.leftSubtreeHeight, self.leftChild.rightSubtreeHeight) + 1
        else:
            self.leftSubtreeHeight = 0
        if self.hasRightChild():
            self.rightSubtreeHeight = max(self.rightChild.leftSubtreeHeight, self.rightChild.rightSubtreeHeight) + 1
        else:
            self.rightSubtreeHeight = 0
        self.balanceFactor = self.leftSubtreeHeight - self.rightSubtreeHeight

    def delete(self, key):
        nodeToDelete = self.get(key)
        if nodeToDelete.isLeaf():
            if nodeToDelete.hasParent():
                parent = nodeToDelete.parent
                if nodeToDelete.isLeftChild():
                    nodeToDelete.parent.leftChild = None
                    parent.updateAfterDeletion()
                else:
                    nodeToDelete.parent.rightChild = None
                    parent.updateAfterDeletion()
            else:
                nodeToDelete = None
        elif nodeToDelete.hasBothChildren():
            maxInLeftBranch = nodeToDelete.leftChild.findMax()
            tmpKey = maxInLeftBranch.key
            tmpPayload = maxInLeftBranch.payload
            nodeToDelete.key = tmpKey
            nodeToDelete.payload = tmpPayload
            nodeToDelete.delete(tmpKey)
        elif nodeToDelete.hasLeftChild():
            if nodeToDelete.hasParent():
                parent = nodeToDelete.parent
                if nodeToDelete.isLeftChild():
                    nodeToDelete.parent.leftChild = nodeToDelete.leftChild
                    nodeToDelete.leftChild.parent = nodeToDelete.parent
                    parent.updateAfterDeletion()
                else:
                    nodeToDelete.parent.rightChild = nodeToDelete.leftChild
                    nodeToDelete.leftChild.parent = nodeToDelete.parent
                    parent.updateAfterDeletion()
            else:
                nodeToDelete.leftChild.parent = None
        elif nodeToDelete.hasRightChild():
            if nodeToDelete.hasParent():
                parent = nodeToDelete.parent
                if nodeToDelete.isLeftChild():
                    nodeToDelete.rightChild.parent = nodeToDelete.parent
                    nodeToDelete.parent.leftChild = nodeToDelete.rightChild
                    parent.updateAfterDeletion()
                else:
                    nodeToDelete.rightChild.parent = nodeToDelete.parent
                    nodeToDelete.parent.rightChild = nodeToDelete.rightChild
                    parent.updateAfterDeletion()
            else:
                nodeToDelete.rightChild.parent = None

    def updateAfterDeletion(self):
        oldBalanceFactor = self.balanceFactor
        if self.hasLeftChild():
            self.leftSubtreeHeight = max(self.leftChild.leftSubtreeHeight, self.leftChild.rightSubtreeHeight) + 1
        else:
            self.leftSubtreeHeight = 0
        if self.hasRightChild():
            self.rightSubtreeHeight = max(self.rightChild.leftSubtreeHeight, self.rightChild.rightSubtreeHeight) + 1
        else:
            self.rightSubtreeHeight = 0
        self.balanceFactor = self.leftSubtreeHeight - self.rightSubtreeHeight

        if self.balanceFactor > 1 or self.balanceFactor < -1:
            self.rebalance()
            return

        if self.balanceFactor != oldBalanceFactor and self.hasParent():
            self.parent.updateBalanceAfterPut()

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
