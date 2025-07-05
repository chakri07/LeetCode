"""
Given a C++ program, remove comments from it. The program source is an array of strings source where source[i] is the ith line of the source code. This represents the result of splitting the original source code string by the newline character '\n'.

In C++, there are two types of comments, line comments, and block comments.

The string "//" denotes a line comment, which represents that it and the rest of the characters to the right of it in the same line should be ignored.
The string "/*" denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of "*/" should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string "/*/" does not yet end the block comment, as the ending would be overlapping the beginning.
The first effective comment takes precedence over others.

For example, if the string "//" occurs in a block comment, it is ignored.
Similarly, if the string "/*" occurs in a line or block comment, it is also ignored.
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters.

For example, source = "string s = "/* Not a comment. */";" will not be a test case.
Also, nothing else such as defines or macros will interfere with the comments.

It is guaranteed that every open block comment will eventually be closed, so "/*" outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.

 

Example 1:

Input: source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
Explanation: The line by line code is visualized as below:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
The line by line output code is visualized as below:
int main()
{ 
  
int a, b, c;
a = b + c;
}
Example 2:

Input: source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].

https://leetcode.com/problems/remove-comments/description/
"""

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        in_block = False
        result_lines = []
        current_line_buffer = []

        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if i + 1 < len(line) and line[i:i+2] == '*/':
                        in_block = False
                        i += 2
                    else:
                        i += 1
                else:
                    # Check if there are at least 2 characters remaining for '//' or '/*'
                    if i + 1 < len(line) and line[i:i+2] == '//':
                        break # Line comment, ignore rest
                    elif i + 1 < len(line) and line[i:i+2] == '/*':
                        in_block = True
                        i += 2
                    else:
                        # This handles single characters and cases where there aren't enough
                        # characters for a 2-char comment sequence.
                        current_line_buffer.append(line[i])
                        i += 1

            if not in_block and current_line_buffer:
                result_lines.append("".join(current_line_buffer))
                current_line_buffer = []

        return result_lines


class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        inBlock = False
        inLine = False

        ans = []

        for line in source:
            i = 0
            if not inBlock:
                new_line = []
            while i < len(line):
                if line[i:i+2] == '/*' and not inBlock:
                    inBlock = True
                    i += 1
                elif line[i:i+2] == '*/' and inBlock:
                    inBlock = False
                    i += 1
                elif not inBlock and line[i:i+2] == '//':
                    break
                elif not inBlock:
                    new_line.append(line[i])
                i += 1
            if new_line and not inBlock:
                ans.append("".join(new_line))

        return ans