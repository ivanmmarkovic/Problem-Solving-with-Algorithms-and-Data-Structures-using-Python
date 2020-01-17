
class TreeNode:
    def __init__(self, key = None, leftChild = None, rightChild = None):
        self.key = key
        self.leftChild = leftChild
        self.rightChild = rightChild

    def setRootValue(self, key = None):
        self.key = key

    def getRootValue(self):
        return self.key

    def insertLeft(self, key = None):
        self.leftChild = TreeNode(key, self.leftChild)

    def getLeftChild(self):
        return self.leftChild

    def insertRight(self, key = None):
        self.rightChild = TreeNode(key, None, self.rightChild)

    def getRightChild(self):
        return self.rightChild