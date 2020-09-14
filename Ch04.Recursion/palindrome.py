

def palindrome1(string: str) -> bool:

    def palindrome_helper(string: str, start: int, end: int) -> bool:
        if start >= end:
            return True
        else:
            if string[start] != string[end]:
                return False
            else:
                return palindrome_helper(string, start + 1, end - 1)

    return palindrome_helper(string, 0, len(string) - 1)


str1: str = "kayak"
str2: str = "aibohphobia"

print(palindrome1(str1))
print(palindrome1(str2))

def palindrome2(string: str) -> bool:
    if len(string) <= 1:
        return True
    else:
        if string[0] != string[len(string) - 1]:
            return False
        else:
            return palindrome2(string[1: len(string) - 1])


print(palindrome2(str1))
print(palindrome2(str2))