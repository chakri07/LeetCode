"""

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.

https://leetcode.com/problems/word-search-ii
"""


from collections import deque
class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = (False,None)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()


        # insert words
        for word in words:
            curr_root = root
            for char in word:
                if not char in curr_root.children:
                    curr_root.children[char] = TrieNode()
                curr_root = curr_root.children[char]
            
            curr_root.eow = (True,word)


        ans = set()
        rows = len(board)
        cols = len(board[0])

        neighs = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c,trie_node):

            temp =  board[r][c]
            board[r][c]= '#'

            if trie_node.eow[0]:
                ans.add(trie_node.eow[1])

            for dr,dc in neighs:
                nr,nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols: 
                    if board[nr][nc] in trie_node.children:
                            new_char = board[nr][nc]
                            dfs(nr,nc,trie_node.children[new_char])
            
            board[r][c] = temp
                            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    char = board[r][c]
                    dfs(r,c,root.children[char])

        return list(ans)



# ----------------------------------------------- ---------------------------------------------- ----------------------------------------

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col, trie_node, current_word):
            if trie_node.is_end:
                result.add(current_word)

            if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or board[row][col] not in trie_node.children:
                return

            # it means at least on of the first letters is mataching with the words letter
            visited[row][col] = True

            trie_node = trie_node.children[board[row][col]]
            current_word = current_word + board[row][col]

            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(row + dr, col + dc, trie_node, current_word)

            visited[row][col] = False  # Backtrack

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, "")

        return list(result)
