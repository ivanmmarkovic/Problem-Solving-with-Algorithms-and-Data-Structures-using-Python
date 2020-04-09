
# reverse a string
string: str = "This string will be reversed"

# solution 1
def reverser1(string: str)->str:
    if len(string) == 0:
        return ""
    elif len(string) == 1:
        return string[0]
    else:
        return string[len(string) - 1] + reverser1(string[0:len(string) - 1])

print(reverser1(string))

# solution 2
def reverser2(string: str)->str:
    if len(string) == 0:
        return ""
    elif len(string) == 1:
        return string[0]
    else:
        return reverser2(string[1:]) + string[0]

print(reverser2(string))

# solution 3
def reverser3(string: str, end: int)->str:
    if end < 0: # if len(string) == 0:
        return ""
    elif end == 0:
        return string[end]
    else:
        return string[end] + reverser3(string, end - 1)

print(reverser3(string, len(string) - 1))
