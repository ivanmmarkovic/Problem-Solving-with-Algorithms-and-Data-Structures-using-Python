array = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def quick_sort(nums: list, i: int, j: int):
    if i < j:
        left: int = i
        right: int = j
        pointer: int = left
        pivot_index: int = left + (right - left) // 2
        pivot_value: int = nums[pivot_index]

        while pointer <= right:
            if nums[pointer] < pivot_value:
                nums[left], nums[pointer] = nums[pointer], nums[left]
                left += 1
                pointer += 1
            elif nums[pointer] > pivot_value:
                nums[pointer], nums[right] = nums[right], nums[pointer]
                right -= 1
            else:
                pointer += 1

        quick_sort(nums, i, left)
        if pointer > left:
            quick_sort(nums, pointer, j)
        else:
            quick_sort(nums, pointer + 1, j)


print(array)
quick_sort(array, 0, len(array) - 1)
print(array)
