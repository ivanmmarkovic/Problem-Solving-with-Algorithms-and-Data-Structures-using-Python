from stack import Stack


def converter(num: int, base: int) -> str:
    digits = "0123456789ABCDEF"
    stack: Stack = Stack()
    while num > 0:
        stack.push(digits[num % base])
        num = num // base
    result: str = ""
    while not stack.is_empty():
        result += stack.pop()
    return result


'''
digits = "0123456789ABCDEF"
def converter(num: int, base: int) -> str:

    r:str = ''
    while num >  0:
        r = digits[num % base] + r
        num = num // base       
    
    return r
'''

print(converter(1453, 16)) # 5AD
