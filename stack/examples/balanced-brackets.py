from stack import Stack


def balanced_brackets(string: str) -> bool:
    stack: Stack = Stack()
    for character in string:
        if character in "([{":
            stack.push(character)
        if character in ")]}":
            if stack.is_empty():
                return False
            if "([{".index(stack.peek()) == ")]}".index(character):
                stack.pop()
    return stack.is_empty()


print(balanced_brackets('((()))'))  # True
print(balanced_brackets('(()'))  # False
print(balanced_brackets(']()'))  # False
