def converter(num: int, base: int) -> str:
    digits = "0123456789ABCDEF"
    if num < base:
        return digits[num]
    else:
        return converter(num // base, base) + digits[num % base]


print(converter(1453, 16)) # 5AD