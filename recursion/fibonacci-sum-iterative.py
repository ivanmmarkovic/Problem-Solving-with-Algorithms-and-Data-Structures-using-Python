def fibonacci(n: int) -> int:
    
    if n <= 1:
        return 0
    elif n == 2:
        return 1

    acc: int = 0
    prev: int = 0
    curr: int = 1
    for _ in range(n - 1):
        acc += curr
        prev, curr = curr, prev + curr

    return acc


for i in range(6):
    print(f'Fibonacci {i} is : {fibonacci(i)}')
