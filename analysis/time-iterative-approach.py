import time


def sum_nums(n: int) -> int:
    start = time.time()
    total: int = 0
    for i in range(n + 1):
        total += i
    end = time.time()
    print("For ", n, " numbers time is", end - start)
    return total


print(sum_nums(100))
print(sum_nums(50000000))

