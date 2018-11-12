
def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(5)) # 120
print(factorial(1)) # 1
print(factorial(-1)) # 1
