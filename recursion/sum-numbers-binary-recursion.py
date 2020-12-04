numbers: list = [1, 2, 3, 4, 5]


# O(n) time, O(logn) space
def sum_numbers(nums: list) -> int:

    def helper(elements: list, start: int, end: int) -> int:
        if start > end:
            return 0
        else:
            index: int = start + (end - start) // 2
            return helper(elements, start, index - 1) + elements[index] + helper(elements, index + 1, end)

    return helper(nums, 0, len(nums) - 1)


print(sum_numbers(numbers))
