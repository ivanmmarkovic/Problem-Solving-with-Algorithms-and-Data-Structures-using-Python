

class AVLTree:
    def __init__(self, key: int = None, parent = None, leftChild = None, rightChild = None,
        leftSubtreeHeight: int = 0, rightSubtreeHeight: int = 0, balanceFactor: int = 0):
        self.key = key
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.leftSubtreeHeight = leftSubtreeHeight
        self.rightSubtreeHeight = rightSubtreeHeight
        self.balanceFactor = balanceFactor

    def isRoot(self)-> bool:
        return self.parent is None

    def isLeftChild(self)-> bool:
        return self.parent.leftChild == self

    def isRightChild(self)-> bool:
        return self.parent.rightChild == self

    def hasParent(self)-> bool:
        return self.parent is not None

    def hasLeftChild(self)-> bool:
        return self.leftChild is not None

    def hasRightChild(self)-> bool:
        return self.rightChild is not None

    def isLeaf(self):
        return self.leftChild is None and self.rightChild is None

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def put(self, key: int):
        if self.key is None or self.key == key:
            self.key = key
        elif key < self.key:
            if self.hasLeftChild():
                self.leftChild.put(key)
            else:
                self.leftChild = BinarySearchTree(key, self)
                self.updateHeight(self.leftChild)
        else:
            if self.hasRightChild():
                self.rightChild.put(key)
            else:
                self.rightChild = BinarySearchTree(key, self)
                self.updateHeight(self.rightChild)
    
    def get(self, key):
        if self.key is None:
            return None
        elif self.key == key:
            return self
        elif self.key > key:
            if self.hasLeftChild():
                return self.leftChild.get(key)
            else:
                return self
        else:
            if self.hasRightChild():
                return self.rightChild.get(key)
            else:
                return None

    def findMax(self):
        if self.key is None:
            return None
        else:
            if self.hasRightChild():
                return self.rightChild.findMax()
            else:
                return self

    def findMin(self):
        if self.key is None:
            return None
        else:
            if self.hasLeftChild():
                return self.leftChild.findMin()
            else:
                return self

    def contains(self, key)-> bool:
        if self.key is None:
            return False
        elif self.key == key:
            return True
        elif self.key > key:
            if self.hasLeftChild():
                return self.leftChild.contains(key)
            else:
                return False
        else:
            if self.hasRightChild():
                return self.rightChild.contains(key)
            else:
                return False

    def size(self):
        count: int = 1
        if self.hasLeftChild():
            count += self.leftChild.size()
        if self.hasRightChild():
            count += self.rightChild.size()
        return count

    def delete(self, key):
        tmp = self.get(key)
        if tmp is None:
            return
        parent = None
        if tmp.isLeaf():
            if tmp.isRoot():
                tmp.key = None
            else:
                parent = tmp.parent
                if tmp.isLeftChild():
                    tmp.parent.leftChild = None
                else:
                    tmp.parent.rightChild = None
        elif tmp.hasBothChildren():
            maxBinarySearchTree = tmp.leftChild.findMax()
            tmpKey: int = maxBinarySearchTree.key
            self.delete(tmpKey)
            tmp.key = tmpKey
        elif tmp.hasLeftChild():
            parent = tmp.parent
            if tmp.isRoot():
                tmp.leftChild.parent = None
            elif tmp.isRightChild():
                tmp.parent.rightChild = tmp.leftChild
                tmp.leftChild.parent = tmp.parent
            else:
                tmp.parent.leftChild = tmp.leftChild
                tmp.leftChild = tmp.parent
        else:
            parent = tmp.parent
            if tmp.isRoot():
                tmp.rightChild.parent = None
            elif tmp.isRightChild():
                tmp.parent.rightChild = tmp.rightChild
                tmp.rightChild.parent = tmp.parent
            else:
                tmp.parent.leftChild = tmp.rightChild
                tmp.rightChild.parent = tmp.parent
        if parent is not None:
            parent.updateHeightAfterDeletion()

    def inorder(self):
        if self.hasLeftChild():
            self.leftChild.inorder()
        print(self.key)
        if self.hasRightChild():
            self.rightChild.inorder()

    def updateHeight(self, tree):
        if tree.isLeftChild():
            self.leftSubtreeHeight += 1
        if tree.isRightChild():
            self.rightSubtreeHeight += 1
        self.balanceFactor = self.leftSubtreeHeight - self.rightSubtreeHeight
        if self.balanceFactor < -1 or self.balanceFactor > 1:
            self.rebalance()
            return
        if self.balanceFactor != 0 and self.hasParent():
            self.parent.updateHeight(self)

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

    def updateHeightAfterDeletion(self):
        if self.hasLeftChild():
            self.leftSubtreeHeight = max(self.leftChild.leftSubtreeHeight, self.leftChild.rightSubtreeHeight) + 1
        else:
            self.leftSubtreeHeight = 0
        if self.hasRightChild():
            self.rightSubtreeHeight = max(self.rightChild.leftSubtreeHeight, self.rightChild.rightSubtreeHeight) + 1
        else:
            self.rightSubtreeHeight = 0
        self.balanceFactor = self.leftSubtreeHeight - self.rightSubtreeHeight
        if self.balanceFactor < -1 or self.balanceFactor > 1:
            self.rebalance()
            return
        if self.balanceFactor != 0 and self.hasParent():
            self.parent.updateHeight(self)

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
        newRoot.leftChild = oldRoot
        oldRoot.parent = newRoot

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



