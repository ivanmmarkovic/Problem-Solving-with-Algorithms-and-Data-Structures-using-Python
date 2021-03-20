

# O(m * n)
# m - length of the text
# n - length of pattern
def search(text: str, pattern: str) -> int:

    last_index: int = len(text) - len(pattern) + 1
    for t in range(last_index):
        p:int = 0
        while p < len(pattern):
            if text[t + p] != pattern[p]:
                break
            else:
                p += 1
        if p == len(pattern):
            return t
        t += 1
    return -1


        