
class TreeNode:
    def __init__(self, key = None, parent = None, leftChild = None, rightChild = None,
        balanceFactor = 0, leftSubtreeHeight = 0, rightSubtreeHeight = 0):
        self.key = key
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.balanceFactor = 0
        self.leftSubtreeHeight = leftSubtreeHeight
        self.rightSubtreeHeight = rightSubtreeHeight

    def isRoot(self)->bool:
        return self.parent is None

    def hasParent(self)->bool:
        return self.parent is not None

    def isLeftChild(self)->bool:
        return self.parent.leftChild == self

    def isRightChild(self)->bool:
        return self.parent.rightChild == self

    def hasLeftChild(self)->bool:
        return self.leftChild is not None

    def hasRightChild(self)->bool:
        return self.rightChild is not None

    def hasBothChildren(self):
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self):
        return not self.hasLeftChild() and not self.hasRightChild()

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

    def inorder(self):
        if self is not None:
            if self.leftChild is not None:
                self.leftChild.inorder()
            print(self.key, end=", ")
            if self.rightChild is not None:
                self.rightChild.inorder()