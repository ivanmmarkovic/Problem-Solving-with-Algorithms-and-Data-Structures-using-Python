import random

alist = [21, 2, 98, 13, 1, 1001, 9, 53, 92]

def quicksort(arr: list, start: int, end: int):
    if start < end:
        left: int = start
        right: int = end
        pointer: int = left

		#pivotIndex: int = random.randint(left, right)
        pivotIndex: int = left + (right - left) // 2
        pivotValue: int = arr[pivotIndex]

        while pointer <= right:
            if arr[pointer] < pivotValue:
                arr[left], arr[pointer] = arr[pointer], arr[left]
                left += 1
                pointer += 1
            elif arr[pointer] > pivotValue:
                arr[right], arr[pointer] = arr[pointer], arr[right]
                right -= 1
            else:
                pointer += 1

        quicksort(arr, start, left)
        if(right > left):
            quicksort(arr, right, end)
        else:
            quicksort(arr, left + 1, end)

print(alist)
quicksort(alist, 0, len(alist) - 1)
print(alist)
