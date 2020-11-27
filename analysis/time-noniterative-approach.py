import time


def sum_nums(n: int) -> int:
    start = time.time()
    total: int = n * (n + 1) / 2
    end = time.time()
    print("For ", n, " numbers time is", end - start)
    return total


nums: list = [100, 10000, 100000, 1000000]
for n in nums:
    print(sum_nums(n))

