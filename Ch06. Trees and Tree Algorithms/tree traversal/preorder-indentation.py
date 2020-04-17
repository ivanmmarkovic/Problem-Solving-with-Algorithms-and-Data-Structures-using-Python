from tree import TreeNode
from stack import Stack

import operator

opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

import re
pattern = re.compile("[0-9]")

string = "( ( 10 + 5 ) * 3 )"

def treeParser(string: str)->TreeNode:
    string = string.split()
    tree = TreeNode()
    stack: Stack = Stack()
    currentTree: TreeNode = tree
    stack.push(tree)
    for item in string:
        if item == "(":
            currentTree.insertLeft()
            stack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif item == ")":
            currentTree = stack.pop()
        elif item in "+-*/":
            currentTree.setRootValue(item)
            currentTree.insertRight()
            stack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif pattern.match(item):
            currentTree.setRootValue(int(item))
            currentTree = stack.pop()
        else:
            raise ValueError()
    
    return tree

tree: TreeNode = treeParser(string)

def prettyPrint(bt: TreeNode, indent: int):
    print(indent * " ", bt.key)
    if bt.leftChild is not None:
        prettyPrint(bt.leftChild, indent + 2)
    if bt.rightChild is not None:
        prettyPrint(bt.rightChild, indent + 2)

prettyPrint(bt, 0)
