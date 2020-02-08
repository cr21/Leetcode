"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        count = 0
        while count < len(s) - 1:
            remaining_length = len(s) - count
            #             if remaining length is less than K then go for remainng length index
            if k > remaining_length:
                s = self.helper(list(s), count, count + remaining_length - 1)
                return "".join(s)
            s = self.helper(list(s), count, count + k - 1)
            count += 2 * k

        return "".join(s)

    def helper(self, s, start, end):
        if start >= end:
            return s
        s[start], s[end] = s[end], s[start]
        return self.helper(s, start + 1, end - 1)