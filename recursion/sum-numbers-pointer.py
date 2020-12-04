numbers: list = [1, 2, 3, 4, 5]


# O(n) time, O(n) space
def sum_numbers(nums: list) -> int:

    def helper(elements: list, end: int) -> int:
        if end < 0:
            return 0
        else:
            return elements[end] + helper(elements, end - 1)

    return helper(nums, len(nums) - 1)


print(sum_numbers(numbers))
