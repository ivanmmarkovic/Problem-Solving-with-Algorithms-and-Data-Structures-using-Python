


arr: list = [1, 2, 3]
def sum(arr: list, start: int, end: int)->int:
    if start > end:
        return 0
    if start == end:
        return arr[start]
    else:
        midpoint: int = int(start + (end - start) / 2)
        return sum(alist, start, midpoint - 1) + alist[midpoint] + sum(alist, midpoint + 1, end)
    
        # this works return sum(arr, start, midpoint) + sum(arr, midpoint + 1, end)
        
        # this doesn't return sum(arr, start, midpoint - 1) + sum(arr, midpoint, end)
        # RecursionError: maximum recursion depth exceeded in comparison

print(sum(arr, 0, len(arr) - 1))

