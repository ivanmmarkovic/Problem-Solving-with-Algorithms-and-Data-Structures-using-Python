from Stack import Stack

def reverser(string):
    s = Stack()
    for character in string:
        s.push(character)
    
    result = ""
    while not s.isEmpty():
        result += s.pop()

    return result

print(reverser("This is my string."))