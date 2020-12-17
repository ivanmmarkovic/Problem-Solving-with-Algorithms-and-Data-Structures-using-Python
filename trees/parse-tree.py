
from stack import Stack
import operator

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


opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

import re
pattern = re.compile("[0-9]")

string = "( ( 10 + 5 ) * 3 )"


def tree_parser(s: str) -> TreeNode:
    arr: list = s.split()
    stack: Stack = Stack()
    node: TreeNode = TreeNode()
    current_node: TreeNode = node
    stack.push(node)
    for e in arr:
        if e == "(":
            current_node.insert_left()
            stack.push(current_node)
            current_node = current_node.get_left_child()
        elif e in "+-*/":
            current_node.insert_root_value(e)
            current_node.insert_right()
            stack.push(current_node)
            current_node = current_node.get_right_child()
        elif pattern.match(e):
            current_node.insert_root_value(int(e))
            current_node = stack.pop()
        elif e == ")":
            current_node = stack.pop()
        else:
            raise Exception()
    return node


tree_node: TreeNode = tree_parser(string)


def evaluate(node: TreeNode) -> int:
    if node.get_left_child() is not None and node.get_right_child() is not None:
        f = opers[node.get_root_value()]
        return f(evaluate(node.get_left_child()), evaluate(node.get_right_child()))
    else:
        return node.get_root_value()


print(evaluate(tree_node)) # 45
