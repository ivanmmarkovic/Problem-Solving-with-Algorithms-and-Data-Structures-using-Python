'''
you might think that this algorithm is O(n) but,
sorting is dominant part of algorithm and
sorting is typically either O(n2) or O(nlogn)
'''


def anagramDetection(string1, string2):
    l1 = list(string1)
    l2 = list(string2)

    l1.sort()
    l2.sort()

    isAnagram = True
    pos = 0
    while pos < len(l1) and isAnagram:
        if l1[pos] == l2[pos]:
            pos += 1
        else:
            isAnagram = False


    return isAnagram

print(anagramDetection("python", "typhon"))
print(anagramDetection("baba", "abba"))
print(anagramDetection("babb", "abba"))
