
class TrieNode:
    def __init__(self, key, parent = None, children: dict = {}):
        self.key = key
        self.parent = parent
        self.children:dict = {}
        self.endchar: bool = False

class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode(None)

    def insert(self, string: str):
        current: TrieNode = self.root
        for character in string:
            if character not in current.children:
                current.children[character] = TrieNode(character, current)
            current = current.children[character]
        current.endchar = True

    def contains(self, string: str)->bool:
        current: TrieNode = self.root
        for character in string:
            if character not in current.children:
                current = None
                break
            current = current.children[character]
        if current is None:
            return False
        return current.endchar

    def delete(self, string: str):
        current: TrieNode = self.root
        for character in string:
            if character not in current.children:
                current = None
                break
            current = current.children[character]
        if current is None:
            return
        current.endchar = False
        parent: TrieNode = current.parent
        while parent is not None and not current.endchar and len(current.children) == 0:
            del(parent.children[current.key])
            current = parent
            parent = current.parent

    def prefix(self, prefix: str)->list:
        current: TrieNode = self.root
        for character in prefix:
            if character not in current.children:
                current = None
                break
            current = current.children[character]
        if current is None:
            return
        words: list = []
        self.helper(current, words, prefix)
        return words

    def helper(self, node: TrieNode, words: list, currentWord: str):
        if node is None:
            return
        if node.endchar:
            words.append(currentWord)
        for key in node.children:
            self.helper(node.children[key], words, currentWord + key)

    def allWords(self)->list:
        words: list = []
        self.helper(self.root, words, "")
        return words

    def count(self)->int:
        return self.countHelper(self.root)

    def countHelper(self, node: TrieNode)->int:
        if node is None:
            return 0
        sum: int = 0
        if node.endchar:
            sum += 1
        for character in node.children:
            sum += self.countHelper(node.children[character])
        return sum

trie = Trie()
trie.insert("javascript")
trie.insert("java")
trie.insert("scala")
trie.insert("scale")
trie.insert("scalable")
trie.insert("perl")

print("Contains 'javascript' : ", trie.contains("javascript"))
print("Contains 'java' : ", trie.contains("java"))
print("Contains 'ruby' : ", trie.contains("ruby"))

#trie.delete("java")
trie.delete("javascript")


print("Contains 'javascript' : ", trie.contains("javascript"))
print("Contains 'java' : ", trie.contains("java"))
print("Contains 'ruby' : ", trie.contains("ruby"))

print(trie.prefix("scal")) # ['scala', 'scalable', 'scale']
print(trie.prefix("java")) # ['java']

print("All words", trie.allWords()) # All words ['java', 'scala', 'scalable', 'scale', 'perl']
print("Count : ", trie.count())