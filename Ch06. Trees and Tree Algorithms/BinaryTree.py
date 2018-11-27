
class BinaryTree:
    def __init__(self, key):
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def setRootValue(self, key):
        self.key = key

    def getRootValue(self):
        return self.key

    def insertLeft(self, key):
        newChild = BinaryTree(key)
        newChild.leftChild = self.leftChild
        self.leftChild = newChild

    def insertRight(self, key):
        newChild = BinaryTree(key)
        newChild.rightChild = self.rightChild
        self.rightChild = newChild

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

