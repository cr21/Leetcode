"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.



Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
import  collections
class Solution(object):
    # NlogN Approach
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
#         O(Nlogn)
        return sorted([item**2 for item in A])
    # two poiter approach similar to binary search
    def sortedSquares_using_deque(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #  O(N) using dequeue
        answer = collections.deque()
        l, r = 0, len(A) - 1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left > right:
                answer.appendleft(left * left)
                l += 1
            else:
                answer.appendleft(right * right)
                r -= 1
        return answer

sol=Solution()

print(sol.sortedSquares_using_deque([-9,-1,0,3,10]))
print(sol.sortedSquares_using_deque([-7,-3,2,3,11]))
