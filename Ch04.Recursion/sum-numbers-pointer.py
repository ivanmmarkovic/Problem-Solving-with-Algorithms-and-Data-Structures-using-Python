
numbers: list = [1, 2, 3, 4, 5]

def sum_nums(nums: list) -> int:

    def sum_nums_helper(nums: list, end: int) -> int:
        if end < 0:
            return 0
        elif end == 0:
            return nums[0]
        else:
            return nums[end] + sum_nums_helper(nums, end - 1)

    return sum_nums_helper(nums, len(nums) - 1)

print(sum_nums(numbers))
