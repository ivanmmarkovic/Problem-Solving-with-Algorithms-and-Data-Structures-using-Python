from treenode import TreeNode

class AVLTree:
    def __init__(self):
        self.root: TreeNode = None
        self.size = 0

    def isEmpty(self)->bool:
        return self.root == None

    def put(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        elif self.root.key == key:
            self.root.key = key
        else:
            self.putHelper(self.root, key)

    def putHelper(self, node: TreeNode, key): # helper method
        if node.key == key:
            return
        self.size += 1
        if node.key > key:
            if node.hasLeftChild():
                self.putHelper(node.leftChild, key)
            else:
                node.leftChild = TreeNode(key, node)
        else: 
            if node.hasRightChild():
                self.putHelper(node.rightChild, key)  
            else:
                node.rightChild = TreeNode(key, node)
        
    def get(self, key)->TreeNode:
        if self.root is None:
            return None
        else:
            return self.getHelper(self.root, key)

    def getHelper(self, node: TreeNode, key): # helper method
        if node.key == key:
            return node
        elif node.key > key:
            if node.hasLeftChild():
                return self.getHelper(node.leftChild, key)
            else:
                return None
        else:
            if node.hasRightChild():
                return self.getHelper(node.rightChild, key)
            else:
                return None

    def delete(self, key):
        toDelete: TreeNode = self.get(key)
        if toDelete is None:
            return
        self.size -= 1
        if toDelete == self.root:
            if toDelete.isLeaf():
                self.root = None
            elif toDelete.hasBothChildren():
                maxNode: TreeNode = self.root.leftChild.findMax()
                tmpKey = maxNode.key
                self.delete(tmpKey)
                self.root.key = tmpKey
            elif toDelete.hasLeftChild():
                self.root = self.root.leftChild
            else:
                self.root = self.root.rightChild
        else:
            parent: TreeNode = toDelete.parent
            if toDelete.isLeaf():
                if toDelete.isLeftChild():
                    parent.leftChild = None
                else:
                    parent.rightChild = None
            elif toDelete.hasBothChildren():
                maxNode: TreeNode = toDelete.leftChild.findMax()
                tmpKey = maxNode.key
                self.delete(tmpKey)
                toDelete.key = tmpKey
            elif toDelete.hasLeftChild():
                if toDelete.isLeftChild():
                    parent.leftChild = toDelete.leftChild
                    toDelete.leftChild.parent = parent
                else:
                    parent.rightChild = toDelete.leftChild
                    toDelete.leftChild.parent = parent
            else:
                if toDelete.isLeftChild():
                    parent.leftChild = toDelete.rightChild
                    toDelete.rightChild.parent = parent
                else:
                    parent.rightChild = toDelete.rightChild
                    toDelete.rightChild.parent = parent

    def contains(self, key)->bool: 
        if self.root is None:
            return False
        else:
            node: TreeNode = self.root
            found: bool = False
            while node is not None and not found:
                if node.key == key:
                    found = True
                elif node.key < key:
                    node = node.rightChild
                else:
                    node = node.leftChild
            return found
        
    def length(self)->int: 
        return self.size
        
    def findMin(self)->TreeNode: 
        if self.root is None:
            return None
        else:
            node: TreeNode = self.root
            while node.leftChild is not None:
                node = node.leftChild
            return node
        
    def findMax(self)->TreeNode:
        if self.root is None:
            return None
        else:
            node: TreeNode = self.root
            while node.rightChild is not None:
                node = node.rightChild
            return node

    def inorder(self):
        if self.root is not None:
            self.root.inorder()
        print()
            

avl = AVLTree()
avl.put(15)
avl.put(50)
avl.put(7)
avl.put(8)
avl.put(1)
avl.put(9)

avl.inorder()
print(avl.root.key)
print(avl.root.rightChild.key)
print(avl.root.rightChild.leftChild.key)


'''
avl.put(15)
avl.put(7)
avl.put(8)
avl.put(6)
avl.put(30)
avl.put(20)
avl.put(40)
avl.put(18)
avl.put(19)
avl.put(25)
avl.put(24)
avl.put(17)
avl.put(3)


print("contains #############")
print(avl.contains(8), avl.contains(19), avl.contains(1101))
print("Min ",avl.findMin().key, ", max ", avl.findMax().key)



print("delete node with value 20 - has both children")
avl.inorder()
avl.delete(20)
avl.inorder()
'''
