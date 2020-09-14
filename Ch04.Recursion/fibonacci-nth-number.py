
def fibonacci(n: int) -> int:

    def fibonacci_helper(n: int, prev: int, curr: int) -> int:
        if n == 1:
            return prev
        elif n == 2:
            return curr
        else:
            return fibonacci_helper(n - 1, curr, prev + curr)

    return fibonacci_helper(n, 0, 1)


for i in range(1, 6, +1):
    print(i, ":", fibonacci(i))





