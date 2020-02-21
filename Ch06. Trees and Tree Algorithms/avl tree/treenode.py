

class TreeNode:
    def __init__(self, key = None, parent = None, leftChild = None, rightChild = None, 
                        leftSubtreeHeight: int = 0, rightSubtreeHeight: int = 0, balanceFactor: int = 0):
        self.key = key
        self.parent = parent
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.leftSubtreeHeight = leftSubtreeHeight
        self.rightSubtreeHeight = rightSubtreeHeight
        self.balanceFactor = balanceFactor

    def hasParent(self)->bool:
        return self.parent is not None

    def hasLeftChild(self)->bool:
        return self.leftChild is not None

    def hasRightChild(self)->bool:
        return self.rightChild is not None

    def hasBothChildren(self)->bool:
        return self.hasLeftChild() and self.hasRightChild()

    def isLeaf(self)->bool:
        return not self.hasLeftChild() and not self.hasRightChild()

    def isLeftChild(self)->bool:
        return self.parent.leftChild == self

    def isRightChild(self)->bool:
        return self.parent.rightChild == self

    def findMin(self):
        node = self
        while node.leftChild is not None:
            node = node.leftChild
        return node

    def findMax(self):
        node = self
        while node.rightChild is not None:
            node = node.rightChild
        return node
