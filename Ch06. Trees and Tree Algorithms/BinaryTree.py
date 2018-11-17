
class BinaryTree:
    def __init__(self, key):
        self.root = key
        self.leftChild = None
        self.rightChild = None

    def getRootValue(self):
        return self.root

    def setRootValue(self,  key):
        self.root = key

    def getLeftChild(self):
        return self.leftChild

    def insertLeft(self, key):
        oldChild = self.leftChild
        newChild = BinaryTree(key)
        newChild.leftChild = oldChild
        self.leftChild = newChild

    def getRightChild(self):
        return self.rightChild

    def insertRight(self, key):
        oldChild = self.rightChild
        newChild = BinaryTree(key)
        newChild.rightChild = oldChild
        self.rightChild = newChild

#       a
#    /    \
#   b      c
#    \    / \
#     d  e   f

bt = BinaryTree('a')

bt.insertLeft('b')
bt.getLeftChild().insertRight('d')

bt.insertRight('f')
bt.insertRight('c')
bt.getRightChild().insertLeft('e')