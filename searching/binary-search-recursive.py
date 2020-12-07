# slicing a list is O(k)
# better is recursive solution with pointers
def binary_search(nums: list, target: int) -> bool:
    if len(nums) == 0:
        return False
    else:
        midpoint: int = len(nums) // 2
        if nums[midpoint] == target:
            return True
        else:
            if nums[midpoint] > target:
                return binary_search(nums[0: midpoint], target)
            else:
                return binary_search(nums[midpoint + 1:], target)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
