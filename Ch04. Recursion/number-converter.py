
def converter(number: int, base: int)->str:
    digits = "0123456789ABCDEF"
    if number < base:
        return digits[number]
    else:
        return converter(number // base, base) + digits[number % base]

print(converter(1453, 16)) # 5AD
