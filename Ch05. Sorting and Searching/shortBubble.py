alist = [15, 3, 437, 59, 1, 117, 500, 19]
print(alist)

def shortBubble(alist):
    swapped = True
    dec = 1
    while swapped:
        swapped = False
        for i in range(len(alist) - dec):
            print("Comparing ", alist[i], alist[i + 1])
            if alist[i] > alist[i + 1]:
                tmp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = tmp
                swapped = True
        dec += 1
        print("------------------------------------")

    print("##################################")

shortBubble(alist)
print(alist)