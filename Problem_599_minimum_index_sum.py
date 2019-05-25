"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

"""

from operator import itemgetter
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1 = dict()
        # dic2=dict()
        common = []
        min = 10000000000
        for index, element in enumerate(list1):
            dic1[element] = index

        for index,element in enumerate(list2):
            if element in dic1:
                if  index+dic1[element] < min :
                    min = index+dic1[element]
                    common.clear()
                    common.append(list2[index])
                elif index+dic1[element] == min:
                    common.append(list2[index])
        return common

    def findRestaurant1(self, list1, list2):


        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1 = dict()
        dic2=dict()
        for index, element in enumerate(list1):
            dic1[element] = index

        # print(dic1)

        for index,element in enumerate(list2):
            if element in dic1:
                dic2[element]=index+dic1[element]
        minumumValue =min(dic2.values())
        return [key for key in dic2 if dic2[key] == minumumValue]

solution = Solution()
list1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2=["KFC", "Shogun", "Burger King"]
print(solution.findRestaurant(list1,list2))

