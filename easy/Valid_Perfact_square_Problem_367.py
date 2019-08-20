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


    #  square number is 1+3+5+7+... Time Complexity O(sqrt(N))
    def isPerfactSquare_using_Sum(self,num):
        """

        :param num: int
        :return: bool
        """
        if (num < 1 ):
            return False
        i=1
        while num >0 :
            num-=i
            i+=2
        return num == 0

    def isPerfactSquare_using_Binary_Search(self, num):
        """

        :param num: int
        :return: bool
        """
        if num == 0 :
            return False
        low ,high = 0, num

        while low <= high:
            mid = low + (high-low)//2
            sq = mid*mid

            if sq == num:
                return True
            elif num < sq:
                high = mid-1
            else:
                low =mid+1

        return False




simple=Solution()
# print(simple.isPerfectSquare_simple(16))# True
#
# print(simple.isPerfectSquare_simple(33))# False

#
# print(simple.isPerfactSquare_using_Sum(16))# True
#
# print(simple.isPerfactSquare_using_Sum(11))# False



print(simple.isPerfactSquare_using_Binary_Search(16))# True

print(simple.isPerfactSquare_using_Binary_Search(9))# False
