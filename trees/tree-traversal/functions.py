from treenode import TreeNode

node: TreeNode = TreeNode('a')
node.insert_left('b')
node.insert_left('c')
node.get_left_child().insert_left('f')

node.insert_right('k')
node.insert_right('j')

print("\nInorder")
node.inorder()
print("\nPreorder")
node.preorder()
print("\nPostorder")
node.postorder()

# functions for tree traversal


def inorder(tree: TreeNode):
    if tree is not None:
        inorder(tree.left)
        print(tree.key, end=", ")
        inorder(tree.right)


def preorder(tree: TreeNode):
    if tree is not None:
        print(tree.key, end=", ")
        preorder(tree.left)
        preorder(tree.right)


def postorder(tree: TreeNode):
    if tree is not None:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.key, end=", ")


print("\nInorder")
inorder(node)
print("\nPreorder")
preorder(node)
print("\nPostorder")
postorder(node)
