
def fibonacci(n: int) -> int:

    def fibonacci_helper(n: int, acc: int, prev: int, curr: int) -> int:
        if n == 1:
            return prev
        elif n == 2:
            return acc + curr
        else:
            return fibonacci_helper(n - 1, acc + curr, curr, prev + curr)

    return fibonacci_helper(n, 0, 0, 1)


for i in range(1, 6, +1):
    print("Sum of",i, " fibonacci numbers :", fibonacci(i))





