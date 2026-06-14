class TrieNode:
    def __init__(self, char = ""):
        self.char = char
        self.children = {}
        self.is_end = False


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()     

    def insert(self, word: str) -> None:
        root = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in root.children:
                root.children[char] = TrieNode(char)
            
            if i == len(word) -1 : 
                root.children[char].is_end = True
            root = root.children[char]


    def search(self, word: str) -> bool:
        root = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in root.children:
                return False
            if i == len(word) -1 and not root.children[char].is_end:
                return False
            
            root = root.children[char]

        return True
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            if char not in root.children:
                return False
            
            root = root.children[char]

        return True

        
        