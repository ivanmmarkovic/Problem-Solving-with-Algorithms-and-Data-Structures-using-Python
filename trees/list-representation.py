
def create_tree(root=None) -> list:
    return [None, [], []]


def insert_root(tree: list, root=None):
    tree[0] = root


def insert_left(tree: list, root=None):
    left_child: list = tree.pop(1)
    tree.insert(1, [root, left_child, []])


def insert_right(tree: list, root=None):
    right_child: list = tree.pop(2)
    tree.insert(2, [root, [], right_child])


def get_root(tree: list):
    return tree[0]


def get_left_child(tree: list) -> list:
    return tree[1]


def get_right_child(tree: list) -> list:
    return tree[2]


# Write a function build_tree that returns a tree
# using the list of lists functions that look like this :
#      a
#    /   \
#   b     c
#    \   / \
#     d e   f


def build_tree() -> list:
    tree: list = create_tree()
    insert_root(tree, 'a')

    insert_right(tree, 'f')
    insert_right(tree, 'c')
    insert_left(get_right_child(tree), 'e')

    insert_left(tree, 'b')
    insert_right(get_left_child(tree), 'd')

    return tree


binary_tree: list = build_tree()
print(binary_tree)


# ['a',
#     ['b',
#         [],
#         ['d', [], []]],
#     ['c',
#         ['e', [], []],
#         ['f', [], []]
#     ]
# ]
