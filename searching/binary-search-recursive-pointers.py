
def binary_search(nums: list, target: int) -> bool:

    def binary_search_helper(numbers: list, element, start: int, end: int) -> bool:
        if start > end:
            return False
        else:
            midpoint: int = start + (end - start) // 2
            if nums[midpoint] == element:
                return True
            else:
                if nums[midpoint] > element:
                    return binary_search_helper(numbers, element, start, midpoint - 1)
                else:
                    return binary_search_helper(numbers, element, midpoint + 1, end)

    return binary_search_helper(nums, target, 0, len(nums) - 1)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
