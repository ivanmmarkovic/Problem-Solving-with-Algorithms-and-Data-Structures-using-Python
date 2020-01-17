from Stack import Stack

def decimalToBinary(number):
    s = Stack()
    while number > 0:
        reminder = number % 2
        s.push(str(reminder))
        number = number // 2
    
    result = ""
    while not s.isEmpty():
        result += s.pop()

    return result

print(decimalToBinary(233))
print(decimalToBinary(233) == '11101001')
    