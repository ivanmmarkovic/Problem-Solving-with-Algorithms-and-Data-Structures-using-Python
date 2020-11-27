
# O(n)
def anagrams(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    is_anagram: bool = True
    list1: list = [0] * 26
    list2: list = [0] * 26

    count_characters(string1, list1)
    count_characters(string2, list2)
    pos: int = 0
    while pos < len(list1) and is_anagram: # 26 steps max
        if list1[pos] != list2[pos]:
            is_anagram = False
        else:
            pos += 1

    return is_anagram


def count_characters(string: str, arr: list):
    for character in string:
        index: int = ord(character) - ord('a')
        arr[index] += 1


print(anagrams("python", "typhon"))
print(anagrams("abba", "baba"))
print(anagrams("abba", "abbb"))

