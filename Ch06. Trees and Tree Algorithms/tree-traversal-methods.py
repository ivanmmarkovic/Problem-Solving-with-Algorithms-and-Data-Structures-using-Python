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

bt.preorder()
print("#################")
bt.inorder()
print("#################")
bt.postorder()