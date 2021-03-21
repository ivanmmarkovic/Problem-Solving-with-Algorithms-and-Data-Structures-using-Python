

# O(m * n)
# m - length of the text
# n - length of pattern
def search(text: str, pattern: str) -> int:
    
    t:int = 0
    last_index: int = len(text) - len(pattern) + 1
    
    while t <= len(text) - len(pattern):
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


        