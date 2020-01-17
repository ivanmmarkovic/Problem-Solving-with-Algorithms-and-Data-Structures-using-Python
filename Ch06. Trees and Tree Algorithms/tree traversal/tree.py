
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

    def preorder(self):
        print(self.key)
        if self.getLeftChild() is not None:
            self.getLeftChild().preorder()
        if self.getRightChild() is not None:
            self.getRightChild().preorder()

    def inorder(self):
        if self.getLeftChild() is not None:
            self.getLeftChild().inorder()
        print(self.key)
        if self.getRightChild() is not None:
            self.getRightChild().inorder()

    def postorder(self):
        if self.getLeftChild() is not None:
            self.getLeftChild().postorder()
        if self.getRightChild() is not None:
            self.getRightChild().postorder()
        print(self.key)