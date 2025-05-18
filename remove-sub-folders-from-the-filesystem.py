"""



https://leetcode.com/problems/remove-sub-folders-from-the-filesystem
"""

from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.is_eof = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()

        for path in folder:
            split = path.split('/')
            node = root
            for f in split:
                if f not in node.children:
                    node.children[f] = Trie()
                node = node.children[f]
            node.is_eof = True  

        result = []
        for path in folder:
            split = path.split('/')
            node = root
            is_subfolder = False
            for i in range(len(split)):
                node = node.children.get(split[i])
                if node.is_eof:
                    if i < len(split) - 1:  
                        is_subfolder = True
                    break  # Once we find a parent, we know it's a subfolder

            if not is_subfolder:
                result.append(path)

        return result