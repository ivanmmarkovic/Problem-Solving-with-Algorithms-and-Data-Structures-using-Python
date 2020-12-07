
array = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def short_bubble(nums: list):
    swapped: bool = True
    dec: int = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - dec):
            if nums[i] > nums[i + 1]:
                nums[i + 1], nums[i] = nums[i], nums[i + 1]
                swapped = True
        dec += 1


print(array)
short_bubble(array)
print(array)
