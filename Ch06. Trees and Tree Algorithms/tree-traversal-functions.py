from BinaryTree import BinaryTree

#       a
#    /    \
#   b      c
#    \    / \
#     d  e   f

bt = BinaryTree('a')

bt.insertRight('f')
bt.insertRight('c')
bt.getRightChild().insertLeft('e')

bt.insertLeft('b')
bt.getLeftChild().insertRight('d')

def preorder(bt):
    if bt:
        print(bt.getRootValue())
        preorder(bt.getLeftChild())
        preorder(bt.getRightChild())

print("Preorder : ")
preorder(bt)
print("---------------------------")

def inorder(bt):
    if bt:
        inorder(bt.getLeftChild())
        print(bt.getRootValue())
        inorder(bt.getRightChild())

print("Inorder :")
inorder(bt)
print("----------------------------")

def postorder(bt):
    if bt:
        postorder(bt.getLeftChild())
        postorder(bt.getRightChild())
        print(bt.getRootValue())

print("Postorder :")
postorder(bt)
print("----------------------------")