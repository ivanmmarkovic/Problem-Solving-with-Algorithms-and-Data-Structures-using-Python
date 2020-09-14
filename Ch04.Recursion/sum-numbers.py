
numbers: list = [1, 2, 3, 4, 5]

def sum_nums(nums: list) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[0] + sum_nums(nums[1:])

print(sum_nums(numbers))


