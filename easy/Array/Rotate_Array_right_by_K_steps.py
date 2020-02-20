"""

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""


class Solution:

    def reverseString(self, s: List[int], start: int, end: int) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        low = start
        high = end

        while low < high:
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1

        return s

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)
        if len(nums) == 1 or k == 0:
            return nums
        nums = self.reverseString(nums, 0, len(nums) - 1)

        nums = self.reverseString(nums, 0, k - 1)

        nums = self.reverseString(nums, k, len(nums) - 1)

        return nums


sol  = Solution()
nums=[1,2,3,4,5,6,7]
k=2
print(sol.rotate(nums,k))