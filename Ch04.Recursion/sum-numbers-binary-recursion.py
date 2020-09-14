
numbers: list = [1, 2, 3, 4, 5]

def sum_nums(nums: list) -> int:
    
    def sum_nums_helper(nums: list, start: int, end: int) -> int:
        if start > end:
            return 0
        else:
            midpoint: int = start + (end - start) // 2
            return sum_nums_helper(nums, start, midpoint - 1) + nums[midpoint] + sum_nums_helper(nums, midpoint + 1, end)

    return sum_nums_helper(nums, 0, len(nums) - 1)
        

print(sum_nums(numbers))
