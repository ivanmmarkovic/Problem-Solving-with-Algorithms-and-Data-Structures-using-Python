

def createTree(root = None)->list:
    return [root, [], []]

def setRootValue(tree: list, root = None):
    tree[0] = root

def getRootValue(tree: list):
    return tree[0]

def insertLeft(tree: list, root = None):
    subtree: list = tree.pop(1)
    tree.insert(1, [root, subtree, []])

def getLeftChild(tree: list)->list:
    return tree[1]

def insertRight(tree: list, root = None):
    subtree: list = tree.pop(2)
    tree.insert(2, [root, [], subtree])

def getRightChild(tree: list)->list:
    return tree[2]


def buildTree():
    tree: list = createTree("a")

    insertRight(tree, "f")
    insertRight(tree, "c")
    insertLeft(getRightChild(tree), "e")

    insertLeft(tree, "b")
    insertRight(getLeftChild(tree), "d")

    return tree

tree: list = buildTree()
print(tree)