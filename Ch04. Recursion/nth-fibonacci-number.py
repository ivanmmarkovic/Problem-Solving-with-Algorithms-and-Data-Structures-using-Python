def fibonacci(number, prev, curr):
    if number == 1:
        return prev
    elif number == 2:
        return curr
    else:
        return fibonacci(number - 1, curr, prev + curr)


print(fibonacci(5, 0, 1))