def printMove(start, end):
    print("Moving from " + start + " to " + end)


def towers(number, start, spare, end):
    if number == 1:
        printMove(start, end)
    else:
        towers(number - 1, start, end, spare)
        towers(1, start, spare, end)
        towers(number - 1, spare, start, end)


towers(7, "start", "spare", "end")