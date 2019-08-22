""""



Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.


"""


class Solution:
    def findRelativeRanks(self, nums) :
        sorted_nums = sorted(nums, reverse=True)
        rank = {}
        for index, ele in enumerate(sorted_nums):
            if index == 0:
                rank[ele] = "Gold Medal"
            elif index == 1:
                rank[ele] = "Silver Medal"
            elif index == 2:
                rank[ele] = "Bronze Medal"
            else:
                rank[ele] = str(index + 1)

        for index, ele in enumerate(nums):
            nums[index] = rank[ele]

        return nums


sol= Solution()
print(sol.findRelativeRanks([15,13,2,17,1,16]))