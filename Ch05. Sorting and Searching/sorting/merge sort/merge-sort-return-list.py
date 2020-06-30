

arr: list = [54,26,93,17,77,31,44,55,20]

def merge_sort(arr: list):
    result: list = helper(arr, 0, len(arr) - 1)
    for i in range(len(arr)):
        arr[i] = result[i]
    
def helper(arr: list, start: int, end: int) -> list:
    if start > end:
        return []
    elif start == end:
        return [arr[start]]
    else:
        midpoint: int = start + (end - start) // 2
        leftList = helper(arr, start, midpoint)
        rightList = helper(arr, midpoint + 1, end)
        return mergelists(leftList, rightList)
        

def mergelists(leftList: list, rightList: list) -> list:
        arr: list = [None] * (len(leftList) + len(rightList))
        i = j = k = 0
        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                arr[k] = leftList[i]
                i += 1
            else:
                arr[k] = rightList[j]
                j += 1
            k += 1

        while i < len(leftList):
            arr[k] = leftList[i]
            i += 1
            k += 1

        while j < len(rightList):
            arr[k] = rightList[j]
            j += 1
            k += 1
        
        return arr

print(arr)
merge_sort(arr)
print(arr)
