def fibonacci(n: int) -> int:

    def fibonacci_helper(num: int, acc: int = 0, prev: int = 0, curr: int = 1):
        if num <= 1:
            return prev
        elif num == 2:
            return acc + curr
        else:
            return fibonacci_helper(num - 1, acc + curr, curr, prev + curr)

    return fibonacci_helper(n)


for i in range(6):
    print(fibonacci(i))
