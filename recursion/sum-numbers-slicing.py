numbers: list = [1, 2, 3, 4, 5]


# slicing is O(k), better is solution with pointer
def sum_numbers(nums: list) -> int:
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sum_numbers(nums[1:])


print(sum_numbers(numbers))
