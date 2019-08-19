"""



Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""


import math
class Solution(object):
    # simple without using any perticular algorithm
    def isPerfectSquare_simple(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return math.sqrt(num) == int(math.sqrt(num))


simple=Solution()
print(simple.isPerfectSquare_simple(16))# True

print(simple.isPerfectSquare_simple(33))# False
