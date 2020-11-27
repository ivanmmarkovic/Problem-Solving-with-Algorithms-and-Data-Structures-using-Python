
# O(nlogn)
def anagrams(string1: str, string2: str) -> bool:

    if len(string1) != len(string2):
        return False

    is_anagram: bool = True
    list1: list = list(string1)
    list2: list = list(string2)
    list1.sort() # sorting is O(nlogn)
    list2.sort() # sorting is O(nlogn)
    pos: int = 0
    # loop is O(n)
    while pos < len(list1) and is_anagram:
        if list1[pos] != list2[pos]:
            is_anagram = False
        else:
            pos += 1

    return is_anagram


print(anagrams("python", "typhon"))
print(anagrams("abba", "baba"))
print(anagrams("abba", "abbb"))

