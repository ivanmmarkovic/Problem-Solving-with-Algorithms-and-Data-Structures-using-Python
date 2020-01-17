from Stack import Stack

def parChecker(string):
    s = Stack()
    for character in string:
        if character == "(":
            s.push(character)
        elif character in ")":
            s.pop()
    return s.isEmpty()

print(parChecker('((()))'))
print(parChecker('(()'))
    