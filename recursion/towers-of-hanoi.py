def print_move(start: str, end: str):
    print("Moving from", start, "to", end)


def towers(number: int, start: str, spare: str, end: str):
    if number == 1:
        print_move(start, end)
    else:
        towers(number - 1, start, end, spare)
        towers(1, start, spare, end)
        towers(number - 1, spare, start, end)


towers(3, "start", "spare", "end")
