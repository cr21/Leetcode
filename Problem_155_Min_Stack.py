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
# obj = MinStack()
#
# """
# ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
# [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
# """
#
# print(obj.getMin())
# obj.push(2147483646)
# obj.push(2147483646)
# obj.push(2147483647)
# print(obj.top())
# print(obj.pop())
# print(obj.getMin())
# print(obj.pop())
# print(obj.getMin())
# print(obj.pop())
#
# obj.push(2147483647)
# print(obj.top())
# print(obj.getMin())
# obj.push(-2147483648)
# print(obj.top())
# print(obj.getMin())
# print(obj.pop())
# print(obj.getMin())
# minStack = MinStack()
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# print(minStack.stack)
# print("min",minStack.getMin())
# print("pop",minStack.pop());
# print(minStack.top());
# print(minStack.getMin());


"""
Above solution is getting Minimum in O(1) time but it takes extra space we can do it in O(1)
"""




class OptimizedMinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min =None
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append(x)
            self.min = x
        elif x < self.min:
            # we will add 2*newElement - old_min to preserve and get previous minimum if we popped the element
            self.stack.append(2*x-self.min)
            self.min   = x
        else:
            self.stack.append((x))


    def pop(self):
        """
        :rtype: None
        """

        if len(self.stack) == 0 :
            return
        top_element = self.stack[-1]
        if top_element < self.min:
            # old_min = self.min
            self.min = 2*self.min - top_element
            self.stack.pop()
            # return  old_min
        else :
            self.stack.pop()
            # return self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0 :
            return  None
        if self.stack[-1] < self.min:
            return self.min
        return  self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0 :
            return None
        return  self.min

minStack = OptimizedMinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin());

print(minStack.pop());

print(minStack.top());
print(minStack.getMin())


"""
BElow is another great solution

"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s1.append(x)
        if not self.s2:
            self.s2.append(x)
        else:
            top = self.s2[-1]
            if x<top:
                self.s2.append(x)
            else:
                self.s2.append(top)

    def pop(self):
        """
        :rtype: None
        """
        if self.s1:
            self.s1.pop()
            self.s2.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.s1:
            return self.s1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.s2:
            return self.s2[-1]
