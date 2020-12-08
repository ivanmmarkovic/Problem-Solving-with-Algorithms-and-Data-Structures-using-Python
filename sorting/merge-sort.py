
array = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def merge_sort(nums: list):
    if len(nums) < 2:
        return
    midpoint: int = len(nums) // 2
    left: list = nums[0:midpoint]
    right: list = nums[midpoint:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1


print(array)
merge_sort(array)
print(array)