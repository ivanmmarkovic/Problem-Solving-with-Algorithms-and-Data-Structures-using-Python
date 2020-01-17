'''
this solution is O(n),
but it requires extra space for 2 lists
'''

def anagramDetection(string1, string2):
    l1 = [0] * 26
    l2 = [0] * 26

    pos1 = 0
    while pos1 < len(string1):
        character = string1[pos1]
        index = ord(character) - ord("a")
        l1[index] = l1[index] + 1
        pos1 += 1

    pos2 = 0
    while pos2 < len(string2):
        character = string2[pos2]
        index = ord(character) - ord("a")
        l2[index] = l2[index] + 1
        pos2 += 1

    pos = 0
    isAnagram = True
    while pos < len(l1) and isAnagram:
        if l1[pos] != l2[pos]:
            isAnagram = False
        else:
            pos += 1

    return isAnagram

print(anagramDetection("python", "typhon"))
print(anagramDetection("baba", "abba"))
print(anagramDetection("babb", "abba"))
