
from stack import Stack
import operator
import re
from treenode import TreeNode

opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

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


def preorder(node: TreeNode, space: int = 0):
    if node is not None:
        print(" " * space, node.key)
        preorder(node.get_left_child(), space + 2)
        preorder(node.get_right_child(), space + 2)


preorder(tree_node)

