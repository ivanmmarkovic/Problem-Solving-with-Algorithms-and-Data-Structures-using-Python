
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


def inorder(node: TreeNode) -> str:
    ret_value: str = ""
    if node.get_left_child() is not None:
        ret_value += "(" + inorder(node.get_left_child())
    ret_value += str(node.get_root_value())
    if node.get_right_child() is not None:
        ret_value += inorder(node.get_right_child()) + ")"

    return ret_value


print(inorder(tree_node))  # ((10+5)*3)

