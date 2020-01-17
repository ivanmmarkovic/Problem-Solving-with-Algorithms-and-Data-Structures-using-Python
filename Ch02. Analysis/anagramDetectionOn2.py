
# loop inside loop - O(n2)

def anagramDetection(string1, string2):
    l2 = list(string2)
    isAnagram = True
    pos1 = 0
    while pos1 < len(string1) and isAnagram:
        character = string1[pos1]

        characterFound = False
        pos2 = 0
        while pos2 < len(l2) and not characterFound:
            if character == l2[pos2]:
                l2[pos2] = None
                characterFound = True
            else:
                pos2 += 1

        if not characterFound:
            isAnagram = False
        else:
            pos1 += 1

    return isAnagram

print(anagramDetection("python", "typhon"))
print(anagramDetection("baba", "abba"))
print(anagramDetection("babb", "abba"))
