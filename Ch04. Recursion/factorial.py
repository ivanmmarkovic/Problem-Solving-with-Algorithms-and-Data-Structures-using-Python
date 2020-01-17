
def factorial(number: int)->int:
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(3))
print(factorial(5))