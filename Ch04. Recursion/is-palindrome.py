
def isPalindrome(string: str)->bool:
    if len(string) < 2:
        return True
    else:
        if string[0] == string[len(string) - 1]:
            return isPalindrome(string[1: len(string) - 1])
        else:
            return False

print(isPalindrome('kayak'))
print(isPalindrome('aibohphobia'))

# no slicing
def isPalindrome2(string: str, start: int, end: int)->bool:
    if start >= end:
        return True
    else:
        if string[start] == string[end]:
            return isPalindrome2(string, start + 1, end - 1)
        else:
            return False

print(isPalindrome2('kayak', 0, len('kayak') - 1))
print(isPalindrome2('aibohphobia', 0, len('aibohphobia') - 1))

