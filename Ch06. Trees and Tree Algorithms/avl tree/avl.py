
from treenode import TreeNode

class AVLTree:
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
                self._updateBalanceFactor(root)
        else:
            if root.hasRightChild():
                self._put(root.rightChild, key)
            else:
                root.rightChild = TreeNode(key, root)
                self._size += 1
                self._updateBalanceFactor(root)

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
                toDelete.key = tmpKey # keep pointer to that node, not root, root might change 
            else:
                self._size -= 1
                if toDelete.hasLeftChild():
                    self.root = self.root.leftChild
                    self.root.parent = None
                else:
                    self.root = self.root.rightChild
                    self.root.parent = None
                self._updateBalanceFactor(self.root) 
        else:
            parent: TreeNode = None
            if toDelete.isLeaf():
                parent = toDelete.parent
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
                parent = toDelete.parent
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
            if parent is not None:
                self._updateBalanceFactor(parent)

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

    def _updateBalanceFactor(self, node: TreeNode):
        oldBalanceFactor: int = node.balanceFactor
        if node.leftChild is None:
            node.leftSubtreeHeight = 0
        else:
            node.leftSubtreeHeight = max(node.leftChild.leftSubtreeHeight, node.leftChild.rightSubtreeHeight) + 1
        if node.rightChild is None:
            node.rightSubtreeHeight = 0
        else:
            node.rightSubtreeHeight = max(node.rightChild.leftSubtreeHeight, node.rightChild.rightSubtreeHeight) + 1
        node.balanceFactor = node.leftSubtreeHeight - node.rightSubtreeHeight
        if node.balanceFactor < -1 or node.balanceFactor > 1:
            self._rebalance(node)
            return
        if node.balanceFactor != oldBalanceFactor and node.hasParent():
            self._updateBalanceFactor(node.parent)

    def _rebalance(self, node: TreeNode):
        if node.balanceFactor < -1:
            if node.rightChild.balanceFactor > 0:
                self._rotateRight(node.rightChild)
            else:
                self._rotateLeft(node)
        else:
            if node.leftChild.balanceFactor < 0:
                self._rotateLeft(node.leftChild)
            else:
                self._rotateRight(node)

    def _rotateLeft(self, node: TreeNode):
        oldRoot: TreeNode = node
        newRoot: TreeNode = node.rightChild
        oldRoot.rightChild = newRoot.leftChild
        if newRoot.hasLeftChild():
            newRoot.leftChild.parent = oldRoot
        newRoot.parent = oldRoot.parent
        if oldRoot.hasParent():
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        else:
            self.root = newRoot
        oldRoot.parent = newRoot
        newRoot.leftChild = oldRoot
        self._updateBalanceFactor(oldRoot)

    def _rotateRight(self, node: TreeNode):
        oldRoot: TreeNode = node
        newRoot: TreeNode = node.leftChild
        oldRoot.leftChild = newRoot.rightChild
        if newRoot.hasRightChild():
            newRoot.rightChild.parent = oldRoot
        newRoot.parent = oldRoot.parent
        if oldRoot.hasParent():
            if oldRoot.isLeftChild():
                oldRoot.parent.leftChild = newRoot
            else:
                oldRoot.parent.rightChild = newRoot
        else:
            self.root = newRoot
        oldRoot.parent = newRoot
        newRoot.rightChild = oldRoot
        self._updateBalanceFactor(oldRoot)

        



avl = AVLTree()
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

print(avl.root.key)
print(avl.root.rightChild.key)

print("contains #############")
print(avl.contains(8), avl.contains(19), avl.contains(1101))
print("Min ",avl.findMin().key, ", max ", avl.findMax().key)
print("delete node with value 20 - has both children")

print("Root key is ", avl.root.key)
print("Checking 18")
print("Contains 18", avl.contains(18))
print("Deleting 18 ...")
avl.delete(18)
print("Contains 18", avl.contains(18))


print("Root key is ", avl.root.key)
print("Contains 20", avl.contains(20))
print("Deleting 20 ...")
avl.delete(20)
print("Contains 20", avl.contains(20))
print("Root key is ", avl.root.key)

print("Contains 8", avl.contains(8))
