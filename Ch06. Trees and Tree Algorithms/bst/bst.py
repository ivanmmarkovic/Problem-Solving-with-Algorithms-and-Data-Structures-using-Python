
from treenode import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root: TreeNode = None
        self._size: int = 0

    def size(self)->int:
        return self._size

    def isEmpty(self)->bool:
        return self.root is None

    def put(self, key):
        if self.root is None:
            self.root = TreeNode(key)
            self._size += 1
        else: 
            self._put(self.root, key)
    
    def _put(self, root: TreeNode, key):
        if root.key == key:
            root.key = key
        elif key < root.key:
            if root.hasLeftChild():
                self._put(root.leftChild, key)
            else:
                root.leftChild = TreeNode(key, root)
                self._size += 1
        else:
            if root.hasRightChild():
                self._put(root.rightChild, key)
            else:
                root.rightChild = TreeNode(key, root)
                self._size += 1

    def get(self, key)->TreeNode:
        if self.root is None:
            return None
        else:
            return self._get(self.root, key)

    def _get(self, root: TreeNode, key)->TreeNode:
        if root.key == key:
            return root
        elif key < root.key:
            if root.hasLeftChild():
                return self._get(root.leftChild, key)
            else:
                return None
        else:
            if root.hasRightChild():
                return self._get(root.rightChild, key)
            else:
                return None
    '''
    def contains(self, key)->bool:
        if self.root is None:
            return False
        else:
            return self._contains(self.root, key)

    def _contains(self, root: TreeNode, key)->bool:
        if root.key == key:
            return True
        elif key < root.key:
            if root.hasLeftChild():
                return self._contains(root.leftChild, key)
            else:
                return False
        else:
            if root.hasRightChild():
                return self._contains(root.rightChild, key)
            else:
                return False
    '''
    def contains(self, key)->bool:
        if self.root is None:
            return False
        else:
            found: bool = False
            node: TreeNode = self.root
            while node is not None and not found:
                if node.key == key:
                    found = True
                elif key < node.key:
                    node = node.leftChild
                else:
                    node = node.rightChild
            return found

    def delete(self, key):
        if self.isEmpty():
            return None
        toDelete: TreeNode = self.get(key)
        if toDelete is None:
            return
        if toDelete == self.root:
            if toDelete.isLeaf():
                self.root = None
                self._size -= 1
            elif toDelete.hasBothChildren():
                minNode: TreeNode = toDelete.rightChild.findMin()
                tmpKey = minNode.key
                self.delete(tmpKey)
                self.root.key = tmpKey
            else:
                self._size -= 1
                if toDelete.hasLeftChild():
                    self.root = self.root.leftChild
                    self.root.parent = None
                else:
                    self.root = self.root.rightChild
                    self.root.parent = None 
        else:
            if toDelete.isLeaf():
                self._size -= 1
                if toDelete.isLeftChild():
                    toDelete.parent.leftChild = None
                else:
                    toDelete.parent.rightChild = None
            elif toDelete.hasBothChildren():
                minNode: TreeNode = toDelete.rightChild.findMin()
                tmpKey = minNode.key
                self.delete(tmpKey)
                toDelete.key = tmpKey
            else:
                self._size -= 1
                if toDelete.hasLeftChild():
                    if toDelete.isLeftChild():
                        toDelete.parent.leftChild = toDelete.leftChild
                        toDelete.leftChild.parent = toDelete.parent
                    else:
                        toDelete.parent.rightChild = toDelete.leftChild
                        toDelete.leftChild.parent = toDelete.parent
                else:
                    if toDelete.isLeftChild():
                        toDelete.parent.leftChild = toDelete.rightChild
                        toDelete.rightChild.parent = toDelete.parent
                    else:
                        toDelete.parent.rightChild = toDelete.rightChild
                        toDelete.rightChild.parent = toDelete.parent

    def findMin(self)->TreeNode:
        if self.isEmpty():
            return None
        else:
            node: TreeNode = self.root
            while node.leftChild is not None:
                node = node.leftChild
            return node

    def findMax(self)->TreeNode:
        if self.isEmpty():
            return None
        else:
            node: TreeNode = self.root
            while node.rightChild is not None:
                node = node.rightChild
            return node

    


bst = BinarySearchTree()
bst.put(15)
bst.put(7)
bst.put(8)
bst.put(6)
bst.put(30)
bst.put(20)
bst.put(40)
bst.put(18)
bst.put(19)
bst.put(25)
bst.put(24)
bst.put(17)
bst.put(3)

print(bst.root.key)
print(bst.root.rightChild.key)

print("contains #############")
print(bst.contains(8), bst.contains(19), bst.contains(1101))
print("Min ",bst.findMin().key, ", max ", bst.findMax().key)
print("delete node with value 20 - has both children")

print(bst.contains(20))
bst.delete(20)
print(bst.contains(20))

