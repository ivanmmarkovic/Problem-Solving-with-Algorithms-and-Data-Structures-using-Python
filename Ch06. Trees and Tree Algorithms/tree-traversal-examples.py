from Stack import Stack
from BinaryTree import BinaryTree

import operator
opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

import re
pattern = re.compile("[0-9]")

string = "( ( 10 + 5 ) * 3 )"
def treeParser(string):
    string = string.split()
    s = Stack()
    bt = BinaryTree('')
    s.push(bt)
    currentTree = bt

    for character in string:
        if character == "(":
            currentTree.insertLeft('')
            s.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif character in "+-*/":
            currentTree.setRootValue(character)
            currentTree.insertRight('')
            s.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif pattern.match(character):
            currentTree.setRootValue(int(character))
            currentTree = s.pop()
        elif character == ")":
            currentTree = s.pop()

    return bt

bt = treeParser(string)

# postorder example
def evaluate(bt):
    leftChild = None
    rightChild = None
    if bt:
        leftChild = evaluate(bt.getLeftChild())
        rightChild = evaluate(bt.getRightChild())
        if leftChild != None and rightChild != None:
            fn = opers[bt.getRootValue()]
            return fn(leftChild, rightChild)
        else:
            return bt.getRootValue()

print(evaluate(bt))

# inorder example
def inorder(bt):
    result = ""
    if bt and bt.getLeftChild() != None and bt.getRightChild() != None:
        result += "(" + inorder(bt.getLeftChild())
        result += str(bt.getRootValue())
        result += inorder(bt.getRightChild()) + ")"
    elif bt:
        result += str(bt.getRootValue())
    return result

print(inorder(bt))

# same as method above
def inorderv02(bt):
    result = ""
    if bt:
        if bt.leftChild:
            result += "(" + inorderv02(bt.leftChild)
        result += str(bt.getRootValue())
        if bt.rightChild:
            result += inorderv02(bt.rightChild) + ")"
    return result
    

print(inorderv02(bt))
                
