array = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def quick_sort(nums: list) -> list:
    if len(nums) < 2:
        return nums
    pivot_index: int = len(nums) // 2
    pivot_value: int = nums[pivot_index]

    left: list = []
    right: list = []
    for i in range(len(nums)):
        if i != pivot_index:
            if nums[i] < pivot_value:
                left.append(nums[i])
            else:
                right.append(nums[i])
    return quick_sort(left) + [pivot_value] + quick_sort(right)


print(array)
array_sorted: list = quick_sort(array)
print(array_sorted)
