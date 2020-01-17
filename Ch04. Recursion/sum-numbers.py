
def sum(numbers: list)->int:
    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return numbers[0]
    else:
        return numbers[0] + sum(numbers[1:])


print(sum([]))
print(sum([1]))
print(sum([1, 2]))