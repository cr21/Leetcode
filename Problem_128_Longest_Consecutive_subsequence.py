"""


Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""


class Solution:
    def longestConsecutive(self, input_list):
        """
        :type nums: List[int]
        :rtype: int
        """

        dic = dict()

        for index, element in enumerate(input_list):
            dic[element] = index
        max_length = 0
        starts_at = len(input_list)

        for index, element in enumerate(input_list):
            current_starts = index
            current_count = 1
            dic[element] = -1

            # search_upward
            current = element + 1
            while current in dic and dic[current] > 0:
                current_count += 1
                dic[current] = -1
                current = current + 1

            current = element - 1
            # search downward
            while current in dic and dic[current] > 0:
                current_starts = dic[current]
                current_count += 1
                dic[current] = -1
                current = current - 1

            if current_count >= max_length:
                if current_count == max_length and current_starts > starts_at:
                    continue
                max_length = current_count
                starts_at = current_starts
        return  max_length
        # if you want to return longest consecutive subsequence then uncomment this

        # start_element = input_list[starts_at]
        # return [num for num in range(start_element, start_element + max_length)]

solution = Solution()
# print(solution.longestConsecutive([1,2,3,4]))
test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
print(solution.longestConsecutive([0, 1, 2, 3, 4]))
# test_function(test_case_3)
print("________________________________")
test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
# test_function(test_case_1)
print(solution.longestConsecutive([5, 4, 7, 10, 1, 3, 55, 2]))

print("______________________________________")
test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ], [8, 9, 10, 11, 12]]
# test_function(test_case_2)
print(solution.longestConsecutive([2, 12, 9, 16, 10, 5, 3, 20, 25, 11, 1, 8, 6 ]))

print("(((((((((((((((((((((((((((((((((((((((((((((")
def longestConsecutive(nums):
    nums = set(nums)
    best = 0
    best_list=[]
    #
    # current_best=[]
    for x in nums:
        current_best = [x]
        if x-1  not in nums:
            y = x+1
            # current_best.append(y)
            # print("current_best")
            while y in nums:
                current_best.append(y)
                y+=1

        best=max(best,y-x)
        best_list.append((len(current_best),current_best))
    print(best_list)
    return  best
print(longestConsecutive([1,12,3,4,5,8,7,6,1,2,3,4,5,6,7,8,9,11,12,13,14,16,15,17,18,19,20,21,22]))