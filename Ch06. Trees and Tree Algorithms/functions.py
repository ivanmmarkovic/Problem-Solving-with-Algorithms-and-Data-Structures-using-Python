
def createBinaryTree(root):
    return [root, [], []]

def getRootValue(bt):
    return bt[0]

def insertLeft(bt, key):
    t = bt.pop(1)
    bt.insert(1, [key, t, []])

def insertRight(bt, key):
    t = bt.pop(2)
    bt.insert(2, [key, [], t])

def getLeftChild(bt):
    return bt[1]

def getRightChild(bt):
    return bt[2]

x = createBinaryTree('a')
insertLeft(x, 'b')
insertRight(x, 'c')
insertRight(getRightChild(x), 'd')
insertLeft(getRightChild(getRightChild(x)), 'e')
print(x)

#       a
#    /    \
#   b      c
#    \    / \
#     d  e   f

def buildTree():
    bt = createBinaryTree('a')
    insertRight(bt, 'f')
    insertRight(bt, 'c')
    insertLeft(getRightChild(bt), 'e')

    insertLeft(bt,'b')
    insertRight(getLeftChild(bt), 'd')

    return bt
bt = buildTree()
print(bt)