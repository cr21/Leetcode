


"""

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        for _s in s.split(" "):
            l.append("".join(self.helper(list(_s), 0, len(_s) - 1)))

        return " ".join(l)

    def helper(self, s, start, end):
        if start >= end:
            return s
        s[start], s[end] = s[end], s[start]
        return self.helper(s, start + 1, end - 1)