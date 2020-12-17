class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert_root_value(self, key=None):
        self.key = key

    def insert_left(self, key=None):
        self.left = TreeNode(key, self.left)

    def insert_right(self, key=None):
        self.right = TreeNode(key, None, self.right)

    def get_root_value(self):
        return self.key

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right


# Write a function build_tree that returns a tree
# using the list of lists functions that look like this :
#      a
#    /   \
#   b     c
#    \   / \
#     d e   f


def build_tree() -> TreeNode:
    tree: TreeNode = TreeNode('a')
    tree.insert_right('f')
    tree.insert_right('c')
    tree.get_right_child().insert_left('e')

    tree.insert_left('b')
    tree.get_left_child().insert_right('d')

    return tree


binary_tree: TreeNode = build_tree()


def print_tree(tree: TreeNode):
    if tree is not None:
        print_tree(tree.get_left_child())
        print(tree.key, end=", ")
        print_tree(tree.get_right_child())


print_tree(binary_tree)

# ['a', 
#     ['b',
#         [],
#         ['d', [], []]],
#     ['c',
#         ['e', [], []],
#         ['f', [], []]
#     ]
# ]
