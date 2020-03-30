


arr: list = [1, 2, 3]
def sum(arr: list, start: int, end: int)->int:
    if start > end:
        return 0
    if start == end:
        return arr[start]
    else:
        midpoint: int = int(start + (end - start) / 2)
        return sum(arr, start, midpoint) + sum(arr, midpoint + 1, end)

print(sum(arr, 0, len(arr) - 1))

