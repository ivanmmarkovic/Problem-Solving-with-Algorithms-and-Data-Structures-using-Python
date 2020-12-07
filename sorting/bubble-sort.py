
array = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def bubble_sort(nums: list):
    for i in range(len(nums)):
        for j in range(len(nums) - 1, i, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]


print(array)
bubble_sort(array)
print(array)
