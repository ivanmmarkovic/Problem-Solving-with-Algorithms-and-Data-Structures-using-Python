nums: list = [1, 2, 3, 4, 5]


def reverse_rec(elements: list):

    def reverse_list_helper(values: list, start: int, end: int):
        if start < end:
            values[start], values[end] = values[end], values[start]
            reverse_list_helper(values, start + 1, end - 1)

    reverse_list_helper(elements, 0, len(elements) - 1)


print(nums)
reverse_rec(nums)
print(nums)


def reverse_iterative(elements: list):
    start: int = 0
    end: int = len(elements) - 1
    while start < end:
        elements[start], elements[end] = elements[end], elements[start]
        start += 1
        end -= 1


reverse_iterative(nums)
print(nums)
