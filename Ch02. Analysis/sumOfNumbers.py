
# iterative solution
def sumOfNumbersIterative(number):
    sum = 0
    for item in range(number + 1):
        sum += item
    return sum


print(sumOfNumbersIterative(5))

# non-iterative solution
def sumOfNumbersNonIterative(number):
    return number * (number + 1) / 2

print(sumOfNumbersNonIterative(5))

