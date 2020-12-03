def fibonacci(n: int) -> int:
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    prev: int = 0
    curr: int = 1
    for _ in range(n - 2):
        prev, curr = curr, prev + curr
    return curr


for i in range(6):
    print(fibonacci(i))
