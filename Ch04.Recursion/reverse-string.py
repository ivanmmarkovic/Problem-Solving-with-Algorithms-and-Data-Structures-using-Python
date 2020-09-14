
# reverse a string
string: str = "This string will be reversed"

def reverser1(string: str) -> str:
    if len(string) == 0:
        return ""
    else:
        return reverser1(string[1:]) + string[0]

print(reverser1(string))

def reverser2(string: str) -> str:
    if len(string) == 0:
        return ""
    else:
        return string[len(string) - 1] + reverser2(string[0:len(string) - 1])

print(reverser2(string))


def reverser3(string: str) -> str:
    def helper(string: str, end: int) -> str:
        if end < 0:
            return ""
        else:
            return string[end] + helper(string, end - 1)
    
    return helper(string, len(string) - 1)

print(reverser3(string))