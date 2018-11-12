
def reverser(string):
    if len(string) == 1:
        return string[0]
    else:
        return reverser(string[1:]) + string[0]


print(reverser("This is a string!"))