
memo: dict = {}

def fibonacci(num: int) -> int:
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        if num in memo:
            return memo[num]
        memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return memo[num]


for i in range(1, 6, +1):
    print(i, " : ", fibonacci(i))

