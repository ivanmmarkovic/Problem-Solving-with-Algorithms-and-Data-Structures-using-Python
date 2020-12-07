
def sequential_search(nums: list, target: int) -> bool:
    found: bool = False
    stopped: bool = False
    i: int = 0
    while i < len(nums) and not found and not stopped:
        if nums[i] == target:
            found = True
        else:
            if nums[i] > target:
                stopped = True
            else:
                i += 1
    return found


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(sequential_search(testlist, 3))
print(sequential_search(testlist, 13))
