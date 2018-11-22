from Dequeue import Dequeue

def isPalindrome(string):
    d = Dequeue()
    for character in string:
        d.addRear(character)

    while d.size() > 1:
        if d.removeFront() != d.removeRear():
            return False

    return True
    
print(isPalindrome("radar"))
print(isPalindrome("radr"))


