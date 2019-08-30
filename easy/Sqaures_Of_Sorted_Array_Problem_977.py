"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution(object):
    # NlogN Approach
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
#         O(Nlogn)
        return sorted([item**2 for item in A])