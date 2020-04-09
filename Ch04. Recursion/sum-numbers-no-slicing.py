

def sum(numbers: list, end: int)->int:
    if end < 0: # empty list -> len(alist) == 0
        return 0
    elif end == 0:
        return numbers[end]
    else:
        return numbers[end] + sum(numbers, end - 1)


numbers1: list = []
numbers2: list = [1]
numbers3: list = [1, 2, 3]

print(sum(numbers1, len(numbers1) - 1))
print(sum(numbers2, len(numbers2) - 1))
print(sum(numbers3, len(numbers3) - 1))
