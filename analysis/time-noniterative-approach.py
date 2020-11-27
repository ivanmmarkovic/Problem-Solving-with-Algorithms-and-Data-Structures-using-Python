import time


def sum_nums(n: int) -> int:
    start = time.time()
    total: int = n * (n + 1) / 2
    end = time.time()
    print("For ", n, " numbers time is", end - start)
    return total


print(sum_nums(100))
print(sum_nums(50000000))

