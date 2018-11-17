from Stack import Stack

import operator
opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

import re
pattern = re.compile("[0-9]")

def createBinaryTree(root):
    return [root, [], []]

def setRootvalue(bt, key):
    bt[0] = key

def getRootValue(bt):
    return bt[0]

def insertLeft(bt, key):
    t = bt.pop(1)
    bt.insert(1, [key, t, []])

def insertRight(bt, key):
    t = bt.pop(2)
    bt.insert(2, [key, [], t])

def getLeftChild(bt):
    return bt[1]

def getRightChild(bt):
    return bt[2]

string = "( ( 10 + 5 ) * 3 )"
def treeParser(string):
    string = string.split()
    s = Stack()
    bt = createBinaryTree('')
    s.push(bt)
    currentTree = bt 

    for character in string:
        if character == "(":
            insertLeft(currentTree, '')
            s.push(currentTree)
            currentTree = getLeftChild(currentTree)
        elif pattern.match(character):
            setRootvalue(currentTree, int(character))
            currentTree = s.pop()
        elif character in "+-*/":
            setRootvalue(currentTree, character)
            insertRight(currentTree, '')
            s.push(currentTree)
            currentTree = getRightChild(currentTree) 
        elif character == ")":
            currentTree = s.pop()

    return bt


bt = treeParser(string)

def evaluate(bt):
    leftChild = getLeftChild(bt)
    rightChild = getRightChild(bt)
    if leftChild != [] and rightChild != []:
        fn = opers[getRootValue(bt)]
        return fn(evaluate(leftChild), evaluate(rightChild))
    else:
        return getRootValue(bt)


print(evaluate(bt))
