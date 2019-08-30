





def sum(alist: list, pointer: int)->int:
    if pointer == 0:
        return alist[pointer]
    else:
        return alist[pointer] + sum2(alist, pointer - 1)



print(sum(alist, len(alist) - 1))