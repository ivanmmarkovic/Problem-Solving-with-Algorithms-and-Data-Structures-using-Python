

def palindromeChecker(string):
    if len(string) < 2:
        return True
    else:
        if string[0] == string[len(string) - 1]:
            return palindromeChecker(string[1 : len(string) - 1]) 
        else:
            return False

print(palindromeChecker("kayak")) # True
print(palindromeChecker("kayyak")) # True
print(palindromeChecker("kayxak")) # False
print(palindromeChecker("aibohphobia")) # True
