
def printMove(start: str, end: str):
    print("Moving from", start, "to", end)

def towers(number: int, start: str, spare: str, end: str):
    if number == 1:
        printMove(start, end)
    else:
        towers(number - 1, start, end, spare)
        towers(1, start, spare, end)
        towers(number - 1, spare, start, end)

towers(3, "start", "spare", "end")