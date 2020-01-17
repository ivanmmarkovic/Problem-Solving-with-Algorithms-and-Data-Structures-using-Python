from deque import Deque

def isPalindrome(string: str)->bool:
    d = Deque()
    for character in string:
        d.addRear(character)

    isPalindromeFlag: bool = True

    while d.size() > 1 and isPalindromeFlag:
        if d.removeFront() != d.removeRear():
            isPalindromeFlag = False
        
    return isPalindromeFlag


print(isPalindrome("radar"))
print(isPalindrome("radr"))