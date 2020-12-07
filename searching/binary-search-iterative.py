
def binary_search(nums: list, target: int) -> bool:
    start: int = 0
    end: int = len(nums) - 1
    found: bool = False
    while start <= end and not found:
        midpoint: int = start + (end - start) // 2
        if nums[midpoint] == target:
            found = True
        else:
            if nums[midpoint] > target:
                end = midpoint - 1
            else:
                start = midpoint + 1
    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
