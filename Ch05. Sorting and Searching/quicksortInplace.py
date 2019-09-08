import random

def quicksort(alist: list, left:int, right:int):
	if left >= right:
		return
	else:
		#pivot: int = random.randint(left, right)
		pivot: int = left + (right - left) // 2
		pivot_value: int = alist[pivot]
		i: int = left
		j: int = right 
		mid: int = i
		while mid <= j:
			if alist[mid] < pivot_value:
				alist[mid], alist[i] = alist[i], alist[mid]
				i += 1
				mid += 1
			elif alist[mid] > pivot_value:
				alist[mid], alist[j] = alist[j], alist[mid]
				j -= 1 
			else:
				mid += 1
		
		quicksort(alist, left, i - 1)
		quicksort(alist, j + 1, right)

		

alist = [21, 2, 98, 13, 1, 1001, 9, 53, 92]
print(alist)
quicksort(alist, 0, len(alist) - 1)
print(alist)

