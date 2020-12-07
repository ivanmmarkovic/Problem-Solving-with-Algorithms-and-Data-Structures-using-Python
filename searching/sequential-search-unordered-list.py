
def sequential_search(nums: list, target: int) -> bool:
    i: int = 0
    found: bool = False
    while i < len(nums) and not found:
        if nums[i] == target:
            found = True
        else:
            i += 1
    return found


testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(testlist, 3))
print(sequential_search(testlist, 13))
