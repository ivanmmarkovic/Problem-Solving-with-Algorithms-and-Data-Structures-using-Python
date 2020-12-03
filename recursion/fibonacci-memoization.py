
nums: dict = {}


def fibonacci(n: int) -> int:
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        if n in nums:
            return nums[n]
        nums[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return nums[n]


for i in range(6):
    print(fibonacci(i))
