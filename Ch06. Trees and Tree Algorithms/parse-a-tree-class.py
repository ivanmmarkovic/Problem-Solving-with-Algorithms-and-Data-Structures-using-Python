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
        elif pattern.match(character):
            currentTree.setRootValue(int(character))
            currentTree = s.pop()
        elif character in "+-*/":
            currentTree.setRootValue(character)
            currentTree.insertRight('')
            s.push(currentTree)
            currentTree = currentTree.getRightChild() 
        elif character == ")":
            currentTree = s.pop()

    return bt


bt = treeParser(string)

def evaluate(bt):
    leftChild = bt.getLeftChild()
    rightChild = bt.getRightChild()
    if leftChild != None and rightChild != None:
        fn = opers[bt.getRootValue()]
        return fn(evaluate(leftChild), evaluate(rightChild))
    else:
        return bt.getRootValue()


print(evaluate(bt))
