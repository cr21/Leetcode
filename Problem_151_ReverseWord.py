
from collections import deque


class Solution(object):
    def reverseWords(self, s):
        s = " ".join(s.split())
        q = deque()
        for word in s.split():
            q.append(word)
        reverseStr = ""
        while len(q) != 0:
            reverseStr += q.pop() + " "
        return reverseStr.strip()

    def reverse(self,s):
        if s == "":
            return  ""
        li = s.split()

        if len(li) == 1:
            return  s.strip()
        li= li[::-1]
        return " ".join(li)
Solution = Solution()
print(Solution.reverseWords("the sky is blue"))
print(Solution.reverseWords("  hello world!  "))
print(Solution.reverseWords("a good   example"))
