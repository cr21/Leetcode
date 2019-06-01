# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def size(self):
#         return len(self.items)
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         if self.size() == 0:
#             return None
#         else:
#             return self.items.pop()
#
#
# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         balanced = True
#         if len(s) == 0:
#             return balanced
#         mystack = Stack()
#         index = 0
#
#
#         while index < len(s):
#             if s[index] == "(" or s[index] == "[" or s[index] == "{":
#                 mystack.push(s[index])
#
#             if s[index] == ")":
#                 if len(mystack.items) == 0:
#                     # balanced = False
#                     return False
#                 if mystack.pop() != "(":
#                     return False
#
#             if s[index] == "]":
#                 if len(mystack.items) == 0:
#                     # balanced = False
#                     return False
#                 if mystack.pop() != "[":
#                     # balanced = False
#                     return False
#
#             if s[index] == "}":
#                 if len(mystack.items) == 0:
#                     # balanced = False
#                     return False
#                 if mystack.pop() != "{":
#                     # balanced = False
#                     return False
#             index = index + 1
#         if balanced and len(mystack.items) == 0:
#             # print("HEYYYY")
#             return True
#         else:
#             # print("&&&&")
#             return False
#
# #
# solution =  Solution()
# print(solution.isValid("["))


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        balanced = True
        if len(s) == 0:
            return balanced
        mystack = Stack()
        index = 0


        while index < len(s):
            if s[index] == "(" or s[index] == "[" or s[index] == "{":
                mystack.push(s[index])

            if s[index] == ")":
                if len(mystack.items) == 0 or mystack.pop() != "(":
                    return False

            if s[index] == "]":
                if len(mystack.items) == 0 or mystack.pop() != "[":
                    # balanced = False
                    return False

            if s[index] == "}":
                if len(mystack.items) == 0 or mystack.pop() != "{":
                    # balanced = False
                    return False

            index = index + 1

        if balanced and len(mystack.items) == 0:
            return True
        else:
            return False

#
solution =  Solution()
print(solution.isValid("["))
