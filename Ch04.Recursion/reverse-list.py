

nums: list = [1, 2, 3, 4, 5]

def reverse(nums: list):

    def helper(nums: list, start: int, end: int):
        if start < end:
            nums[start], nums[end] = nums[end], nums[start]
            helper(nums, start + 1, end - 1)

    helper(nums, 0, len(nums) - 1)

print(nums)
reverse(nums)
print(nums)
