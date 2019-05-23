"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append((x,x))
        elif x < self.stack[-1][1]:
            self.stack.append((x,x))
        else:
            self.stack.append((x,self.stack[-1][1]))


    def pop(self):
        """
        :rtype: None
        """
        if self.top() is None:
            return None
        popped = self.stack.pop()
        return  popped[0]
    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0 :
            return  None
        return  self.stack[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0 :
            return None
        return  self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# Your MinStack object will be instantiated and called as such:
obj = MinStack()

"""
["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
"""

print(obj.getMin())
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
print(obj.top())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.pop())

obj.push(2147483647)
print(obj.top())
print(obj.getMin())
obj.push(-2147483648)
print(obj.top())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
# minStack = MinStack()
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# print(minStack.stack)
# print("min",minStack.getMin())
# print("pop",minStack.pop());
# print(minStack.top());
# print(minStack.getMin());