"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.


"""


def findPeak_Naive(arr):
    if len(arr)==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[-1]>arr[-2]:
        return len(arr)-1
    for index,ele in enumerate(arr):
        if arr[index+1]<arr[index] and arr[index] > arr[index-1]:
            return index

    return -1


def finaPeak_Efficent(arr):

    low =0
    high = len(arr)-1
    while low < high:
        mid =  (high +low )//2
        if arr[mid] > arr[mid+1]:
            high = mid
        else:
            low = mid+1
    return low





print(findPeak_Naive([1,2,3,1]))

print(findPeak_Naive([1,2,1,3,5,6,4]))

print(finaPeak_Efficent([1,2,3,1]))

print(finaPeak_Efficent([1,2,1,3,5,6,4]))

print(finaPeak_Efficent([1,2,3,4,3]))