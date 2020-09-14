from stack import Stack

def converter(number: int, base: int)->str:
    digits = "0123456789ABCDEF"
    stack: Stack = Stack()

    while number > 0:
        stack.push(digits[number % base])
        number = number // base

    result: str = ""
    while not stack.is_empty():
        result += stack.pop()

    return result



print(converter(1453, 16)) # 5AD