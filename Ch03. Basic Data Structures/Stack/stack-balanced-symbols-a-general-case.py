from Stack import Stack

def balancedSymbols(string):
    s = Stack()
    for character in string:
        if character in "([{":
            s.push(character)
        elif character in ")]}":
            if "([{".index(s.peek()) == ")]}".index(character):
                s.pop()
    return s.isEmpty()

print(balancedSymbols('{{([][])}()}'))
print(balancedSymbols('[{()]'))
    