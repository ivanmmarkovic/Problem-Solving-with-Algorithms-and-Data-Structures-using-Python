
array = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def selection_sort(nums: list):
    for i in range(0, len(nums), +1):
        min_index: int = i
        for j in range(i + 1, len(nums) - 1, +1):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[min_index], nums[i] = nums[i], nums[min_index]


print(array)
selection_sort(array)
print(array)
