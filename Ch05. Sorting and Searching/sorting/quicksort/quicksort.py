
alist: list = [54,26,93,17,77,31,44,55,20]

def quicksort(alist: list, left: int, right: int):
    if left < right:
        start: int = left
        end: int = right
        pointer: int = start

        midpoint: int = start + (end - start) // 2
        refValue: int = alist[midpoint]

        while pointer <= end:
            if alist[pointer] < refValue:
                alist[start], alist[pointer] = alist[pointer], alist[start]
                start += 1
                pointer += 1
            elif alist[pointer] > refValue:
                alist[pointer], alist[end] = alist[end], alist[pointer]
                end -= 1
            else:
                pointer += 1

        quicksort(alist, left, start)
        if pointer > start:
            quicksort(alist, pointer, right)
        else:
            quicksort(alist, start +1, right)

print(alist)
quicksort(alist, 0, len(alist) - 1)
print(alist)
