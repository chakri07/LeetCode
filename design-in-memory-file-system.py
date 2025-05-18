"""
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.
 

Example 1:


Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
 

Constraints:

1 <= path.length, filePath.length <= 100
path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that the parent directory for the file in addContentToFile will exist.
1 <= content.length <= 50
At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.


https://leetcode.com/problems/design-in-memory-file-system
"""

from collections import defaultdict
from typing import List

class Folder:
    def __init__(self):
        # dictionary of folder structures
        self.folders = {}
        # dictionary of files (filename: content)
        self.files = {}

class FileSystem:

    def __init__(self):
        self.root = Folder()

    def ls(self, path: str) -> List[str]:
        node = self.root
        folders = [f for f in path.split('/') if f]

        if not folders:
            # root directory
            return sorted(list(node.folders.keys()) + list(node.files.keys()))

        for i in range(len(folders) - 1):
            folder_name = folders[i]
            if folder_name not in node.folders:
                return []  # Path not found
            node = node.folders[folder_name]

        last = folders[-1]
        if last in node.folders:
            # It's a folder
            node = node.folders[last]
            return sorted(list(node.folders.keys()) + list(node.files.keys()))
        elif last in node.files:
            # It's a file
            return [last]
        else:
            return []  # Not found


    def mkdir(self, path: str) -> None:
        node = self.root
        folders = [f for f in path.split('/') if f]
        for folder_name in folders:
            if folder_name not in node.folders:
                node.folders[folder_name] = Folder()
            node = node.folders[folder_name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        folders = [f for f in filePath.split('/') if f]
        filename = folders[-1]
        for folder_name in folders[:-1]:
            if folder_name not in node.folders:
                node.folders[folder_name] = Folder()
            node = node.folders[folder_name]

        if filename not in node.files:
            node.files[filename] = ""
        node.files[filename] += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        folders = [f for f in filePath.split('/') if f]
        filename = folders[-1]
        for folder_name in folders[:-1]:
            if folder_name not in node.folders:
                return "" # Or raise an error, depending on desired behavior
            node = node.folders[folder_name]

        return node.files.get(filename, "")

# Example Usage (for testing):
# obj = FileSystem()
# obj.mkdir("/a")
# obj.mkdir("/a/b")
# obj.addContentToFile("/a/b/file.txt", "Hello ")
# obj.addContentToFile("/a/b/file.txt", "World!")
# print(obj.readContentFromFile("/a/b/file.txt"))
# print(obj.ls("/a"))
# print(obj.ls("/a/b"))
# print(obj.ls("/a/b/file.txt"))