__author__ = "chirag"

"""

Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
"""


class Solution(object):
    def reverse(self, s):
        low = 0
        high = len(s) - 1

        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        return s

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []

        for _s in s.split(" "):
            # print("____________",_s)
            if _s == " " or _s == "":
                continue
            else:
                words.append(_s)
        # print(words)
        words = self.reverse(words)
        return " ".join(words)