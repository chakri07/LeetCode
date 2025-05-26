"""

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



https://leetcode.com/problems/serialize-and-deserialize-binary-tree\
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        Using Breadth-First Search (BFS) / Level-Order Traversal.
        """
        if not root:
            return "N"  # Represent an empty tree with "N"

        serialized_nodes = []
        queue = deque([root])

        while queue:
            current_node = queue.popleft()

            if current_node:
                serialized_nodes.append(str(current_node.val))
                queue.append(current_node.left)  # Enqueue left child, even if None
                queue.append(current_node.right) # Enqueue right child, even if None
            else:
                serialized_nodes.append("N") # Mark null nodes

        # Join the list elements with a comma to form the string
        return ",".join(serialized_nodes)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        Using Breadth-First Search (BFS) / Level-Order Traversal.
        """
        if data == "N":
            return None  # If the string is "N", it's an empty tree

        nodes_list = data.split(",") # Split the string back into a list of node values/markers

        # The first element is always the root
        root = TreeNode(int(nodes_list[0]))
        queue = deque([root])
        i = 1 # Start index for processing children

        while queue and i < len(nodes_list):
            parent_node = queue.popleft()

            # Process left child
            if nodes_list[i] != "N":
                left_child_val = int(nodes_list[i])
                parent_node.left = TreeNode(left_child_val)
                queue.append(parent_node.left)
            i += 1

            # Process right child, if available
            if i < len(nodes_list) and nodes_list[i] != "N":
                right_child_val = int(nodes_list[i])
                parent_node.right = TreeNode(right_child_val)
                queue.append(parent_node.right)
            i += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))