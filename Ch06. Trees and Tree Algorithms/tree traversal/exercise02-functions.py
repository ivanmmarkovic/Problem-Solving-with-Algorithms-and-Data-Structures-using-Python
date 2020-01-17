
from tree import TreeNode

def buildTree()->TreeNode:
    tree: TreeNode = TreeNode("a")

    tree.insertRight("f")
    tree.insertRight("c")
    tree.getRightChild().insertLeft("e")

    tree.insertLeft("b")
    tree.getLeftChild().insertRight("d")

    return tree


tree: TreeNode = buildTree()

def preorder(tree: TreeNode):
    if tree is not None:
        print(tree.key)
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

preorder(tree)

def inorder(tree: TreeNode):
    if tree is not None:
        inorder(tree.getLeftChild())
        print(tree.key)
        inorder(tree.getRightChild())

inorder(tree)

def postorder(tree: TreeNode):
    if tree is not None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.key)

postorder(tree)