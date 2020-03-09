def fibonacci(n: int, prev: int, curr: int, acc: int):
    if n == 1:
        return prev
    elif n == 2:
        return acc + curr
    else:
        return fibonacci(n - 1, curr, prev + curr, acc + curr)


print(fibonacci(5, 0, 1, 0)) # 7
print(fibonacci(2, 0, 1, 0)) # 1
print(fibonacci(1, 0, 1, 0)) # 0
