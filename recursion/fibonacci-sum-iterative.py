def fibonaci(n: int):
    
    if n == 1:
        return 0
    if n == 2:
        return 1

    prev: int = 0
    curr: int = 1
    acc: int = 1

    for _ in range(n - 2):
        prev,curr = curr, prev + curr
        acc += curr


    return acc


for i in range(6):
    print(f'Fibonacci {i} is : {fibonacci(i)}')
