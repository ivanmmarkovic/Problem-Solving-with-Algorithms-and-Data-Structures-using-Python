
# O(n2)
def anagrams(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    is_anagram: bool = True

    list2: list = list(string2)
    pos1: int = 0
    while pos1 < len(string1) and is_anagram:
        character = string1[pos1]
        character_found: bool = False
        pos2: int = 0
        while pos2 < len(list2) and not character_found:
            if list2[pos2] == character:
                list2[pos2] = None
                character_found = True
            else:
                pos2 += 1
        if not character_found:
            is_anagram = False
        else:
            pos1 += 1

    return is_anagram


print(anagrams("python", "typhon"))
print(anagrams("abba", "baba"))
print(anagrams("abba", "abbb"))

