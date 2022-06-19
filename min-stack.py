'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
https://leetcode.com/problems/min-stack/
'''

# we have to use two stacks to keep track of the min value
class MinStack:

    def __init__(self):
        self.data = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.data.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
            return
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)

    def pop(self) -> None:
        if len(self.data) != 0:
            pop_val = self.data.pop()
            if pop_val == self.min_stack[-1]:
                self.min_stack.pop()
        return pop_val
            

    def top(self) -> int:
        if len(self.data) !=0:
            return self.data[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
