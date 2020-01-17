from Stack import Stack

def baseConverter(number, base):
    s = Stack()
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while number > 0:
        reminder = number% base
        s.push(digits[reminder])
        number = number // base

    result = ""
    while not s.isEmpty():
        result += s.pop()

    return result

print(baseConverter(25,8))
print(baseConverter(256,16))
print(baseConverter(26,26))