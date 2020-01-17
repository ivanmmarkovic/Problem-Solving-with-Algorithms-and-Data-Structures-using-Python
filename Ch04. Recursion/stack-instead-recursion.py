from stack import Stack

def converter(number: int, base: int)->str:
    digits = "0123456789ABCDEF"
    stack = Stack()
    while number > base:
        stack.push(digits[number % base])
        number = number // base

    result: str = ""
    while not stack.isEmpty():
        result += stack.pop()
    
    return result


print(converter(1453,16)) # 5AD