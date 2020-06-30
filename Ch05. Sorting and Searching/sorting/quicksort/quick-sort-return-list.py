

arr: list = [54,26,93,17,77,31,44,55,20]

def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    midpoint: int = len(arr) // 2
    leftList: list = []
    rightList: list = []
    for i in range(len(arr)):
        if i != midpoint:
            if arr[i] < arr[midpoint]:
                leftList.append(arr[i])
            else:
                rightList.append(arr[i])
    
    return quick_sort(leftList) + [arr[midpoint]] + quick_sort(rightList)

print(arr)
arr = quick_sort(arr)
print(arr)
