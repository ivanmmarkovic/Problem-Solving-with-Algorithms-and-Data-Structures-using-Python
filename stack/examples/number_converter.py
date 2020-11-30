from stack import Stack


def base_converter(num, base) -> str:
    digits = "0123456789ABCDEF"
    stack: Stack = Stack()
    while num > 0:
        stack.push(digits[num % base])
        num = num // base

    result: str = ""
    while not stack.is_empty():
        result += stack.pop()

    return result


print(base_converter(25, 8))  # 31
print(base_converter(256, 16))  # 100
print(base_converter(26, 26))  # 10
