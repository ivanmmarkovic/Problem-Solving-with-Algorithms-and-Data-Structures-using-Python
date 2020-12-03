def factorial_rec(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * factorial_rec(n - 1)


def factorial_it(n: int) -> int:
    if n <= 1:
        return 1
    result: int = 1
    while n > 1:
        result *= n
        n -= 1
    return result
