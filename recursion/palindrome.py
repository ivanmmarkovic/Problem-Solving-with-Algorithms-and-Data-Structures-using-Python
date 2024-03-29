def palindrome_checker(string: str) -> bool:

    def palindrome_helper(s: str, start: int, end: int) -> bool:
        if start >= end:
            return True
        else:
            if s[start] == s[end]:
                return palindrome_helper(s, start + 1, end - 1)
            else:
                return False

    return palindrome_helper(string, 0, len(string) - 1)


str1: str = "kayak"
str2: str = "aibohphobia"

print(palindrome_checker(str1))
print(palindrome_checker(str2))


def palindrome_checker_iterative(string:str) -> bool:
    is_palindrome: bool = True
    start = 0
    end = len(string) - 1

    while start < end and is_palindrome:
        if string[start] != string[end]:
            is_palindrome = False
        start += 1
        end -= 1
    
    return is_palindrome


print(palindrome_checker_iterative(str1))
print(palindrome_checker_iterative(str2))


def palindrome_checker_slicing(string: str) -> bool:
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome_checker_slicing(string[1: -1])
        else:
            return False


print(palindrome_checker_slicing(str1))
print(palindrome_checker_slicing(str2))
