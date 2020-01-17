from tree import TreeNode

def buildTree()->TreeNode:
    tree: TreeNode = TreeNode("a")

    tree.insertRight("f")
    tree.insertRight("c")
    tree.getRightChild().insertLeft("e")

    tree.insertLeft("b")
    tree.getLeftChild().insertRight("d")

    return tree


